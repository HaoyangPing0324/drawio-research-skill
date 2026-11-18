# Export and review

## Capability setup

The required capabilities are a native model editor/generator, a Draw.io renderer, and an image viewer. Python 3 runs the included structural audit. Node.js and a local Playwright package are optional for SVG measurement and PDF output. Rendering the source still requires an actual Draw.io renderer.

For the optional browser tools, from the repository root:

```bash
npm install
npx playwright install chromium
```

Use the lockfile with `npm ci` when present. An existing installation can instead be selected through `PLAYWRIGHT_MODULE`, an absolute path to Playwright's `index.mjs`; browser and operating-system prerequisites remain the operator's environment. Missing prerequisites must not be mistaken for a diagram defect.

## Commands for a user-provided figure

```bash
python3 scripts/audit_drawio.py figure.drawio --report geometry-audit.json
```

Choose one available renderer. These are alternatives, not interchangeable interfaces:

```bash
# Draw.io Desktop; confirm flags with the installed binary's help.
drawio --export --format png --scale 3 --border 8 --output figure.drawio.png figure.drawio
drawio --export --format svg --border 8 --output figure.drawio.svg figure.drawio

# Optional BRBussy/draw-io-cli checkout; not bundled with this repository.
node /path/to/draw-io-cli/src/cli.js render figure.drawio --png --svg
```

After rendering:

```bash
node scripts/review_svg.mjs figure.drawio.svg --report render-audit.json
node scripts/export_pdf.mjs figure.drawio.svg --width-mm 88 --output figure.pdf
python3 scripts/artifact_manifest.py record figure.drawio figure.drawio.png figure.drawio.svg figure.pdf --manifest artifacts.json
python3 scripts/artifact_manifest.py verify --manifest artifacts.json
```

Do not record the final manifest before reviewing the outputs. Re-record only after intentional changes and fresh validation; otherwise verification would merely bless stale exports. Where the exporter supports embedded-model comparison, use that as well.

## Four review layers

### 1. Structural and content review

Check source fidelity, required labels/artifacts, conditional branches, evidence status, unique IDs, existing references, parent containment, and route classes. The included `audit_drawio.py` accepts compressed or uncompressed pages, checks reference integrity and explicit orthogonal workflow routes, and reports unsupported route coverage. It does not prove semantic accuracy or actual text clearance.

The role-based audit deliberately treats internal circuit wires separately. Supply `--min-segment` according to the local policy. Do not reduce it solely to conceal a short main-flow arrow. Examine all reported skipped cases before describing the result.

### 2. Rendered geometry review

Run `review_svg.mjs` to inspect actual browser text boxes. It handles SVG text and common Draw.io HTML labels and reports text/text overlaps, text/image overlaps, and text crossing visible axis-aligned SVG rectangle borders. It does not map every arbitrary path or ellipse to a semantic frame; use image review for those and for edge/text collisions.

The report states counts. Zero detected labels is a failure, not success. It also reports unsupported non-axis-aligned rectangles and embedded image load failures. Rectangles that intentionally contain text are not an overlap by themselves; their border intersection is the relevant check. The script's bounding boxes are conservative layout bounds, not exact glyph-pixel masks.

Custom padded-frame checks should use source-to-render calibration, not a hard-coded scale such as dividing coordinates by 3. Export scale, crop border, and font substitution can change. When source labels repeat, match them by stable element IDs or calibrated position, not the first identical string.

### 3. Visual inspection and rejection

Open the actual PNG or a PDF raster. Inspect the whole composition, then the most crowded areas. Review at high zoom for line joins and at intended publication size for comprehension. Specifically inspect:

- Clear reading order and meaningful grouping.
- No clipped labels, duplicated text, literal escape sequences, or missing glyphs.
- Text not touching thick frames, icons, neighboring labels, or unrelated lines.
- Arrow shafts visible; arrowheads point to the intended objects.
- No accidental joins, ambiguous crossings, or hidden paths under filled shapes.
- Consistent type hierarchy, color roles, frame weights, and pictogram scale.
- Large empty right/bottom bands removed without collapsing semantic separation.
- Tool symbols separate from editable names; no accidental duplicated wordmarks.
- Schematic detail remains recognizable at final size and is scientifically justified.
- PNG, SVG, and PDF all show the same intended content.

Reject material failures and rerender after repair. A fixed number of passes does not guarantee quality. At least one rendered inspection is necessary; additional passes are driven by observed defects. Keep a short record of what failed and what changed.

### 4. Publication and delivery review

Check physical PDF dimensions with a PDF inspector and compare them with the brief. Ensure no extra blank pages. The bundled browser exporter preserves common SVG `foreignObject` text better than converters that ignore HTML; still inspect the final PDF because unsupported fonts and platform differences remain possible. It accepts arbitrary positive width, computes height from the SVG viewBox, and uses a white page.

Do not claim font embedding, all-vector output, or embedded Draw.io XML unless checked. A PDF with raster logos can still be useful, but its limitations should be accurately described. Crop marks, captions, and manuscript figure numbering are included only when requested.

## Stop conditions

A final figure has accurate content, a readable dominant story, no known material geometric defect, an editable source, fresh exports, and a documented physical size. If rendering is unavailable or the target size is incompatible with mandatory content, state that limitation and provide the useful work completed. Do not silently drop content or claim a screenshot was inspected when only XML was reviewed.
