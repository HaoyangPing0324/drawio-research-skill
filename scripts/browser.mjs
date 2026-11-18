// Optional dependency adapter. No machine-specific paths.
import {pathToFileURL} from 'node:url';
export async function chromium() {
  try {
    const mod = process.env.PLAYWRIGHT_MODULE
      ? await import(pathToFileURL(process.env.PLAYWRIGHT_MODULE).href)
      : await import('playwright');
    return mod.chromium;
  } catch (error) {
    throw new Error('Playwright is unavailable. Run npm install in the repository, or set PLAYWRIGHT_MODULE to its absolute index.mjs path.', {cause:error});
  }
}
export function svgBody(text) {
  if (!/<svg\b/.test(text)) throw new Error('Expected SVG input.');
  return text.replace(/<\?xml[^>]*>/g,'').replace(/<!DOCTYPE[^>]*>/g,'');
}
export function option(args,name,fallback) {
  const i=args.indexOf(name);
  if (i<0) return fallback;
  if (!args[i+1] || args[i+1].startsWith('--')) throw new Error(`Missing value for ${name}`);
  return args[i+1];
}
