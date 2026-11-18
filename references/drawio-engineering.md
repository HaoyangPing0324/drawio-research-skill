# Native Draw.io engineering

## Source and tool selection

Preserve a native `.drawio` file regardless of preview format. Prefer uncompressed XML for new programmatically generated figures because it is inspectable and diffable. Existing compressed pages should be decoded with a real parser or a capable editor; do not treat base64 as XML. Inspect every relevant page and any `object`/`UserObject` wrappers before editing.

Use a renderer already available in the environment. Draw.io Desktop, a verified browser-based Draw.io exporter, and suitable editor integrations have different commands. Inspect the installed tool's help; do not assume a third-party CLI uses desktop flags or that every version supports Mermaid conversion. Authoring XML itself requires no network.

For precise publication work, native XML placement is usually appropriate. Auto-layout is useful for topology discovery but can destroy a carefully packed composition. Never run a global layout pass on an approved diagram merely to adjust one caption.

## Model invariants

A page normally contains `mxGraphModel/root`, root cell `0`, and default layer `1`. Vertices have unique descriptive IDs, parent references, a style, and `mxGeometry`. Edges have source/target IDs and relative edge geometry; explicit waypoints live in an `Array` named `points`. Use names such as `profile-input` rather than builtin-like bare identifiers.

Keep style serialization explicit: fill, stroke, width, font family, font size, font color, alignment, wrapping, and arrow semantics. Use an XML serializer to escape ampersands, less-than signs, quotes, and line breaks. Plain labels are easier to transfer than arbitrary HTML. Nevertheless, some exporters use SVG `foreignObject` even for plain labels; check the actual output.

Group coordinate systems require care. Child coordinates are normally relative to the parent; report coordinates may be absolute. Do not add a parent's offset twice. Edge-label relative geometry is a special case and must not be interpreted as an ordinary vertex rectangle. Preserve grouping, ports, z-order, and unrelated metadata during edits.

Optional `drsRole` metadata used by this repository:

- `frame`: enclosing panel rectangle; used for frame-clearance review.
- `label`: free-standing text.
- `component`: a labelled or unlabelled schematic object.
- `detail`: subordinate circuit marks.
- `port`: explicit connection terminal.
- `workflow`: main relation edge with explicit route.
- `wire`: internal circuit wiring, excluded from workflow length checks.

These attributes are helper conventions, not a Draw.io requirement. Existing files do not need to be rebuilt to adopt them. Unsupported model structures must be reported as skipped coverage rather than silently treated as valid.

## File operations and reproducibility

Read and write existing diagram bytes through local scripts or editor tools. Do not echo huge embedded image payloads into conversation output. Use XML-aware changes instead of regex rewrites of whole documents. A small generator may write new cells directly; the restriction is against needlessly recopying large existing assets through the model.

Before major edits, keep a baseline in a revision directory. Record protected-file hashes and check them at delivery. If another editor may be open, recheck the source hash before overwriting it and before exporting. A changed source invalidates previous previews and measurements.

Keep a small parameterized builder for repeated figures: style tokens, label content, layout dimensions, circuit helpers, and connector routes should be separate concerns. Prefer one authoritative layout over a chain of accumulated post-hoc transformations. Regenerate into a temporary file when comparing against manual edits.

## Portable tooling

Do not embed a developer's home directory, browser cache, font path, or repository path into reusable scripts. Accept CLI arguments or documented environment variables. Python standard-library helpers can inspect and generate XML. Browser-based SVG inspection/PDF output uses the optional local Playwright dependency; this repository does not bundle a browser, fonts, Draw.io, or a third-party renderer.

Use local project dependencies when setup is required. Detect missing capabilities and report the exact step that cannot run. Do not substitute a screenshot of the entire figure for editable XML. Do not claim a fake `.drawio` extension makes an SVG or PNG an editable source.

## Exports and source pairing

A PNG preview is useful in GitHub because it has stable colors and does not depend on SVG HTML support. SVG is useful for inspection and vector export. PDF is useful for publication, but must be checked for missing text, rasterization, font substitution, and physical size.

Where an exporter embeds the Draw.io model, verify that its IDs, values, styles, connections, geometry, and waypoints match the source; metadata serialization can legitimately differ. Otherwise record source and output hashes in a manifest and clearly describe this as freshness bookkeeping, not embedded-model equivalence. Never delete the native source after producing a preview.

## Source-backed implementation example

The [DeepSeek report demonstration](../examples/deepseek-v4.1-flash/README.md) includes a native builder, source mapping, exports, and an honest single-task run record. Inspect its builder for small XML helper patterns, not as a fixed topology or a source of facts for unrelated figures.
