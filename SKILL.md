---
name: drawio-research-skill
description: Creates and refines editable Draw.io research figures using source-grounded content, reference-matched academic styling, compact layouts, meaningful schematic details, and export-based visual review. Use when creating or improving paper architecture, method, challenge, workflow, or evaluation diagrams in .drawio format; not for measured data plots or raster artwork.
---

# Draw.io Research Skill

Produce an editable research figure that communicates its main relationship at a glance and remains readable at its intended publication size. A successful export is not evidence of a successful figure.

## Essential contract

1. Follow the user's current content, scope, language, target size, and approved visual decisions. Read applicable project instructions such as `AGENTS.md` and `docs/diagramming.md`. This skill supplies defaults, not authority to override the user.
2. **Use English for figure labels unless explicitly instructed otherwise**, even when the conversation or source notes use another language. Preserve exact scientific names and meaningful mathematical notation.
3. Ground every claim, dependency, output, and distinction in supplied sources. Do not invent measurements, capabilities, technologies, or success states to fill a layout.
4. Preserve `.drawio` as the editable source of truth. Keep approved sibling figures unchanged unless the task includes them. Back up before a substantial redesign.
5. Use native editable shapes, lines, and text for schematic content. A bitmap of an entire figure is not an editable deliverable. Separate tool symbols from editable tool-name labels.
6. Optimize information density, not decoration count. A small element needs an identifiable semantic role. Whitespace that protects legibility is necessary space.
7. Keep text away from frame strokes, icons, other text, and unrelated lines. Preserve visible arrow shafts and unambiguous endpoints. Verify the actual export, not just model rectangles.
8. Do not finish an edited figure without exporting and inspecting it when rendering is available. Fix observed defects, rerender, and reinspect. If rendering is unavailable, clearly deliver an unreviewed source rather than claiming publication readiness.

## Read only the references needed for the task

| Task | Reference |
|---|---|
| Establish content, sources, and scope | [Content and semantics](references/content-and-semantics.md) |
| Match a paper's colors, linework, and typography | [Academic style](references/academic-style.md) |
| Reduce width/height or increase density | [Layout and compaction](references/layout-and-compaction.md) |
| Route arrows or repair tiny/ambiguous connections | [Connectors](references/connectors.md) |
| Add circuits, hardware motifs, or tool symbols | [Semantic iconography](references/semantic-iconography.md) |
| Build or modify a native model | [Draw.io engineering](references/drawio-engineering.md) |
| Render, measure, and reject defective drafts | [Export and review](references/export-and-review.md) |
| Diagram implementation/evaluation or challenge/method relations | [Research patterns](references/research-patterns.md) |
| Interpret recurring user feedback | [Revision playbook](references/revision-playbook.md) |

## Workflow

### 1. Establish the figure contract

Read the active source and existing figure. Inspect supplied PDF/image references visually; inspect editable reference models for exact styles when available. Record the message, evidence, required objects/relations, target dimensions, language, style tokens, and protected files. Use [the brief template](assets/templates/figure-brief.md). Resolve routine choices yourself; ask only when missing information affects factual correctness or a material constraint.

### 2. Design the reading order

Write the figure's one-sentence message. Select a topology that expresses it: pipeline, challenge-to-method strips, architecture with limited feedback, or structured comparison. Place meaningful object groups before arrows. Separate required scientific content from optional explanatory details. Do not mechanically preserve an unsuitable inherited layout when the user allows redesign.

### 3. Build in native primitives

Use an XML-aware generator or a capable Draw.io editing tool. Prefer explicit placement for compact publication compositions; automatic layout can supply an initial topology but does not replace manual composition. Use semantic IDs and reusable style tokens. Copy embedded assets file-to-file, without emitting large payloads through model output. See [Draw.io engineering](references/drawio-engineering.md) for model invariants and portable tooling.

### 4. Compact while preserving meaning

Shorten repeated wording, resize containers to their contents, move connected groups together, reroute edges, then crop the page. Preserve semantic distinctions and physical text legibility. Repack a wide figure instead of merely scaling it down. Any new pictogram must explain an existing concept. Use the [circuit preset](assets/presets/circuit-academic.json) as a starting point only.

### 5. Export, inspect, and revise

Run structural checks, render PNG/SVG, inspect the whole image and dense crops, and review at the intended physical size. Check text/text overlaps, text/frame contact, text/icon separation, arrow visibility, unused bands, content accuracy, and exported text completeness. The bundled scripts cover a documented subset; manual visual and semantic review remain mandatory. Read [export and review](references/export-and-review.md) for commands and limitations.

Reject a draft with a factual mismatch, missing label, clipped text, touching frame, ambiguous edge, stale preview, or unreadable publication-scale content. Fix the cause, not the audit threshold. Repeat until material defects are resolved or explain a concrete remaining blocker.

### 6. Deliver a reproducible result

Provide the `.drawio`, a fresh PNG preview, and requested vector/PDF exports. Include final dimensions, material simplifications, validation performed, and unresolved limitations. Save a brief review record using [the review template](assets/templates/review-report.md). Do not claim every generic lint warning is fixed when deliberate circuit wires remain outside its assumptions. Do not publish or message others without applicable authorization.

## Scope boundaries

The skill supports research schematics, not empirical chart generation or invented architecture. Example motifs and evaluation patterns are conditional vocabulary, not facts to insert into unrelated papers. Third-party symbols retain their own terms. Source attribution is documented in [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md).
