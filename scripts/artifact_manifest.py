#!/usr/bin/env python3
"""Record or verify source/export hashes. This does not prove model equivalence."""
import argparse
import hashlib
import json
import os
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['record','verify'])
    parser.add_argument('files',nargs='*',type=Path)
    parser.add_argument('--manifest',required=True,type=Path)
    args=parser.parse_args()
    base=args.manifest.resolve().parent
    if args.action=='record':
        if len(args.files)<2:
            parser.error('record needs a source followed by at least one export')
        data={'scope':'Hash freshness record, not embedded-model equivalence. First entry is the source.',
              'files':[{'path':os.path.relpath(p.resolve(),base),'sha256':digest(p)} for p in args.files]}
        base.mkdir(parents=True,exist_ok=True)
        args.manifest.write_text(json.dumps(data,indent=2)+'\n')
        print(f'Recorded {len(args.files)} artifacts')
    else:
        data=json.loads(args.manifest.read_text())
        if not data.get('files'):
            parser.error('manifest contains no files')
        failed=[]
        for item in data['files']:
            path=base/item['path']
            if not path.is_file() or digest(path)!=item['sha256']:
                failed.append(item['path'])
        if failed:
            print('Changed or missing: '+', '.join(failed))
            return 1
        print(f'Verified {len(data["files"])} artifact hashes')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
