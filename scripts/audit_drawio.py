#!/usr/bin/env python3
"""Structural checks for native Draw.io. No third-party dependencies."""
import argparse
import base64
import hashlib
import json
import math
from pathlib import Path
import urllib.parse
import xml.etree.ElementTree as ET
import zlib


def models(path):
    root = ET.parse(path).getroot()
    if root.tag == 'mxGraphModel':
        return [('page-1', root)]
    if root.tag != 'mxfile':
        raise ValueError('Expected mxfile or mxGraphModel; image exports need extraction first.')
    pages = []
    for i, page in enumerate(root.findall('diagram')):
        model = page.find('mxGraphModel')
        if model is None and (page.text or '').strip():
            content = page.text.strip()
            if not content.startswith('<'):
                content = urllib.parse.unquote(zlib.decompress(base64.b64decode(content), -15).decode())
            model = ET.fromstring(content)
        if model is None or model.tag != 'mxGraphModel':
            raise ValueError(f'Page {i + 1} has no supported model.')
        pages.append((page.get('name', f'page-{i + 1}'), model))
    if not pages:
        raise ValueError('No diagram pages found.')
    return pages


def styles(cell):
    return dict(item.split('=', 1) for item in cell.get('style', '').split(';') if '=' in item)


def cells_from(model):
    root = model.find('root')
    if root is None:
        raise ValueError('Model has no root.')
    result = []
    for item in root:
        if item.tag == 'mxCell':
            result.append(item)
        elif item.tag in ('object', 'UserObject') and item.find('mxCell') is not None:
            cell = ET.fromstring(ET.tostring(item.find('mxCell')))
            if item.get('id'):
                cell.set('id', item.get('id'))
            if item.get('label') is not None:
                cell.set('value', item.get('label'))
            if item.get('drsRole'):
                cell.set('drsRole', item.get('drsRole'))
            result.append(cell)
        else:
            raise ValueError(f'Unsupported root child: {item.tag}')
    return result


