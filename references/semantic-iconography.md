# Semantic iconography

## Each motif must earn its space

For every small object, answer: what scientific object, operation, state, or artifact does this represent? Which adjacent label or enclosing component identifies it? Would removing it remove useful information? If the only answer is "it fills a hole," remove it and compress the layout instead.

Use a coherent native schematic vocabulary:

| Concept | Editable primitive composition | Guardrail |
|---|---|---|
| Tensor / tile | Small row-column grid with restrained highlighting | Counts are illustrative unless specified |
| Processing element array | Chip outline, regular PE cells, short pins | Do not invent exact parallelism |
| FIFO / buffering | Adjacent slots with a clear connected path | Occupancy colors must not imply measured behavior |
| Banked memory | Parallel narrow banks with slot marks | Labels or context identify memory |
| Pipeline | Short sequence of stage rectangles | Do not imply measured latency |
| Comparator | Two labelled input paths into a comparison node | Reference and DUT roles remain distinct |
| Source alternatives | Stacked code-like cards or editable short code marks | Do not insert fabricated algorithm code |
| Schedule | Aligned stage/slot structure | Exact cycles require evidence |
| Integrated FPGA | Site grid with sparse routing paths | Schematic placement is not a real implementation result |
| Time / backend wait | Small clock or hourglass | Distinguish duration from deadline or cycle count |
| Report / artifact | Compact document shape with several text rules | Use one per actual key output |
| Dependency tracking | Small connected nodes | Keep "provisional" explicit when applicable |
| Resource reassignment | Branching allocation motif | Do not imply unsupported quantities |
| Error / reconsideration | Small symbol beside explicit text | A red cross is not a substitute for fault classification |

Native schematic components are preferable to generic clip art for research architecture diagrams. Reuse the same concept-to-icon mapping throughout a figure set. Avoid sticker-like illustrations, pictorial gradients, and a mixture of incompatible line weights.

## Tool logos and names

Make the verified tool symbol one image cell and the name a separate editable text cell. Align by visible symbol ink rather than the asset's padded bounding box. Use the same apparent height and baseline across a tool row; logos with different aspect ratios need different widths.

If the official asset is a wordmark only, do not pretend a cropped fragment is an official standalone symbol. Look for an authorized symbol variant. If none exists, use a clearly generic role icon beside the accurate tool name, or retain the intact official wordmark without duplicating its name. Explain any deviation when it matters to the user's request.

For C simulation, a compact source-file plus run marker or a clearly labelled comparison schematic can communicate the function better than an arbitrary letter "C" in a circle. The choice should match the figure's focus. Do not label custom artwork as an official product logo.

## Asset handling

Prefer official sources and SVG or sufficiently high-resolution assets. Record the source URL, retrieval date, applicable terms, and modifications in an [asset manifest](../assets/templates/asset-manifest.md). Availability on the web is not a reuse license. Do not copy a reference paper's decorative image into a distributable skill without permission.

Embed approved assets in the diagram when offline portability matters. Keep original assets and attribution alongside the source where their terms allow it. External image URLs can break later. Limit embedded bitmap dimensions to an appropriate resolution instead of inflating the XML with oversized files.

Inspect each asset before and after export: unwanted background, blurred detail, disproportionate padding, cut-off edges, dark-mode color inversion, or duplicate wordmarks. Keep icon and text ink separated even when their cell rectangles do not overlap.

## Avoid false scientific precision

A rich figure does not require dense numerical detail. More PE cells, waveform transitions, arrows, or routing tracks are not automatically more informative. Use enough detail to recognize the object and explain its role, then stop. Do not decorate generic diagrams with FPGA motifs when the subject is not hardware.
