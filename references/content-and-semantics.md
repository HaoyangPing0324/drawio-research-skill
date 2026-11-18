# Content and semantics

## Establish authority before composition

Use the current user specification and the active manuscript, not whichever file is easiest to read. In a LaTeX project, inspect the root file's includes; old drafts with similar names may be inactive. When several archives exist, identify the latest intended version through the user's instructions and available metadata. A file name alone is not proof of scientific authority.

Distinguish three sources of information:

- **Content authority:** the manuscript, supplied table, approved specification, or explicitly stated correction.
- **Visual authority:** reference figures, an existing approved diagram, or the user's requested style.
- **Implementation guidance:** this skill, renderer documentation, helper scripts, and project conventions.

A visual reference can justify a palette or line weight, not a new algorithm, benchmark, hardware component, or evaluation result. Existing diagrams can also contain outdated wording. Resolve conflicts explicitly in the brief. Do not silently blend incompatible versions.

## Build a compact content inventory

For each required concept record: exact source location; concise English label; native visual representation; required relation; evidence status; and whether it may be abbreviated. Record important exclusions as well. For example, a quick estimate limited to one subgraph must not look like whole-system physical validation.

Classify content into:

1. Essential scientific claims and relationships: must survive every size reduction.
2. Supporting explanations: may become concise captions or recognizable motifs.
3. Redundant wording: can be removed when the meaning remains explicit.
4. Unsupported decoration: must not be introduced.

A tool name is usually secondary to the object or check it performs. A component label, its pictogram, and its output should tell one consistent story.

## Meaning-preserving abbreviation

Prefer a short noun phrase plus a graphic over a paragraph in a box. Keep the same terms across panels and captions. Expand unfamiliar abbreviations in an external figure caption or legend when needed. Do not abbreviate a word merely because it can be shortened; evaluate the audience.

Examples:

| Verbose expression | Possible compact rendering | What must remain clear |
|---|---|---|
| A report containing functional comparison results | Functional report | It is an output, not a separate checker |
| Estimated latency and hardware resource use | Latency / resources | Whether they are estimates or measurements |
| Revision of architecture and source implementation | Revise architecture / source | Both levels are in scope |
| Candidate eligible for reconsideration | Restore eligibility | This does not mean accepted or validated |

Never remove a qualifier that changes certainty or scope. "May prune feasible candidates" is not equivalent to "prunes feasible candidates." "Estimate" is not equivalent to "confirm." "Provisional" must not disappear just because a caption is long.

## One-glance comprehension

Before drawing, finish the sentence: "This figure explains how _____ leads to _____ through _____." If that sentence requires several unrelated stories, use clear panels or split the figure if authorized.

After drawing, read it in the intended order without consulting the paper. Can a reader identify the inputs, transformations, results, and feedback destinations? Does each color or line pattern have a stable meaning? Are feedback objects identified? Is an apparent parallel branch actually parallel in the source?

Do not use an unlabeled decorative diamond when there is no decision or trade-off. Do not imply an execution sequence by putting unrelated concepts on a numbered pipeline. Connecting two icons can assert causality; a connection requires evidence just as a label does.

## Scientific status and illustrative details

A representative PE array, tensor tile, FIFO slots, or FPGA site grid may visualize a named concept without asserting an exact count. Record it as schematic; do not attach counts or capacities unless supplied. Timing waveforms must be illustrative and labelled accordingly unless based on actual traces. Avoid fabricated timing values, utilization bars, pass rates, speedups, benchmark logos, or measurements.

When adapting published work, do not distribute its full PDF, proprietary symbols, or copyrighted figures merely because it was supplied as a visual reference. A new palette and original schematic can express the requested style without copying a third-party figure's artwork.