def audit(path, min_segment=12):
    errors, warnings, pages = [], [], []
    for name, model in models(path):
        items = cells_from(model)
        cs = {c.get('id'): c for c in items}
        if None in cs or len(cs) != len(items):
            errors.append(f'{name}: duplicate or missing cell IDs')
            continue
        valid = True
        for cell in items:
            for key in ('parent', 'source', 'target'):
                if cell.get(key) and cell.get(key) not in cs:
                    errors.append(f'{name}/{cell.get("id")}: missing {key} {cell.get(key)}')
                    valid = False
            seen, current = set(), cell
            while current is not None:
                cid = current.get('id')
                if cid in seen:
                    errors.append(f'{name}/{cell.get("id")}: parent cycle')
                    valid = False
                    break
                seen.add(cid)
                current = cs.get(current.get('parent'))
        if not valid:
            continue

        def geometry(cid):
            c = cs[cid]
            g = c.find('mxGeometry')
            if g is None:
                return (0., 0., 0., 0.)
            if g.get('relative') == '1' and c.get('vertex') == '1':
                raise ValueError('relative vertex/edge label requires renderer-aware geometry')
            values = tuple(float(g.get(k, '0')) for k in ('x', 'y', 'width', 'height'))
            if not all(math.isfinite(v) for v in values) or min(values[2:]) < 0:
                raise ValueError('invalid or nonfinite geometry')
            x, y, w, h = values
            parent = c.get('parent')
            if parent in cs:
                px, py, _, _ = geometry(parent)
                x, y = x + px, y + py
            return x, y, w, h

        segments, routed, skipped, labels = [], 0, [], 0
        for cid, cell in cs.items():
            labels += bool(cell.get('value'))
            if cell.get('vertex') == '1':
                try:
                    x, y, w, h = geometry(cid)
                    parent = cs.get(cell.get('parent'))
                    if parent is not None and parent.get('drsRole') == 'frame':
                        px, py, pw, ph = geometry(parent.get('id'))
                        if x < px or y < py or x+w > px+pw or y+h > py+ph:
                            errors.append(f'{name}/{cid}: geometry extends outside parent frame')
                except ValueError as exc:
                    if 'relative vertex' in str(exc):
                        skipped.append(f'{cid}: {exc}')
                    else:
                        errors.append(f'{name}/{cid}: {exc}')
                if 'image=http' in cell.get('style', ''):
                    warnings.append(f'{name}/{cid}: external image dependency')
            if cell.get('edge') != '1':
                continue
            if not cell.get('source') or not cell.get('target'):
                errors.append(f'{name}/{cid}: edge has no attached source/target')
                continue
            if cell.get('drsRole') != 'workflow':
                continue
            s = styles(cell)
            try:
                a, b = geometry(cell.get('source')), geometry(cell.get('target'))
                # Renderer-derived perimeter routes need separate coverage.
                if any(a[2:]) or any(b[2:]):
                    if s.get('exitPerimeter') != '0' or s.get('entryPerimeter') != '0':
                        skipped.append(f'{cid}: perimeter route not reconstructed')
                        continue
                start = (a[0] + a[2]*float(s.get('exitX', '.5')), a[1] + a[3]*float(s.get('exitY', '.5')))
                end = (b[0] + b[2]*float(s.get('entryX', '.5')), b[1] + b[3]*float(s.get('entryY', '.5')))
                px, py, _, _ = geometry(cell.get('parent', '1'))
                points = [start] + [(float(p.get('x'))+px, float(p.get('y'))+py) for p in cell.findall('./mxGeometry/Array/mxPoint')] + [end]
                routed += 1
                for a, b in zip(points, points[1:]):
                    if abs(a[0]-b[0]) > .01 and abs(a[1]-b[1]) > .01:
                        errors.append(f'{name}/{cid}: diagonal workflow segment')
                    if math.dist(a,b) < min_segment:
                        errors.append(f'{name}/{cid}: workflow segment shorter than {min_segment:g}')
                    segments.append((cid,a,b))
            except (ValueError, TypeError) as exc:
                errors.append(f'{name}/{cid}: {exc}')

        def crosses(a,b,c,d):
            if abs(a[0]-b[0]) < .01 and abs(c[1]-d[1]) < .01:
                return min(c[0],d[0]) < a[0] < max(c[0],d[0]) and min(a[1],b[1]) < c[1] < max(a[1],b[1])
            if abs(a[1]-b[1]) < .01 and abs(c[0]-d[0]) < .01:
                return crosses(c,d,a,b)
            return False
        for i,(cid,a,b) in enumerate(segments):
            for did,c,d in segments[i+1:]:
                if cid != did and crosses(a,b,c,d):
                    errors.append(f'{name}: workflow crossing {cid} / {did}')
        if not routed:
            warnings.append(f'{name}: no explicit workflow routes checked; route coverage absent')
        if not labels:
            warnings.append(f'{name}: no labels found')
        pages.append(dict(name=name,cells=len(cs),labels=labels,workflow_routes_checked=routed,skipped=skipped))
    return dict(source=Path(path).name,source_sha256=hashlib.sha256(Path(path).read_bytes()).hexdigest(),pages=pages,errors=errors,warnings=warnings,scope='Structural only; rendered text, perimeter routes, junctions, and scientific semantics need separate review.')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source',type=Path)
    p.add_argument('--min-segment',type=float,default=12)
    p.add_argument('--report',type=Path)
    args=p.parse_args()
    if not math.isfinite(args.min_segment) or args.min_segment <= 0:
        p.error('--min-segment must be finite and positive')
    try:
        report=audit(args.source,args.min_segment)
    except (ValueError,ET.ParseError,OSError,zlib.error) as exc:
        p.exit(2,f'Cannot audit source: {exc}\n')
    output=json.dumps(report,indent=2)
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True)
        args.report.write_text(output+'\n')
    print(output)
    return bool(report['errors'])

if __name__=='__main__':
    raise SystemExit(main())
