#!/usr/bin/env python3
"""Original overview of the cited technical report; all geometry is editable."""
from pathlib import Path
import xml.etree.ElementTree as E
OUT=Path(__file__).resolve().parent
N='#282B30';B='#D5E4EE';G='#DCEBE3';A='#F0E3C7';P='#E7E1EE';T='#327F75';R='#A2574C'
mx=E.Element('mxfile',host='app.diagrams.net');d=E.SubElement(mx,'diagram',id='deepseek-overview',name='DeepSeek V4.1 Flash overview')
m=E.SubElement(d,'mxGraphModel',page='1',pageWidth='580',pageHeight='630',background='#FFFFFF');root=E.SubElement(m,'root');E.SubElement(root,'mxCell',id='0');E.SubElement(root,'mxCell',id='1',parent='0')
def box(cid,x,y,w,h,label='',fill='none',stroke=N,sw=1,fs=16,parent='1',role='component',extra=''):
 st=f'rounded=0;html=0;whiteSpace=wrap;overflow=visible;fontFamily=Times New Roman;fontSize={fs};fontStyle=1;fontColor={N};align=center;verticalAlign=middle;spacing=0;fillColor={fill};strokeColor={stroke};strokeWidth={sw};'+extra
 c=E.SubElement(root,'mxCell',id=cid,value=label,vertex='1',parent=parent,style=st,drsRole=role);E.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
def txt(cid,x,y,w,h,label,fs=16,parent='1',extra=''):box(cid,x,y,w,h,label,stroke='none',fs=fs,parent=parent,role='label',extra=extra)
def line(cid,pts,parent='1',arrow=False,color=N,sw=1,main=False,dash=False):
 for k,p in [('a',pts[0]),('b',pts[-1])]:box(cid+'-'+k,*p,0,0,stroke='none',parent=parent,role='port')
 st=f'edgeStyle=none;rounded=0;strokeColor={color};strokeWidth={sw};endArrow={"block" if arrow else "none"};endSize=4;endFill=1;exitX=0;exitY=0;entryX=0;entryY=0;exitPerimeter=0;entryPerimeter=0;'+('dashed=1;dashPattern=4 3;' if dash else '')
 c=E.SubElement(root,'mxCell',id=cid,edge='1',source=cid+'-a',target=cid+'-b',parent=parent,style=st,drsRole='workflow' if main else 'wire');geo=E.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
 if len(pts)>2:
  ar=E.SubElement(geo,'Array',attrib={'as':'points'})
  for x,y in pts[1:-1]:E.SubElement(ar,'mxPoint',x=str(x),y=str(y))
def grid(cid,x,y,cols,rows,step=8,parent='1',fill=B):
 for row in range(rows):
  for col in range(cols):box(f'{cid}-{row}-{col}',x+col*step,y+row*step,step-2,step-2,fill=fill if col%3!=2 else G,sw=.5,parent=parent,role='detail')
def doc(cid,x,y,parent):
 box(cid,x,y,24,28,fill='#FFFFFF',sw=.85,parent=parent)
 for j in range(3):box(cid+'-rule-'+str(j),x+4,y+6+j*7,16 if j<2 else 11,1,fill=N,stroke='none',parent=parent,role='detail')
def panel(cid,y,h,title):
 box(cid,10,y,560,h,fill='#FFFFFF',sw=2.2,role='frame');txt(cid+'-head',8,3,544,25,title,18,parent=cid)

txt('title',10,5,560,26,'DeepSeek-V4.1-Flash',23)
txt('size',10,32,560,20,'552B backbone · 196B Engram · Up to 1M context',16)
panel('arch',58,208,'A · Causal encoder–decoder')
# Image and text pathways stay distinct until embeddings enter the backbone.
grid('image',21,34,3,2,parent='arch');txt('image-label',48,33,58,20,'Image',14,parent='arch')
box('vision',10,59,96,24,'ViT → MLP',B,fs=15,parent='arch')
line('vision-input',[(106,69),(118,69),(118,85),(130,85)],'arch',arrow=True,sw=.9,main=True)
box('text-input',10,94,96,23,'Text tokens',G,fs=15,parent='arch')
line('text-encoder',[(106,109),(118,109),(118,97),(130,97)],'arch',arrow=True,sw=.9,main=True)
box('encoder',132,33,172,87,fill='#F5F8FA',sw=1.05,parent='arch')
txt('encoder-title',136,37,164,20,'Encoder · 20 layers',16,parent='arch')
for j in range(3):box('enc-layer-'+str(j),143,62+j*13,37,10,fill=B if j==0 else A,sw=.65,parent='arch',role='detail')
txt('enc-csa',185,63,113,18,'CSA2 · ratio 2',14.5,parent='arch')
txt('enc-swa',185,83,113,28,'First 2 layers:\nSWA only',13.5,parent='arch')
box('decoder',342,33,207,87,fill='#F4F8F5',sw=1.05,parent='arch')
txt('decoder-title',347,37,197,20,'Decoder · 20 layers',16,parent='arch')
for j in range(3):box('dec-layer-'+str(j),354,62+j*13,37,10,fill=G if j==0 else A,sw=.65,parent='arch',role='detail')
txt('dec-csa',397,63,147,18,'CSA2 · ratio 1',14.5,parent='arch')
txt('dec-output',397,84,147,27,'Autoregressive\ntext output',13.5,parent='arch')
line('encoder-decoder',[(305,78),(340,78)],'arch',arrow=True,sw=1.3,main=True)
txt('projection',128,122,423,20,'Decoder global KV ← final encoder states',15,parent='arch')
txt('activation',10,143,539,20,'Active parameters: 8B prefill / 16B decode',16,parent='arch')
# Native expert routing and residual/drafting motifs remain attached to labels.
for j in range(6):box('expert-'+str(j),13+j*8,177,6,10,fill=B if j<3 else G,sw=.45,parent='arch',role='detail')
txt('moe',66,167,190,32,'MoE: 1 shared + 384 routed\n6 routed experts active',13.5,parent='arch')
line('extensions-divide',[(264,167),(264,199)],'arch',sw=.6,color='#9DA6AA')
txt('extensions',273,165,274,36,'Single-Pass mHC · Engram\nDSpark: draft → verify',14,parent='arch')

