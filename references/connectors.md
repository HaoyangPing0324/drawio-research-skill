# Connector engineering

## Distinguish flows from icon detail

A workflow edge asserts a scientific relationship. An internal wire draws a circuit motif. Classify them separately in the model or validation configuration. Main-flow visibility checks should not reject a 3-unit chip pin, and tiny-wire exceptions must not excuse a 3-unit inter-stage arrow.

Use a dominant reading direction for the primary flow. Use color plus line pattern or wording to distinguish a secondary estimate/provisional branch. Keep feedback in a reserved corridor or labelled band. Do not attach a global return line to every tiny check when a clearly defined enclosing stage can represent the source.

## Endpoint and route rules

- Attach endpoints to semantic vertices or explicit native port/terminal vertices. Every referenced ID must exist.
- Use sensible side ports. A line should not terminate in text, inside an unrelated icon, or at an arbitrary point near its target.
- Prefer straight adjacent-stage links. Use orthogonal bends when needed. Do not bend solely to create decorative motion.
- Order fan-out ports to match the order of their destinations. Use one clear split where the source truly branches.
- Keep primary workflow paths free of crossings. If a necessary crossing remains, distinguish crossing from junction and inspect it at publication scale.
- Avoid paths that run along a frame border, through an unrelated box, or under a label.
- Explicit junctions are useful when lines meet; proximity alone is not a connection.

Native zero-size terminals can support precise schematic placement, but they must move with their owning semantic groups. A terminal with an attached edge does not automatically stay attached to a nearby icon when that icon moves. Update both together and verify the final endpoint visually.

## Visible shaft, not just geometric length

For each inter-component edge, check the first and last segments and any segment interrupted by a label. A 12-unit segment with a 10-unit arrowhead may have almost no visible shaft. A white label background can hide an otherwise long line. Count only the unobstructed visible run when judging readability.

At the default compact scale, begin with 12–18 model units per main-flow segment and modest 4–5-unit arrowheads. Increase spacing if the arrow looks like a detached triangle. Do not universally apply generic 40-unit lead lengths from presentation diagrams to small publication schematics.

An edge label belongs to its edge. Use native edge-label geometry or explicit ownership metadata; keep it beside a sufficiently long horizontal/vertical run. Label only when the relationship would otherwise be ambiguous. Repeating "data" on every obvious pipeline arrow can reduce clarity.

## Editing order

Place objects, align their natural connection ports, route the shortest clear paths, then place any edge labels. If a route looks wrong, ask what each bend avoids. Move groups before adding detours. Recheck routes after any change to font size, box size, icon scale, or group position.

When moving a parent, account for parent-relative child coordinates. When moving a set of sibling cells, include explicit terminals and waypoint arrays. Mixed coordinate systems often leave arrows behind even though all visible boxes moved correctly.

## Audit scope

Check duplicate IDs, missing endpoints, parent cycles, route orthogonality, minimum segment lengths, workflow crossings, and relations to label/frame bounds. Automated routing audits must state which edge classes they inspected. The bundled geometry audit checks explicitly routed workflow edges; it does not reconstruct renderer-computed perimeter paths. A successful audit with zero workflow edges is missing coverage, not proof of correct routing.

The final visual check remains decisive for arrowhead scale, z-order, merged strokes, and lines hidden by filled shapes. Do not deliver a diagram based solely on XML coordinates.
