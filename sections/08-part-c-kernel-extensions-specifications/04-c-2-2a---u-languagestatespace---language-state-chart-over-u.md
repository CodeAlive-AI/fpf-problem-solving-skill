## C.2.2a - `U.LanguageStateSpace` - Language-state chart over `U.CharacteristicSpace`

> **Type:** Architectural (A)
> **Status:** Draft
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state space.

**Builds on.**
`A.19`, `E.10`, `F.18`.

**Used by.**
`C.2.LS`, `C.2.3`, `C.2.4`, `C.2.5`, `C.2.6`, `C.2.7`, `A.16.0`, `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, `B.5.2.0`, `F.9.1`, `A.6.P`, `A.6.Q`, `A.6.A`.

### C.2.2a:1 - Problem frame
In engineering, inquiry, operator, and management practice, teams often need to say where a governed `U.Episteme` publication currently stands before it has reached a late endpoint owner. That governed publication may later appear through several cue-bearing, route-bearing, or endpoint-bound publication forms, but the chart claim remains about the governed `U.Episteme` publication rather than about a local alias or a carrier lane.

Cue packs, routed cue sets, abductive prompts, typed route-bounded projection publications, partial normal forms, and endpoint-bound records are not rival occupants of the space. They are publication forms through which a current position claim is made visible. MVPK faces may render those forms, but faces are not themselves the forms. By contrast, a service disturbance, a model-vs-observation discrepancy, a bodily tension, a telemetry trace, a model output, or a carrier document may trigger, witness, or carry that episteme, but none of those is itself a coordinate in the space.

Practitioners, including engineers, operators, researchers, managers, and engineer-managers, still have to decide where such an episteme currently stands, which thresholds matter next, which publication form is lawful, and what must not yet be claimed. If this domain is described only with folk labels such as `raw`, `early`, `settled`, or `ready`, the real geometry disappears.

### C.2.2a:2 - Problem
Without an explicit language-state chart:

1. teams collapse several facets into one maturity story;
2. `F` is silently misused as a surrogate for articulation, closure, anchoring, and representation factors;
3. thresholds are published as vague readiness statements instead of explicit facet conditions;
4. source phenomena, governed epistemes, publication forms, publication faces, and carriers are conflated;
5. bridge and endpoint work inherit under-described upstream states.

### C.2.2a:3 - Forces
| Force | Tension |
| --- | --- |
| **Multi-facet fidelity vs readable publication** | The chart must preserve several independent facets without becoming unreadable. |
| **Stable basis vs local thresholds** | Basis slots should stay stable across contexts, while thresholds remain context-local. |
| **Position semantics vs publication semantics** | A position claim is not identical to the source phenomenon, publication form, or carrier through which it is currently expressed. |
| **Comparability vs non-collapse** | Teams need to compare positions, but not by flattening them into one pseudo-scale. |
| **Bridge reuse vs local authority** | Cross-context work benefits from a stable upstream chart, yet each context keeps local threshold authority. |

### C.2.2a:4 - Solution
`U.LanguageStateSpace` is the cluster-local name for the declared language-state chart over `U.CharacteristicSpace` as disciplined by `A.19`.

It is not a second kernel state-space apparatus beside `A.19`. It is the particular declared `U.CharacteristicSpace` whose basis slots are the language-state facets used in this cluster.

#### C.2.2a:4.1 - Core role
`U.LanguageStateSpace` gives FPF one explicit home for answering five questions:

- which basis slots define where the governed episteme stands;
- what a position claim in that chart means;
- which thresholds are locally declared over those slots;
- what comparisons are lawful without cross-facet collapse;
- and how the same position claim stays distinct from the publication form currently expressing it.

#### C.2.2a:4.2 - Position reading under `A.19`
A language-state position is a partial, slot-explicit coordinate claim in the declared language-state `U.CharacteristicSpace`.

Each basis slot publishes a `ValueSet(slot)`, interval, or other admissible set-valued claim. Early seam publications may leave some slots unknown or wide, but that uncertainty must be declared rather than hidden inside one stage word.

`position` language is therefore lawful here only as shorthand for such slot-explicit `A.19` coordinate claims. It does **not** authorize a rival lifecycle or feature-vector story.

#### C.2.2a:4.3 - Facet basis
The language-state chart is coordinated by explicit facet owners rather than by an informal master ladder. In the current cluster the basis is formed by:

- `C.2.3` for `F`;
- `C.2.4` for articulation explicitness;
- `C.2.5` for language-state closure degree;
- `C.2.6` for language-state anchoring mode;
- `C.2.7` for the language-state representation-factor bundle.

`C.2.2a` states that these basis slots together define the chart. It does **not** own the internal scale semantics of the individual facets.

#### C.2.2a:4.4 - Ontological role lanes
Within this cluster, keep five roles distinct:

- **occupant** - the governed `U.Episteme` publication whose current position is being claimed;
- **grounds / witnesses** - disturbances, discrepancies, traces, model outputs, bodily tensions, exemplars, or contrasts that justify the current reading;
- **publication forms** - cue packs, routed cue sets, prompt forms, typed route-bounded projection publications, partial normal forms, and later endpoint-bound records through which the episteme is published;
- **publication faces** - the existing MVPK faces on which those publication forms are rendered when face typing matters;
- **carriers** - documents, console notes, cards, trace files, or model artefacts that hold or render a publication.

`U.LanguageStateSpace` owns only the coordinate reading of the position claim. It does not collapse that claim into the grounds, publication form, publication face, or carrier.

#### C.2.2a:4.5 - Position publication rule
A published position claim in `U.LanguageStateSpace` should normally make at least the following explicit:

- the occupant whose position is being described;
- the relevant slot values, `ValueSet` claims, or intervals;
- the current publication form and, when it matters, the MVPK face carrying it;
- the load-bearing grounds, witnesses, or carriers that explain those values;
- any local threshold declarations if the position is being used for a routing or gate decision;
- any note that distinguishes source anchoring from current publication-face anchoring.

A position claim may be partial when some slots are intentionally unknown, but the unknowns should be declared rather than hidden under a broad readiness label.

#### C.2.2a:4.6 - Non-substitution of `F`
`F` remains one basis slot in the chart, not the whole chart.

A conforming account shall not infer:

- closure from formality alone;
- anchoring from surface format alone;
- representation factors from articulation alone;
- or routing legality from a lone `F` statement.

Where operationally meaningful thresholds exist, they must publish on the relevant slots rather than being disguised as informal `F` sublevels.

#### C.2.2a:4.7 - Position versus publication form
A position claim in `U.LanguageStateSpace` is not the same thing as:

- the underlying governed `U.Episteme`,
- the source disturbance, discrepancy, or witness,
- the current publication form,
- the MVPK face that renders that publication,
- the carrier that stores or displays it,
- or the endpoint-owned record that may later result from it.

Those roles are coupled but distinct. `U.LanguageStateSpace` keeps the position claim readable without collapsing it into any one bearer lane.

#### C.2.2a:4.8 - Threshold publication discipline
If a threshold is used to justify a move, a handoff, or an endpoint entry, that threshold shall be stated on explicit basis slots in the chart. Statements such as `this is now ready`, `this has matured`, or `this is still too early` are non-conformant when they substitute for undeclared slot conditions.

#### C.2.2a:4.9 - Comparison and bridge note
Comparisons inside one context may use the shared chart and local thresholds. Comparisons across contexts require explicit bridge discipline. Label similarity or stage-language similarity does not establish sameness of charts, positions, or thresholds.

`C.2.2a` therefore supports bridge work, but does not grant cross-context identity by itself.

### C.2.2a:5 - Archetypal Grounding
**Tell.** One note can be strongly operator-loop anchored yet still weakly closed. Another can be document-mediated and symbol-heavy while still open on route choice. Both are positions in one language-state chart, but not on one maturity ladder.

**Show (System).** A service disturbance is a system-side phenomenon. The governed occupant is the alerting `U.Episteme` published from that disturbance; its position claim may be moderately formal, weakly closed, strongly operator-loop anchored, and mixed in representation because terse codes and natural-language hints coexist.

**Show (Episteme).** A model-vs-observation discrepancy is a witness-level tension, not the occupant itself. Once preserved as a cue pack, the resulting governed `U.Episteme` may be low in articulation, low in closure, strongly trace-anchored, and only partly symbolic even when later written into prose.

### C.2.2a:6 - Bias-Annotation
The pattern deliberately biases authors toward decomposable coordinate claims and away from folk stage vocabularies. That costs some brevity, but it prevents collapse of genuinely different state dimensions into one adjective.

### C.2.2a:7 - Conformance Checklist
- `CC-C.2.2a-1` `U.LanguageStateSpace` **SHALL** be treated as the declared language-state chart over `U.CharacteristicSpace`, not as a rival kernel space and not as a disguised `F` ladder.
- `CC-C.2.2a-2` Published positions **SHALL** cite explicit facet owners when those positions matter for movement, routing, or endpoint entry.
- `CC-C.2.2a-3` Position claims **SHALL** use slot-explicit values, `ValueSet` claims, or intervals; uncertainty **SHALL NOT** be hidden inside stage words such as `ready`, `early`, or `mature`.
- `CC-C.2.2a-4` A position claim in the chart **MUST NOT** be conflated with the current ground, witness, publication form, publication face, or carrier.
- `CC-C.2.2a-5` Cross-context comparison of positions or threshold talk **SHALL** go through bridge discipline rather than label similarity.

### C.2.2a:8 - Common Anti-Patterns and How to Avoid Them
- **Maturity monism.** Replace five facets with one stage word. Repair by publishing explicit slot placement.
- **Formality capture.** Use `F` to stand in for articulation, closure, or anchoring. Repair by naming the actual facet owner.
- **Carrier collapse.** Treat a document, cue pack, or routed note as if it were the position itself. Repair by separating carrier lane, publication form, publication face, and position claim.
- **Threshold folklore.** Speak of readiness without any explicit threshold declaration. Repair by publishing relevant local threshold notes on explicit slots.
- **Bridge by vibe.** Treat similar stage language in two schools as equivalence. Repair by explicit `F.9` bridge with loss notes.

### C.2.2a:9 - Consequences
The benefit is that practitioners, including engineers, operators, researchers, managers, and engineer-managers, can speak about where a governed `U.Episteme` stands without hiding the reasons inside vague maturity language. The trade-off is that publication must carry explicit slot and threshold information when decisions depend on it.

### C.2.2a:10 - Rationale
Language-state work needs one explicit statement of what this chart is before individual facet, move, and endpoint patterns start using it. Without that statement, readers have to reconstruct the same geometry from scattered local rules and examples.

### C.2.2a:11 - SoTA-Echoing
The pattern aligns with contemporary work on exploratory reasoning, embodied inquiry, operator-centered decision support, and structured representation: the useful invariant is not one universal ladder of maturity, but a stable multi-facet `U.CharacteristicSpace` chart in which position claims can be published, compared, and moved.

### C.2.2a:12 - Relations
- Builds on: `A.19`, `E.10`, `F.18`.
- Coordinates with: `C.2.LS`, `C.2.3`, `C.2.4`, `C.2.5`, `C.2.6`, `C.2.7`, `A.16.0`, `A.16`, `F.9`, `F.9.1`, `E.17.1`.
- Constrains: threshold publication, positional claims, and anti-collapse discipline across the language-state cluster.

### C.2.2a:13 - Worked Examples

#### C.2.2a:13.1 - Inquiry cue before endpoint capture
A research cue note may occupy a position claim with:

- moderate `F`,
- low articulation explicitness,
- low closure,
- strong embodied or trace-based anchoring,
- and mixed representation factors.

That position explains why the note should remain upstream of `A.6.P` or `C.25` even if its prose happens to look polished.

#### C.2.2a:13.2 - Routed operator alert note
A routed operational alert may have:

- moderate formality,
- medium articulation,
- low closure because several responses remain live,
- strong operator-loop anchoring,
- and mixed symbolic / natural-language representation.

That position explains why the alert belongs in a route-bearing seam publication before it hardens into an endpoint-owned action record.

#### C.2.2a:13.3 - Viewpoint-bound adequacy note
A document-mediated adequacy note about an architecture description may be relatively high in formality and articulation, mid-level in closure, document-mediated in anchoring, and strongly symbolic in representation. That position remains within the same language-state chart even though its carrier lane differs from an embodied inquiry cue.

### C.2.2a:14 - Position Publication Package Discipline
A publishable position claim should normally identify:

- the occupant whose position is being described;
- the relevant slot values, `ValueSet` claims, or intervals;
- the current publication form and, if relevant, the MVPK face and carrier;
- any source-versus-face anchoring distinction that matters;
- the thresholds, if any, being invoked;
- and the next owner or move family that depends on the claim.

This keeps the claim operationally useful without pretending that the position is itself a full trajectory or endpoint form.

### C.2.2a:15 - Review Guidance
A reviewer should ask:

1. Is the author naming a position claim in the chart, or only a folk stage label?
2. Is `F` being used as a surrogate for another slot?
3. Are source phenomena, publication forms, publication faces, and carriers being confused with the occupant?
4. Are threshold claims explicit enough for the next move or endpoint decision?
5. If the text compares two contexts, is there a real bridge or only a lexical resemblance?

### C.2.2a:16 - Boundary Notes
`C.2.2a` does not own move kinds, seam publication species, endpoint repair semantics, or bridge substitution licence. Those belong respectively to `A.16` / `A.16.0`, `A.16.1` / `B.4.1` / `B.5.2.0`, `A.6.*` / `C.25`, and `F.9` / `F.9.1`.

Its job is narrower and more foundational: to make the declared language-state `U.CharacteristicSpace` chart readable so that downstream patterns can refer to one visible common geometry instead of rebuilding it piecemeal.

### C.2.2a:End