panel('cache',274,174,'B · Cross-layer reuse + cache compression')
# A compact native table expresses the three static modes, not three serial stages.
for x,w,title,cid in [(7,89,'CSA2 mode','mode-key'),(98,65,'Full','full'),(166,77,'Reindex','reindex'),(246,65,'Reuse','reuse')]:txt(cid,x,29,w,20,title,14.5,parent='cache')
for row,(label,values) in enumerate([('Global KV',['New','Shared','Shared']),('Top-K',['New','New','Shared'])]):
 y=52+row*25;txt('row-'+str(row),7,y,89,22,label,14.5,parent='cache')
 for col,(x,w) in enumerate([(98,65),(166,77),(246,65)]):box(f'mode-{row}-{col}',x,y,w,22,values[col],G if values[col]=='New' else A,sw=.65,fs=14,parent='cache')
txt('local-kv',8,102,304,19,'Every layer: own Q + SWA KV',14,parent='cache')
line('cache-divider',[(320,30),(320,121)],'cache',sw=.7,color='#9DA6AA')
grid('cache-bits',333,35,4,2,step=7,parent='cache',fill=P)
txt('fp4',365,29,182,23,'FP4 main KV',16,parent='cache')
txt('global-size',328,54,220,26,'890 B/token · HBM',18,parent='cache')
txt('global-ratio',328,81,220,22,'≈ 1/4 global KV',16,parent='cache')
txt('baseline',328,103,220,17,'vs. DeepSeek-V4-Flash',12.5,parent='cache')
# Shared candidate pool and bounded replay are separate cost reductions.
for j in range(8):box('candidate-'+str(j),12+j*7,130,5,7,fill=G if j<3 else B,sw=.4,parent='cache',role='detail')
txt('pool',76,124,230,23,'Decoder pool ≤ 16,384 → 512',13.5,parent='cache')
for j in range(8):box('replay-token-'+str(j),12+j*7,151,5,7,fill=A if j<5 else G,sw=.4,parent='cache',role='detail')
txt('replay',76,146,230,22,'Replay 128 tokens · approximate',13.5,parent='cache')
box('ssd',332,131,24,29,fill=P,sw=.8,parent='cache')
for j in range(3):line('ssd-slot-'+str(j),[(336,137+j*8),(352,137+j*8)],'cache',sw=.6)
txt('persistent-ratio',363,124,184,23,'≈ 1/8 persistent KV',15.5,parent='cache')
txt('persistent-caption',361,147,188,18,'SSD/host: global KV only',13,parent='cache')

panel('training',456,152,'C · Training, evidence & boundaries')
doc('corpus',12,37,'training');txt('corpus-label',40,32,118,39,'45T multimodal\n64K → 1M context',14,parent='training')
for cid,x,w,label,fill in [('sft',181,66,'SFT',B),('rl',271,66,'RL',G),('opd',361,66,'OPD',P)]:box(cid,x,39,w,26,label,fill,fs=16,parent='training')
for cid,a,b in [('pre-sft',158,179),('sft-rl',248,269),('rl-opd',338,359)]:line(cid,[(a,52),(b,52)],'training',arrow=True,sw=1.1,main=True)
txt('teachers',434,34,115,35,'40+ teachers\n(final OPD)',13.5,parent='training')
txt('infrastructure',10,76,540,20,'Async RL / OPD · DSec sandboxes · Effort 1–100',15,parent='training')
line('eval-separator',[(10,101),(550,101)],'training',sw=.65,color='#9DA6AA')
txt('metrics',8,104,544,20,'GPQA 90.9% · DeepSWE 74.2% · TB 2.1 90.6%',16,parent='training')
txt('metric-scope',10,125,540,20,'Reported at max effort; benchmark-specific harnesses',13.5,parent='training')
txt('limits',10,613,560,20,'Limits: sparse-selection errors / approximate replay boundaries',14,extra=f'fontColor={R};')
txt('citation',10,635,560,18,'Source: DeepSeek-AI technical report (2026), §§2–6; schematic overview.',12)
m.set('pageHeight','665')
E.indent(mx);E.ElementTree(mx).write(OUT/'overview.drawio',encoding='utf-8',xml_declaration=True)
print('Generated',len(root),'native cells')
