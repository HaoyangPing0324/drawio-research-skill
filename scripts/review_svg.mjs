// Browser-space checks: no assumed source-to-render scale.
import fs from 'node:fs';
import {chromium,svgBody,option} from './browser.mjs';
const args=process.argv.slice(2);
if (!args[0] || args.includes('--help')) {
  console.log('Usage: node scripts/review_svg.mjs INPUT.svg [--report REPORT.json]');
  process.exit(args.includes('--help')?0:2);
}
const browser=await (await chromium()).launch({headless:true});
try {
  const page=await browser.newPage({viewport:{width:2400,height:1800}});
  await page.setContent(`<html><body style="margin:0;background:white">${svgBody(fs.readFileSync(args[0],'utf8'))}</body></html>`);
  await page.evaluate(()=>document.fonts.ready);
  const result=await page.evaluate(async()=>{
    const bounds=e=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,w:r.width,h:r.height};};
    const visible=e=>{const s=getComputedStyle(e),r=bounds(e);return s.display!=='none'&&s.visibility!=='hidden'&&+s.opacity!==0&&r.w>0&&r.h>0;};
    const html=[...document.querySelectorAll('foreignObject div')].filter(e=>e.style.fontSize&&e.style.fontSize!=='0px'&&e.innerText.trim()&&visible(e));
    const nodes=[...html,...document.querySelectorAll('svg text')].filter(e=>visible(e)&&!e.closest('switch')?.querySelector('foreignObject'));
    // The switch exclusion concerns fallback SVG text only, not the HTML labels.
    const labels=[...html,...nodes.filter(e=>e.tagName.toLowerCase()==='text')].map(e=>({text:(e.innerText||e.textContent).trim(),...bounds(e)}));
    const images=[...document.querySelectorAll('svg image')].filter(visible);
    const imageFailures=[];
    for (const [index,e] of images.entries()) {
      const url=e.getAttribute('href')||e.getAttribute('xlink:href');
      const ok=await new Promise(resolve=>{const im=new Image();const timer=setTimeout(()=>resolve(false),3000);im.onload=()=>{clearTimeout(timer);resolve(true);};im.onerror=()=>{clearTimeout(timer);resolve(false);};im.src=url||'';});
      if(!ok) imageFailures.push(index);
    }
    const overlap=(a,b)=>Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x)>.3&&Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y)>.3;
    const textOverlaps=[],iconOverlaps=[],ruleContacts=[],skipped=[];
    for(let i=0;i<labels.length;i++) for(let j=i+1;j<labels.length;j++) if(overlap(labels[i],labels[j]))textOverlaps.push([labels[i].text,labels[j].text]);
    for(const a of labels) for(const [i,e] of images.entries()) if(overlap(a,bounds(e)))iconOverlaps.push({text:a.text,image:i});
    const rects=[...document.querySelectorAll('svg rect')].filter(e=>visible(e)&&getComputedStyle(e).stroke!=='none'&&parseFloat(getComputedStyle(e).strokeWidth)>0);
    for(const [index,e] of rects.entries()) {
      const m=e.getScreenCTM();
      if(!m || Math.abs(m.b)>.001 || Math.abs(m.c)>.001){skipped.push(`rectangle ${index}: non-axis-aligned transform`);continue;}
      const b=bounds(e),s=parseFloat(getComputedStyle(e).strokeWidth)*Math.max(Math.abs(m.a),Math.abs(m.d))/2;
      for(const a of labels){
        const ox=a.x<b.x+b.w+s&&a.x+a.w>b.x-s,oy=a.y<b.y+b.h+s&&a.y+a.h>b.y-s;
        const horizontal=ox&&[b.y,b.y+b.h].some(y=>a.y-s<y&&y<a.y+a.h+s);
        const vertical=oy&&[b.x,b.x+b.w].some(x=>a.x-s<x&&x<a.x+a.w+s);
        if(horizontal||vertical)ruleContacts.push({text:a.text,rectangle:index});
      }
    }
    return {labels:labels.length,images:images.length,rectanglesChecked:rects.length-skipped.length,textOverlaps,iconOverlaps,ruleContacts,imageFailures,skipped,scope:'Browser text bounds and axis-aligned rect borders only. Paths, padding, arrow visibility, semantics, and physical readability require visual review.'};
  });
  const report=option(args,'--report',null);
  if(report) fs.writeFileSync(report,JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify(result,null,2));
  if(!result.labels||result.textOverlaps.length||result.iconOverlaps.length||result.ruleContacts.length||result.imageFailures.length)process.exitCode=1;
} finally {await browser.close();}
