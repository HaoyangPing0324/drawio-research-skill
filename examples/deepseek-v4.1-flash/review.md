# Demonstration review

## Outcome

The original overview is delivered as native Draw.io with PNG, SVG, and a one-page PDF. Requested PDF width: 88 mm; measured page: approximately 87.88 × 101.26 mm (browser page-size rounding). The PDF uses Liberation Serif Bold, the available serif fallback for Times New Roman.

## Content review

The full 51-page official report was read, including its tables, bibliography, and appendices. Architecture diagrams on pages 7, 10, and 11 were also inspected visually. The overview selects the architecture/cache/training story rather than reproducing all tables. Every numerical callout is mapped to the report in the accompanying README. No paper artwork, official logo, or fabricated benchmark result was included.

Important distinctions retained: backbone versus Engram parameters; prefill versus decode activation; independent CSA2 modes; global HBM versus persistent SSD/host cache; approximate replay; report-specific evaluation settings; and unresolved robustness boundaries. The final attention/circuit motifs are schematic, not literal layer or expert counts.

## Internal revisions within the single task

1. Initial native composition: three panels with 139 cells and 49 labels. The first SVG review found no text overlap or rectangle-border contact.
2. Semantic clarification: made HBM and SSD/host placement explicit in the cache callouts; regenerated the exports.
3. Connector refinement: lengthened the image/text input route segments and added both to explicit workflow coverage; regenerated and repeated checks.

No human layout editing or intermediate design feedback was used after scope clarification. These internal passes are disclosed; the example is not presented as a single-render result or an independent fresh-context evaluation.

## Checks performed

- Structural audit: unique IDs, attached endpoints, valid parents and geometry; six explicitly routed workflow edges, minimum segment length 12 units, no strict crossings; no skipped routes in that class.
- Rendered review: 49 labels, 60 axis-aligned rectangle borders, no text/text overlaps, no text/rectangle border contacts. Zero embedded images is expected because all art is native; the icon-load check therefore has no image coverage in this example.
- Full PNG visually inspected for layout, arrows, typography, semantic grouping, and meaningful detail.
- Final PDF raster visually inspected; page count, dimensions, font name, and key numeric text verified.
- Exported source/PNG pairing checked with the available external Draw.io CLI; artifact hashes recorded separately.

## Limits

The SVG check does not prove arbitrary path clearance or scientific correctness; those were reviewed separately. Small supporting captions need careful treatment if the figure is reduced below its intended width. The demonstration summarizes reported findings and does not reproduce their experiments. Browser font fallback and page-size rounding are disclosed above.
