// Export browser-rendered SVG, including common Draw.io foreignObject labels.
import fs from 'node:fs';
import {chromium,svgBody,option} from './browser.mjs';
const args=process.argv.slice(2);
if (!args[0] || args.includes('--help')) {
  console.log('Usage: node scripts/export_pdf.mjs INPUT.svg --width-mm 88 --output OUTPUT.pdf');
  process.exit(args.includes('--help')?0:2);
}
const width=Number(option(args,'--width-mm','88'));
if(!Number.isFinite(width)||width<=0)throw new Error('Width must be finite and positive.');
const output=option(args,'--output',args[0].replace(/\.svg$/i,'.pdf'));
if(output===args[0])throw new Error('Output must differ from input.');
const svg=svgBody(fs.readFileSync(args[0],'utf8'));
const match=svg.match(/viewBox=["']([^"']+)["']/);
if(!match)throw new Error('SVG needs an explicit viewBox for physical-size export.');
const view=match[1].trim().split(/[\s,]+/).map(Number);
if(view.length!==4||!view.every(Number.isFinite)||view[2]<=0||view[3]<=0)throw new Error('Invalid SVG viewBox.');
const height=width*view[3]/view[2];
const browser=await (await chromium()).launch({headless:true});
try {
  const page=await browser.newPage();
  await page.setContent(`<html><head><style>@page{size:${width}mm ${height}mm;margin:0}html,body{margin:0;padding:0;background:white;color-scheme:light}body>svg{display:block;width:${width}mm;height:${height}mm}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}</style></head><body>${svg}</body></html>`);
  await page.evaluate(()=>document.fonts.ready);
  await page.pdf({path:output,width:`${width}mm`,height:`${height}mm`,printBackground:true,preferCSSPageSize:true,margin:{top:0,bottom:0,left:0,right:0}});
  console.log(`Exported ${width.toFixed(2)} x ${height.toFixed(2)} mm: ${output}`);
} finally {await browser.close();}
