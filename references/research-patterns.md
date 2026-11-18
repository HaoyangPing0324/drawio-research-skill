# Research patterns: use only when supported

These patterns document the reasoning behind the development figures. They are conditional examples, not a requirement to insert a particular FPGA toolchain, coordinator, or speculative method into every paper.

## Evaluation and verification harness

A useful story is "a candidate progressively acquires verification evidence." Put the object and check at the center of each stage; keep tools subordinate and provide one key output per stage.

| Stage | Native visual | Checks, when specified | One output | Tool signature, if applicable |
|---|---|---|---|---|
| Functional check | DUT and reference entering a comparator | Values, shapes, stream counts | Functional report | C simulation |
| HLS evaluation | Pipeline, PE array, resource blocks | Synthesis feasibility, actual II, estimated resources/clock | Schedule + RTL | Vitis HLS |
| Dataflow verification | IP blocks linked by FIFOs, handshake illustration | Interfaces, backpressure, deadlock, system progress | Integrated RTL + trace | SpinalHDL + Verilator |
| Physical implementation | Placed/routed FPGA grid | Whole-system resources, routing, timing | QoR + bitstream | Vivado |

Keep the distinction between estimated and physically confirmed resources explicit. "Estimate → Confirm" may work as a short annotation, but avoid a long bracket that interferes with the main flow.

If the manuscript includes LightningSimV2, a teal dashed branch can start from Schedule + RTL, produce Cycles / FIFO behavior for matched HLS subgraphs, and feed a coordinator. Do not imply that it validates whole-system resources or final timing. Show the precise branch source; a branch from a generic stage border can obscure which artifact it consumes.

If the method distinguishes feedback classes, keep two explicit destinations or labelled exits:

- Design feedback: functional errors, throughput bottlenecks, resource or timing issues become architecture/source tasks.
- Tool / validation faults: compiler failures, report parsing, or adapter problems become tool-path repair tasks. They should not appear to require a DUT rewrite automatically.

Tokens and development time belong in a separate run ledger if specified. They are process bookkeeping, not hardware verification outputs. Do not repeat them inside every stage.

## Challenge-to-method reasoning strips

A challenge should explain why the corresponding method is needed. A short left region can state the difficulty; the right region can demonstrate the response with meaningful objects and a causal flow. The connecting arrow represents the argument from problem to approach, not an executable data interface.

For coupled accelerator design, a rate-mismatched producer/FIFO/consumer schematic can explain why local speedup need not become system speedup. Profiles, joint compute/storage/I/O choices, source alternatives, and system evidence can illustrate workload-guided co-design when those are the actual method. Do not collapse cross-operator coupling and intra-operator exploration into one vague "optimization" box.

For delayed/imperfect feedback, an hourglass and estimate/physical-report pair can explain the problem. If supported by the manuscript, show A's backend pending while B advances provisionally, record dependencies, and use subsequent physical evidence to reassess affected decisions and restore eligibility. Restored eligibility is reconsideration, not proof of feasibility. A revision cue can point back to architecture/resource allocation without a tangled return bus.

Pessimistic estimates may exclude feasible candidates; optimistic estimates may retain infeasible candidates. Keep both directions explicit if they matter to the argument. A generic error icon alone loses this distinction.

## Richness without invention

Use source-backed objects as places for extra detail: tensor tiles in profiling, PE/FIFO/banks in co-design, code cards at source exploration, device grids at implementation, and dependency nodes beside recorded dependencies. Do not introduce unrelated databases, agents, buses, clocks, or process arrows just because an area is empty.

## Small companions

Treat a reduced companion as a separate artifact if the full figure is approved. Preserve mandatory claims, outputs, tool identities, scope qualifiers, and feedback classifications. Remove redundant captions and excess repeated mesh cells first. Document the difference. Do not overwrite the full figure or claim a compact variant is content-identical if meaningful checks were omitted.
