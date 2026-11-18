#!/usr/bin/env python3
"""Check repository links, required files, language policy, and path portability."""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote

root=Path(__file__).resolve().parents[1]
errors=[]
required=['SKILL.md','README.md','README.zh-CN.md','LICENSE','NOTICE','ACKNOWLEDGMENTS.md','agents/openai.yaml','assets/presets/circuit-academic.json']
for name in required:
    if not (root/name).is_file():errors.append('Missing: '+name)
files=[p for p in root.rglob('*') if p.is_file() and not any(x in p.parts for x in ['work','node_modules','.git','__pycache__'])]
for p in files:
    if p.suffix not in ['.md','.py','.mjs','.json','.yaml','.yml']:continue
    text=p.read_text(encoding='utf-8');rel=str(p.relative_to(root))
    if p.name!='README.zh-CN.md' and re.search('[\u3400-\u9fff]',text):errors.append('Non-English prose: '+rel)
    if re.search(r'/(?:data/home|workspace)/',text):errors.append('Machine-specific path: '+rel)
    if p.suffix=='.json':
        try:json.loads(text)
        except ValueError as e:errors.append(rel+': '+str(e))
    if p.suffix=='.md':
        # Check file targets; web URLs and intra-document anchors are intentionally excluded.
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text):
            target=target.split('#')[0].strip('<>')
            if not target or re.match(r'[a-zA-Z]+:',target):continue
            if not (p.parent/unquote(target)).exists():errors.append(f'{rel}: broken link {target}')
entry=(root/'SKILL.md').read_text(encoding='utf-8')
if not re.match(r'---\nname: drawio-research-skill\ndescription: .+\n---',entry):errors.append('Invalid skill frontmatter')
if len(entry.splitlines())>100:errors.append('Entrypoint exceeds the project 100-line target')
print(json.dumps({'checked_files':len(files),'errors':errors},indent=2))
sys.exit(bool(errors))
