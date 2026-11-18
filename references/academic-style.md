# Academic style and publication size

## Extract style, do not guess it

Inspect at least a full reference figure and a crop with text, borders, arrows, and fine detail. For editable references, inspect style values, font names, line weights, fills, and page bounds. PDF appearance and Draw.io numeric values may use different scales; compare their physical appearance instead of transferring unexplained numbers.

Record a small token set: page background; primary ink; fill colors and roles; accent colors; main/internal/wire stroke hierarchy; corner treatment; title/body/caption type; arrowheads; and spacing. Learn the reference's visual grammar rather than reproducing its scientific content.

Use a white publication background unless the venue or user asks otherwise. For the circuit preset, use straight charcoal frames, muted fills, minimal nesting, and distinct but restrained accents. Avoid generic presentation-card styling: large corner radii, deep shadows, gradients, oversized padding, saturated rainbow panels, and decorative badges. Such effects are not intrinsically forbidden; they are inappropriate when they conflict with the supplied paper style.

## Circuit / architecture preset

The machine-readable starting values are in `assets/presets/circuit-academic.json`.

| Role | Starting value | Intent |
|---|---|---|
| Primary ink | `#282B30` | Text, frames, native primary flow |
| Compute fill | `#D5E4EE` | Pale blue |
| State / revision fill | `#DCEBE3` | Pale green |
| Queue / resource fill | `#F0E3C7` | Muted sand |
| Storage fill | `#E7E1EE` | Muted lavender |
| Provisional accent | `#327F75` | Teal, paired with a dashed line or label |
| Fault / reassessment accent | `#A2574C` | Muted red, paired with explicit wording |
| Background | `#FFFFFF` | White |

These role assignments are examples; do not introduce storage or faults into a figure that has neither. Use redundant cues for meaningful distinctions: text, line pattern, or shape as well as color. Check grayscale legibility. Similar fills should not be the only difference between confirmed and speculative evidence.

Typical model-space values for a compact 520-unit-wide composition:

- Main frame: 1.8–2.2 units; internal divider: 0.7–1.0 units.
- Workflow edge: 1.1–1.5 units; icon detail: 0.4–0.9 units.
- Heading: approximately 18–20 units; body: 15–17 units; supporting caption: 14–16 units.
- Typeface: Times New Roman when matching the circuit preset; use an installed, disclosed serif fallback such as Liberation Serif if needed.
- Bold headings and concise body labels suit dense schematics; avoid heavy weight in every tiny decorative detail.

These are starting ranges, not hard requirements. Small historical figures used smaller model fonts; those values are not a universal readability recommendation. Validate physical type size before copying them.

## Physical size is the actual constraint

Ask for or infer a target width from the manuscript's venue/template. A nominal 88 mm single column is a working default, not a universal conference standard. A request for a 68 mm figure is a width constraint, not an instruction to shrink everything indiscriminately.

For content width `W` in model units, final width `w` in mm, and model font size `f`:

```text
approximate physical font size (pt) = f * (w / W) * (72 / 25.4)
approximate physical stroke (pt)    = s * (w / W) * (72 / 25.4)
```

Use actual exported bounds including margins for final calibration. For example, 16 model units at 88 mm across 520 units is about 7.7 pt. The same model at 68 mm is about 5.9 pt. A higher-resolution PNG does not increase printed type size. Publisher requirements and actual readability govern; approximately 7–9 pt body text is a useful initial target when no stronger constraint exists.

If the width and content cannot coexist at a readable scale, shorten repeated text, reorganize the topology, reduce redundant motifs, or propose a panel split. Do not disguise tiny text with a large preview.

## Typography and rules

Use a controlled type hierarchy and consistent capitalization. Prefer sentence case or consistent title case; do not mix them casually. Use true line breaks rather than escaped `\n` text on the page. Keep tool branding text editable and separate from its symbol. Verify special glyphs such as multiplication, inequalities, arrows, and Greek letters in the export.

Do not assume an assigned label rectangle bounds its rendered glyphs. Font substitution, line-height, boldness, and wrapping change ink extents. Check frame clearance after half the stroke width is subtracted. A thickened frame can collide with unchanged text. In the compact preset, 2.5 model units of clear padding inside major frames and 1 unit in tiny labelled components are starting minima, not guarantees of visual comfort.

Use fewer larger meaningful figures instead of many illegible thumbnails. Fine circuit detail can be subordinate, but the object identity must remain recognizable at final size.
