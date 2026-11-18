# Layout and compaction

## Optimize the composition before the canvas

Choose the aspect ratio to match the story and intended placement. Long serial processes can use a pipeline; two challenge/method pairs often work as two reasoning strips. A central controller with many crossings may be clearer as a narrow feedback band. Do not add a large title inside the drawing if the paper caption already supplies it and the user does not require it.

Build groups around meaningful objects. A stage can contain one heading, a native schematic, a concise check caption, a secondary tool signature, and one unique artifact. Align comparable functions on common baselines. A border is useful when it indicates containment, responsibility, or a stage; it is not required around every icon and caption.

Allocate space according to content, not an arbitrary equal-width grid. Headers and output labels can share alignment without all stages having identical internal geometry. Keep enough separation to distinguish groups visually.

## Density has a semantic definition

Aim for a high ratio of useful information to total area. This is not the same as percentage of non-white pixels. A patch containing random circuit marks is visually occupied but scientifically empty. A narrow gap between two related blocks may be essential to the reading order.

Inspect blank regions by role:

| Region | Typical action |
|---|---|
| Large unused right margin | Pull the rightmost group inward and crop the canvas |
| Empty lower band in every stage | Shorten all stage frames and move following content up |
| Gap caused by repeated long captions | Shorten captions before shifting geometry |
| Empty region inside an oversized box | Fit the box to content; realign adjacent connectors |
| Necessary connector corridor | Preserve it or reroute; do not fill with unrelated motifs |
| Gap between independent panels | Preserve sufficient stroke separation |

Look at the whole composition after each local compression. Moving a box can create a new imbalance elsewhere. Crop exported bounds only after objects and routes have reached their final positions.

## A reliable compaction order

1. Remove redundant prose and duplicate artifacts, while preserving mandatory distinctions.
2. Remove unsupported ornaments and duplicated inner borders.
3. Tighten heading, schematic, caption, and output bands.
4. Resize containers to fit actual rendered content with safe padding.
5. Move complete semantic groups closer; move their wires and child objects with them.
6. Shorten and simplify connector routes while retaining visible shafts.
7. Rebalance unequal columns or convert a wide chain to compact rows.
8. Update page dimensions and export bounds.
9. Recheck physical text size, all contacts, and reading order.

Never only reduce `pageWidth`: it may merely change pagination or clip content. Never anisotropically scale the whole drawing; circles, typography, arrowheads, and logos will distort. Uniform scaling is an export operation, not a solution to poor density.

## Width-first compression

When the user says the figure is too wide, measure the current occupied width and identify the largest recoverable horizontal bands. Shorten repeated stage names, pack pictogram subgroups, use concise captions, and reflow long revision outcomes within a narrow final column. Preserve top-to-bottom height when possible, but do not promise unchanged height if that would force unreadable text.

A useful worked target from the development workflow was 680 to 520 model units, a 23.5% width reduction through repacking. This is an example outcome, not a target all diagrams must meet. At a fixed font scale, the physical width can reduce proportionally. At fixed publication width, the narrower model makes the text physically larger. Report which interpretation you used.

## Height-first compression

Combine repeated headers, avoid nested subtitle bands, place short tool signatures alongside an icon, use one footer strip for bookkeeping, and move side explanations into a concise caption if authorized. A two-strip challenge/method composition may use less height than four standalone cards. Reducing height should not create an excessively wide panorama.

## Distances and explicit exceptions

Set a local spacing policy rather than importing generic presentation gaps. For dense schematics, 6–10 units between main frames and 12–18 units of unobstructed main-flow segment are useful starting points at the circuit preset scale. Tiny pin wires can be shorter. These distances are only appropriate if arrowheads, stroke widths, and physical output size still work.

The lower bound is visibility, not "no mathematical overlap." Two strokes that almost touch can look merged after rasterization. Labels that pass an exact rectangle test can still feel crowded. Inspect the export and provide more space when necessary.

## Preserve accepted work

A request to compress one figure does not authorize changes to its approved siblings. Snapshot the current version and record hashes of protected files. Keep the generator consistent with the final artifact; avoid editing generated XML without updating the generator if it remains the intended source of regeneration. Record deliberate omissions in a small variant. Do not silently remove scientific content to satisfy a size request.
