# Acknowledgments and provenance

## Primary experience

This skill was developed from iterative research-figure editing: understanding an active manuscript, matching paper visuals, replacing text-heavy tool lists with meaningful schematic objects, separating symbols from labels, reducing width and height, rejecting arbitrary filler, and fixing actual text/frame/arrow defects after export.

The instructions and portable helper scripts in this repository were written for this project. The original project manuscript, supplied style PDFs, unpublished project figures, and local renderer checkout are not distributed. The separately requested DeepSeek report overview is original artwork with its own source mapping and run provenance. Domain-specific examples are presented as conditional patterns, not general claims about every project.

## Referenced diagram skills

| Source | Provenance examined | Useful ideas | Reuse boundary |
|---|---|---|---|
| [JGraph drawio-mcp](https://github.com/jgraph/drawio-mcp), Draw.io skill | Local provenance records upstream commit `639186a5cdaea5a0d47215f5f404ac7b76ccf634`; the collected skill had local modifications | Native XML, renderer capability discovery, editable artifacts, diagram export mechanics | Consulted as implementation guidance; no upstream skill text or code is vendored. The supplied upstream license was Apache-2.0, copyright 2025 JGraph Ltd. |
| [BRBussy draw-io-cli](https://github.com/BRBussy/draw-io-cli), drawio-diagrams skill and style guide | Local provenance records upstream commit `1f95a87464d7d78365137561efa3dcedc4d4117d`; the collected skill had local modifications | Source/preview pairing, geometry inspection, palette consistency, safe asset handling, scoped edits, and rendered inspection | Credited as an influence; its skill text, scripts, and style guide are not copied or redistributed here. The CLI is an optional external tool, not a bundled dependency. |

These commit identifiers identify the provenance records inspected, not a claim that the locally modified files are byte-identical to upstream. The records were collected on 2026-11-14. A future contributor copying actual upstream material must verify the applicable license for that material and preserve required notices; acknowledgment alone is not permission.

## Defaults deliberately not inherited

- Always choosing Mermaid or auto-layout is unsuitable for precise compact research compositions.
- Deleting native `.drawio` sources after image export conflicts with an editable research deliverable.
- Matching label language to the conversation conflicts with this project's English-by-default policy.
- Universal large arrow leads and icon clearances can conflict with single-column layouts; calibrated compact distances are used instead.
- Dotted actor boxes, rounded cards, and mandatory icon placement are not universally appropriate for paper figures.
- Machine-specific runtime paths and environment hooks are not portable skill dependencies.
- Generic lint success does not prove content accuracy or publication-scale readability.

The replacement guidance reflects the project's observed needs and is independently written. The upstream tools and authors are not responsible for these changes.

## README presentation references

- [Excalidraw README](https://github.com/excalidraw/excalidraw): immediate project identity, clear navigation, concise feature discovery, and a quick start.
- [Mermaid README](https://github.com/mermaid-js/mermaid): an accessible entrypoint to deeper documentation and an explanation of the project's scope.

Only general presentation conventions informed this README. No logos, screenshots, badges implying project status, or original prose were copied.

## Demonstration report

The explicitly requested [DeepSeek-V4.1-Flash overview](examples/deepseek-v4.1-flash/README.md) summarizes the official DeepSeek-AI technical report. It uses original native shapes; it does not copy the report artwork or redistribute the PDF. The example records the report URL, file hash, reading scope, and generation process.

## Asset policy

No external paper images or official software logos are included. Future additions must record the source, author where known, applicable license or permission, retrieval date, and modifications. Trademarks remain with their respective owners. This project's Apache license cannot relicense third-party assets.
