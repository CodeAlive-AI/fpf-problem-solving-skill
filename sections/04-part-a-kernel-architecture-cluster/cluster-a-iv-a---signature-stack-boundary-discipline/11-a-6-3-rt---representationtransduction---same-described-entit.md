## A.6.3.RT - RepresentationTransduction - same-described-entity representation-scheme transition
> **Status:** Stable

**Placement.** Specialization under `A.6.3 U.EpistemicViewing` for same-described-entity representation-scheme transition.
**Builds on.** `A.6.3 U.EpistemicViewing`; `A.6.2 U.EffectFreeEpistemicMorphing`; `A.7`; `E.10.D2`; `C.2.7`; `E.17.0`; `E.17`; `F.9`; `F.18`.
**Coordinates with.** `ConservativeRetextualization`; `ExplanationFaithfulnessProfile`; `E.17.ID.CR ComparativeReading`; `A.6.4 U.EpistemicRetargeting`; `A.15`; `A.20`; `A.21`; explicit decoding access review.

**One line summary.** `RepresentationTransduction` is a same-described-entity shift in representation-scheme that stays inside `A.6.3 U.EpistemicViewing`: it may move between prose, table, diagram, structured notation, or another declared representation regime, but it does **not** silently change `describedEntityRef`, promote geometry or notation into ontology-by-default, or hide decode-mediated recoverability behind rendering fluency.
**Governed object in plain terms.** One published rendering of the same-described-entity in a different representation-scheme or reasoning-medium; not the whole source corpus, not a new ontology, and not a carrier-operation workflow.
**Governing move in plain terms.** Change representation-scheme while keeping same-described-entity support reviewable, factor deltas visible, and reroute explicit when the case has become explanation, retargeting, bridge work, or a weaker-use card.

**Use this when.** Use this pattern when the same-described-entity needs to move across representation-schemes or reasoning media such as prose, table, diagram, or structured notation, and the real job is still the representation shift rather than explanation, retargeting, or downstream action.

**Start here when.** Your first honest artefact already changes representation-scheme or reasoning-medium, and the main review question is whether the target stays source-tethered and same-described-entity rather than becoming a new ontology, a hidden bridge, or a weakened proxy.

**What goes wrong if missed.** A table, diagram, or notation shift gets treated as harmless formatting even after it has started hiding recoverability loss, ontology drift, decode work, or a separate weaker-use card.

**What this buys.** One honest same-described-entity representation shift with visible source tether, visible factor and reasoning-medium change, and an explicit reroute when the case stops being ordinary representation transduction.

**Not this pattern when.** Not this pattern when only wording changes (`ConservativeRetextualization`), explanation becomes primary (`ExplanationFaithfulnessProfile`), the object-of-talk changes (`A.6.4`), or the target stays honest only by carrying its own narrower use, unsupported use, and stronger-source reopen card because deliberate attenuation has become the governing issue. In that last case, route to `A.6.3.CSC Controlled Semantic Coarsening` instead of resolving it as ordinary `RepresentationTransduction`.

### A.6.3.RT:1 - Problem frame


The same-described-entity often needs to be carried across more than one representation regime:
  prose into a table that makes comparison or coverage clearer;
  a table into a diagram that foregrounds dependency or topology;
  a diagram into a structured notation suitable for replay or technical review;
  a source representation into another regime that changes reasoning affordances without changing the underlying object-of-talk.

In practice these shifts are often treated as harmless reformatting. But some representation changes alter reasoning affordances, weaken recoverability, or quietly change what appears to be present in the source. FPF already has `A.6.3` for same-described-entity conservative viewing. This pattern names the recurring same-described-entity case where the published result changes representation-scheme while the case still remains inside `A.6.3`.

### A.6.3.RT:2 - Problem

Without a dedicated named pattern for representation-scheme transitions:
1. teams treat text-to-table, table-to-diagram, and notation shifts as if they were all the same kind of harmless rewrite;
2. changes in reasoning-medium and recoverability remain implicit;
3. latent/distributed cases tempt authors to treat geometry or feature clusters as ontology-by-default;
4. readers cannot tell when a case is still same-described-entity viewing and when it has become retargeting, explanation, carrier work, or decode-mediated reconstruction;
5. representation-factors owned near `C.2.7` are discussed rhetorically rather than as explicit deltas.

### A.6.3.RT:3 - Forces

  **Same-entity, different reasoning-medium.** Teams need different representational forms without silently changing the described entity.
  **Legibility vs recoverability.** A clearer representation is useful only if readers can still recover how it relates to source claims, anchors, and pins.
  **Representation change vs ontology drift.** A new notation or geometry can make structure more visible, but it must not silently become a new object-of-talk.
  **Recoverability before decode ambition.** Start from cases where recoverability can be reviewed directly before leaning on decode-mediated reconstruction.
  **Owner restraint.** This pattern must stay under `A.6.3`, not swallow explanation governance, retargeting, bridge work, or carrier work.

### A.6.3.RT:4 - Solution — same-described-entity representation-scheme transition under `A.6.3`

#### A.6.3.RT:4.1 - Informal definition

> `RepresentationTransduction` is a named pattern specialized under `A.6.3 U.EpistemicViewing` for same-described-entity transitions across declared representation-schemes.
>
> It preserves `describedEntityRef`, keeps the transform effect-free, and makes explicit what changes in representation-factors, reasoning-medium, recoverability, and loss profile.
>
> It may move between prose, table, diagram, structured notation, or another declared representation regime. It may not silently change the described entity, silently import bridge semantics, or treat decode-mediated structure as if it were directly given.

#### A.6.3.RT:4.1.a - Pattern, case, and published rendering distinction

`RepresentationTransduction` is an **intensional pattern** and a named specialization under `A.6.3`. Concrete same-described-entity representation changes are passive episteme-level cases or published renderings reviewed under this pattern; the pattern itself does not act, decide, or publish.

This distinction matters because the pattern governs **how** a representation change is recognised, justified, and checked. It does **not** turn every table, diagram, or structured notation into a giant standalone evaluation object, and it does not reduce assessment to a mechanical reformatting step.

#### A.6.3.RT:4.1.b - Local working vocabulary

This pattern uses a small local vocabulary for evaluating representation changes.
  **Representation-scheme** = the published form in which the same-described-entity is rendered (for example prose, table, diagram, or structured notation).
  **Reasoning-medium** = the form-specific affordances readers actually use when inspecting the published material.
  **Semiotic mode** = what kind of meaning-bearing support is doing the main work in the rendering, such as structural likeness, trace/index, conventional code, model-mediated correspondence, or decode-mediated recoverability.
  **Factor delta** = the explicit change in representation-factors that matters for evaluation.
  **Source tether** = the visible link back to pinned or otherwise reviewable source material that keeps same-described-entity support honest.
  **Decode-mediated case** = a case where explicit access to the target representation depends on a declared decoding route rather than direct reading from already published source material.
  **actionabilityShift** = a changed reader affordance or apparent readiness created by the rendering. It is not execution authority, gate status, action invitation, work authority, or proof that work may proceed.
  **recoverabilityEvidenceClass** = a load-bearing evidence class for decode-mediated or latent cases. It is not required for ordinary non-latent representation shifts unless recoverability pressure is live.
  **Load-bearing support posture** = the extra support needed only when the representation shift is disputed, assurance-facing, gate-adjacent, externally relied on, decode-mediated, or likely to invite stronger uptake: claim support posture, uncertainty or abstention posture, independent verification question, audience over read risk, anti-drift condition, or recoverability evidence.

These terms are local review aids. They do not create a new face-family or a new ontology pattern.

#### A.6.3.RT:4.2 - Scope and exclusions

**In scope**
  text-to-table shift over the same-described-entity;
  table-to-diagram shift over the same-described-entity;
  diagram-to-structured-notation shift where the represented entity and claim-bearing material stay preserved;
  other same-described-entity representation-scheme changes with explicit recoverability discipline.

**Out of scope**
  any change of `describedEntityRef` or hidden change of object-of-talk (`A.6.4`);
  explanation-facing renderings whose main purpose is didactic or explanatory surface work (`ExplanationFaithfulnessProfile`);
  purely textual rewrites that stay inside one representation regime (`ConservativeRetextualization`);
  carrier work such as rendering, export, upload, serialization, or OCR/parsing like extraction;
  latent/distributed use without explicit decode route and recoverability evidence.


#### A.6.3.RT:4.2.a - Reader guidance

Use this pattern when the object-of-talk stays fixed but the published result changes representation-scheme or reasoning-medium.
  If only wording changes, stay in `ConservativeRetextualization`.
  If the target mainly teaches, narrates, or explains, move to `ExplanationFaithfulnessProfile`.
  If same-described-entity support fails, move to `A.6.4`.
  Stay here when changed representation-scheme or reasoning-medium remains the primary review question, even if some loss is present.
  If the target stays honest only by carrying its own weaker-use card because deliberate attenuation has become primary, route to `A.6.3.CSC Controlled Semantic Coarsening`; do not keep the case here as ordinary representation transduction.

#### A.6.3.RT:4.2.b - What a reader checks first

A reader usually starts with five questions:
1. Is the described entity still the same, or has the object-of-talk shifted?
2. What changed in representation-scheme and reasoning-medium?
3. Can the target still be tethered back to source-bearing material strongly enough for same-described-entity reading?
4. Has the case quietly become explanation, bridge-bearing comparison, retargeting, or carrier work?
5. If decoding is involved, is the evidence class strong enough for the intended face and use?

If the representation shift is no longer the main review problem, and the target instead stays honest only by carrying a weaker-use card with unsupported heavier uptake and reopen duty, the case has crossed out of ordinary representation transduction even if the new form still looks like a neat table, diagram, or notation. Use `A.6.3.CSC Controlled Semantic Coarsening` for that source/rendering relation.

Here, **reopen** means return to the stronger-source-bearing material, while **reroute** means the governing pattern has changed. A coarsened representation may need both.

Only after these questions are answered clearly does a fuller load-bearing review record normally become necessary.

#### A.6.3.RT:4.3 - Working model first; explicit review record only when the case is load-bearing

Most same-described-entity representation shifts should stay human usable and reviewable without turning every table, diagram, or structured rendering into a giant metadata block. This pattern therefore follows **E.14's working model first discipline**: ordinary non-latent cases need enough explicitness to show what stayed the same, what changed in representation and reasoning-medium, what was lost or foregrounded, and where the case would have to reroute.

**Ordinary case (default).** For everyday same-described-entity representation shifts, it is usually enough that the rendering or its surrounding publication keeps explicit:
  which source material is being re expressed in a different representation regime;
  that `describedEntityRef` remains preserved;
  what changed in representation-scheme or reasoning-medium;
  what losses, foregrounding choices, or recoverability limits matter for the reader;
  whether the source is merely pointed at, actually used, faithful to the source material, and supported for the intended use;
  where the case exits if it has turned into explanation, retargeting, bridge-bearing comparison, carrier work, decode-mediated reconstruction with insufficient support, or a separate weaker-use / unsupported use / reopen card whose primary review question is no longer the representation shift.

**Explicit review record (only for load-bearing cases).** A fuller record is warranted when the case is assurance-facing, gate-adjacent, cross-context, correspondence-heavy, decode-mediated, policy-bearing, or likely to be disputed. The record may inherit nearby ids and already pinned metadata instead of restating them inline. When published, that record normally captures:
  what source material is being re rendered and what new representation now stands before the reader;
  what same-described-entity, context, viewpoint, and reference choices stay preserved;
  what claim scope, publication scope, source tether, provenance, and loss profile apply;
  what continuity witness or bridge caution keeps the same-described-entity reading reviewable;
  what stronger world, evidence, gate, or work use stays outside, where the rendering remains supported, and what reopen condition would end this pattern;
  what representation-factor shift, reasoning-medium shift, recoverability class, decode evidence, or correspondence support must be visible for the case to stay honest;
  what public naming keeps the case from sounding stronger than it is.

#### A.6.3.RT:4.3.a - Working support defaults

By default in this pattern:
  primary supported faces for non-latent cases are `Plain` and `Tech`;
  bounded report-only use is lawful when source pins, provenance, loss notes, and same-described-entity support remain visible, and when the target is not relying on one separate weaker-use card to remain honest;
  `Interop` use is supported only when the governing face explicitly declares source-pinned, structure-preserving export without added semantics;
  `Assurance` or gate-bearing use is not default and requires explicit face policy plus source pinned same-described-entity support;
  latent/distributed variants remain bounded until explicit recoverability evidence and decode route discipline are published.

#### A.6.3.RT:4.4 - Direct and correspondence-mediated profiles

**Direct RepresentationTransduction**
  source and target are representation-scheme variants over one same-described-entity source line;
  no `CorrespondenceModelRef` is required;
  the main review question is explicit factor delta, reasoning-medium delta, and recoverability discipline.

**CorrespondenceRepresentationTransduction**
  the target representation is derived through a declared correspondence between epistemes or views of the same-described-entity;
  `CorrespondenceModelRef` is required;
  the result remains under `A.6.3` only if same-described-entity conservativity is still supportable and the correspondence does not silently import extra claims.

Correspondence-mediated representation work does **not** by itself support bridge use, substitution use, or comparative reading. If the case needs those claims, they must be declared separately rather than hidden inside representation language.

#### A.6.3.RT:4.4.a - Recurring same-described-entity representation moves

Recurring same-described-entity moves under this pattern include:
  **Tabulation** — prose or dispersed claims are rendered into a table that exposes comparison or coverage more clearly.
  **Diagramming** — a table or prose relation set is rendered into a diagram that foregrounds structure while remaining source-tethered.
  **Structured notation shift** — prose, table, or diagram material is rendered into a notation better suited for disciplined replay or technical inspection.
  **Correspondence supported representation shift** — the target representation depends on declared same-described-entity correspondence support without thereby becoming a bridge case.

These are recurring move shapes under one governing relation. They are not separate patterns and they do not override `E.17` face discipline.

#### A.6.3.RT:4.4.b - How a reader checks representation-factor and reasoning-medium change
A reader should be able to say, in one short paragraph, what changed in representational shape, what changed in reasoning-medium, and whether the primary change is also a `semioticModeShift` rather than only a scheme change. Typical read outs are: "the table foregrounds comparability across rows", "the diagram foregrounds dependency shape", or "the notation foregrounds explicit argument positions."

When the case is more demanding, that paragraph should also name whether salience, topology, actionability, calibration, or interactivity materially changed. If those shifts cannot be named without slipping into new ontology, hidden bridge work, or a changed described entity, the case is not yet ready to stay here.

#### A.6.3.RT:4.5 - Governing law

##### A.6.3.RT:4.5.a. Preservation law
`RepresentationTransduction` preserves the same-described-entity line, bounded context, and declared claim-bearing source while changing the representation-scheme and, often, the reasoning-medium. It must state what remains preserved about the ontic scaffold, claim scope, publication scope, pins, provenance, and grounding. It must also state whether the case remains direct or correspondence-mediated.

##### A.6.3.RT:4.5.a.1. Local conservativity witness
For this pattern, a new intensional claim is introduced when the target rendering:
  upgrades a source visible relation into a stronger relation theory or stronger dependency semantics;
  turns geometry, notation, embedding proximity, or decoder output into ontology-by-default;
  adds bridge, substitution, comparative reading, or mechanism claims not already supported by the source line or declared correspondence;
  collapses source alternatives, uncertainty, or bounded scope into one stronger commitment;
  or treats decode-mediated recoverability as if it were direct givenness.

Conservativity is approximated here by checking, together, `describedEntityPolicy = preserve`, source tether strength, factor delta, reasoning-medium delta, loss profile, ontic scaffold preservation, and whether each target side connective can be pointed back to pinned source material or declared same-described-entity correspondence support.

##### A.6.3.RT:4.5.b. Loss and reliability law
A reviewed case under this pattern makes explicit which distinctions, affordances, or local cues are lost, foregrounded, or rearranged by the shift in representation regime. Reliability transport may remain source bounded or be explicitly downgraded, but it must never be silently strengthened just because the target form looks clearer, more structured, or more formal.

##### A.6.3.RT:4.5.c. Authority and exit law
A case reviewed under this pattern stays same-described-entity and episteme level. It does not own retargeting, bridge stance, explanation governance, executable docking, gate authority, or work enactment. If the shift depends on decode-mediated recovery, intervention backed extraction, or world/gate consequences, those dependencies must stay explicit and may restrict the target to exploratory or report-only use.

##### A.6.3.RT:4.5.c.1. Same-entity entry condition for decode-mediated cases
A decode-mediated case may stay here only when the target rendering is tethered back to already pinned and provenance-bearing source material for the same-described-entity. A decode-mediated result alone does not establish the same-described-entity strongly enough for this pattern.

##### A.6.3.RT:4.5.d. Composition and reopen law
Repeated same-regime normalization may be idempotent, but heterogeneous regime shifts are generally order-sensitive. The case must reopen whenever recoverability assumptions, pins, provenance, correspondence support, or target-face support change. A representation shift also reopens if what looked like one same-described-entity line turns out to require a new described entity or a decode route stronger than currently declared.

#### A.6.3.RT:4.6 - Hard boundary rules

A case reviewed under this pattern keeps the following explicit:
  `describedEntityPolicy = preserve` is mandatory;
  any change of `DescribedEntityRef` exits to `A.6.4`;
  purely textual rewrite cases stay with `ConservativeRetextualization`;
  explanation-facing cases stay with `ExplanationFaithfulnessProfile`;
  carrier work stays outside this pattern;
  geometry, notation, embedding space, or feature clustering must not become ontology-by-default;
  the family changes representation-scheme, not face ownership, and it therefore stays under existing `E.17.0 / E.17` face discipline rather than creating a new publication family.

If recoverability depends on decoding, probing, or intervention, the evidence class must bound supported use; otherwise the case stays exploratory, report-only, or outside the supported same-described-entity path under `A.6.3.RT`. Low-evidence decode-mediated results are not weaker canonical publications; they are bounded exploratory or report-only renderings. Non-latent cases remain the default entry path until decode-mediated recoverability is made explicit.

### A.6.3.RT:5 - Archetypal grounding

#### A.6.3.RT:5.1 - Same-entity text-to-table shift
**Source slice.** `Service S showed three recurring latency spikes in the evening batch window. Trace T-44 and dashboard pin D-17 identify the same service and time window.`

**Published table slice.** `| Service | Window | Spike count | Source pins |
| Service S | Evening batch | 3 | T-44, D-17 |`

This is a lawful direct `RepresentationTransduction` if no new claims are introduced, the same-described-entity stays explicit, and the representation-factor delta is declared. In ordinary engineering use, this usually needs a visible source tether, explicit loss notes if anything was omitted, and a clear statement that the table is still about the same service occurrence rather than a new derived object.

#### A.6.3.RT:5.2 - Same-entity table-to-diagram shift
**Source table slice.** `| Node | Depends on |
| CoolingLoop | Sensor A |
| CoolingLoop | Valve B |`

**Published diagram slice.** `CoolingLoop -> Sensor A; CoolingLoop -> Valve B`

The move stays in this pattern only if the described entity is preserved, the diagram does not silently add new semantic commitments, and reasoning-medium change is declared. If the diagram starts asserting a stronger dependency theory than the source table actually states, the case must reopen and may leave this pattern.

#### A.6.3.RT:5.2.a - Correspondence-mediated text-to-table shift
**Source prose slice.** `In the safety view, CL-2 maintains the required temperature condition during standard load.`

**Published table slice.** `| View | Entity | Condition | Correspondence model |
| Safety | CL-2 | required temperature condition during standard load | CM-12 |`

The move stays in this pattern only if the correspondence remains explicit, the described entity stays preserved, and the resulting table does not quietly import bridge semantics or a changed object-of-talk. Because the declared correspondence is doing real work here, a fuller review record is often warranted instead of relying only on the rendered table.

#### A.6.3.RT:5.2.b - Same-entity diagram-to-structured-notation shift
**Source diagram slice.** `CoolingLoop -> Sensor A; CoolingLoop -> Valve B`

**Published notation slice.** `dependsOn(CoolingLoop, SensorA)`
`dependsOn(CoolingLoop, ValveB)`

This remains under `RepresentationTransduction` when the notation stays tethered to the same relation line already visible in the diagram, the described entity remains preserved, and no stronger dependency theory is silently imported by the notational rendering.

#### A.6.3.RT:5.3 - Boundary to textual rewrite
A source prose note is shortened, reordered, or translated but remains essentially textual. That case stays with `ConservativeRetextualization`, not this pattern.

#### A.6.3.RT:5.4 - Boundary to explanation surfaces
A representation shift is performed mainly to teach or narrate rather than to publish another same-described-entity representation regime. That case should leave this pattern and be reviewed under explanation governance.

#### A.6.3.RT:5.4.a - Boundary to bridge-bearing comparison
**Source slice.** `Local reliability note: Pump P-2 remained within operating range during test window W-3.`

**Published comparative slice.** `Pump P-2 in W-3 behaves like Unit U-7 in Plant B and can therefore be treated as operationally equivalent for this comparison.`

This does **not** stay in `RepresentationTransduction`. The rendering has moved from a same-described-entity representation shift to comparative or bridge-bearing reading across-contexts. Once the publication starts asserting cross-context equivalence, substitution, or comparative use, the case must leave this pattern and move to explicit bridge-governed review.

#### A.6.3.RT:5.4.b - Boundary to carrier/export work
**Source rendering slice.** `| Service | Window | Spike count | Source pins |`

**Published export slice.** `latency-report.csv` and dashboard PNG generated from the same table.

This also stays outside `RepresentationTransduction`. The representation-scheme was already chosen; what follows is carrier formatting, export, packaging, or rendering work on that representation. The didactic point is that not every change in visible form is a new same-described-entity representation transition.

#### A.6.3.RT:5.4.c - Boundary to weaker-use dashboard view
**Source slice.** `The incident worksheet tracks three causal branches, two confidence bands, and one still-open ambiguity note for Service S.`

**Published dashboard tile.** `Service S: current dashboard view foregrounds cache-failover evidence; alternative branches and confidence bands remain in the incident worksheet.`

This does **not** remain ordinary `RepresentationTransduction` if the tile is treated as more than a narrow report view. The tile foregrounds one path and suppresses uncertainty and alternative branches, so it stays honest only with a stronger-source return to the fuller worksheet and an unsupported heavier use line. It is not a causal proof, service status verdict, or action cue. Once that weakened-use card becomes primary, the case leaves ordinary same-described-entity representation transduction and must use `A.6.3.CSC Controlled Semantic Coarsening` rather than being treated as a normal scheme shift.

#### A.6.3.RT:5.5 - Boundary to decode-mediated latent cases
A downstream reader or decode path tries to restate a latent region or distributed feature cluster as explicit object/relation content. This stays outside the supported same-described-entity path under `A.6.3.RT` unless an explicit decoding access profile, `recoverabilityEvidenceClass`, and an explicit decode route are already present. Readable decode output alone is not enough.

#### A.6.3.RT:5.5.a - Guarded decode-mediated readout
**Pinned source cluster.** `Probe run P-8 is tied to model state log M-12 and evaluation bundle EV-4 for the same diagnostic case.`

**Published exploratory slice.** `A decode-mediated readout suggests a cluster that may correspond to the same failure episode already pinned in P-8 / M-12 / EV-4. This rendering stays exploratory and report-only until stronger recoverability evidence is published.`

This example remains guarded-open rather than green. The didactic point is that a decode-mediated rendering may still be useful, but it does not become a normal same-described-entity publication merely because the result looks readable.

### A.6.3.RT:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for same-described-entity representation-scheme or reasoning-medium shifts that claim `RepresentationTransduction` inside FPF.
This pattern intentionally biases toward same-described-entity representation shifts and away from hidden retargeting, explanation inflation, weaker-use authority drift, or ontology-by-default through notation or geometry. The main mitigation is explicit recoverability discipline, preserve vs retarget escape rules, `A.6.3.CSC` reroute when a weaker-use card becomes primary, and directly reviewable entry cases before decode-mediated ones.

### A.6.3.RT:7 - Conformance Checklist

1. **CC-RT-1 — Same-described-entity remains explicit.**
   The case preserves `describedEntityRef` without special pleading.
2. **CC-RT-2 — Representation shift is the right family.**
   The result is genuinely a representation-scheme shift rather than mere textual rewrite or explanation work.
3. **CC-RT-3 — Factor, reasoning-medium, and mode deltas are explicit.**
   `representationFactorDelta`, `inferenceRegimeDelta`, and any load-bearing `semioticModeShift` are explicit.
4. **CC-RT-4 — Extended delta axes are explicit when load-bearing.**
   `salienceShift`, `topologyShift`, `actionabilityShift`, `calibrationShift`, and `interactivityShift` are named whenever they materially shape review or misuse risk. `actionabilityShift` means changed reader affordance or apparent readiness, not execution authority, gate status, action invitation, or work authority.
5. **CC-RT-5 — Recoverability is explicit.**
   Recoverability is stated explicitly through `onticRecoverabilityClass` and `onticRecoverabilityMode`.
6. **CC-RT-6 — Decode-mediated cases carry stronger evidence.**
   If the case is decode-mediated or latent/distributed, `recoverabilityEvidenceClass` and decode route are explicit.
7. **CC-RT-7 — Loss / provenance / pinning / reliability are explicit.**
   Losses, provenance, pinning, and reliability transport are explicit.
8. **CC-RT-8 — Preserve-vs-retarget and coarsening reroutes are explicit.**
   If the case fails any of the checks above, the reroute path is explicit (`ConservativeRetextualization`, `ExplanationFaithfulnessProfile`, `A.6.4`, `A.6.3.CSC Controlled Semantic Coarsening`, or another pattern).
9. **CC-RT-9 — Direct vs correspondence split is explicit.**
   The case states whether it is direct or correspondence-mediated; if correspondence-mediated, `CorrespondenceModelRef` is explicit.
10. **CC-RT-10 — Non-default face/surface support is explicit.**
    Any `Interop`, `Assurance`, gate-bearing, or decode-bounded use states explicit face support and keeps same-described-entity support visible.
11. **CC-RT-11 — Decode-mediated same-described-entity entry tether is explicit.**
    A decode-mediated case states how the target rendering is tethered back to already pinned and provenance-bearing source material for the same-described-entity.
12. **CC-RT-12 — No hidden bridge or face-family inflation.**
    The case makes clear that representation work does not by itself support bridge use, substitution use, or comparative reading and does not create a new face-family.
13. **CC-RT-13 — Reopen triggers are explicit when recoverability, supported use posture, or primary mode changes.**
    If recoverability assumptions, pins, provenance, correspondence support, target-face support, or the primary semiotic-mode change, the case records the reopen trigger explicitly.

### A.6.3.RT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it is wrong | How to avoid it |
|---|---|---|
| Treating every format shift as harmless formatting | representation changes can alter reasoning affordances and recoverability | publish factor delta and reasoning-medium delta explicitly |
| Collapsing representation-scheme shift, semiotic-mode shift, and viewpoint shift into one vague change | readers cannot tell what actually changed or which shift is primary | name scheme, mode, and viewpoint separately and use the canonical boundary exemplars when only one of them changed |
| Letting notation become ontology-by-default | diagram or geometry starts pretending to define the world rather than represent it | keep ontic scaffold preservation and recoverability explicit |
| Hiding retargeting under representation language | a changed object-of-talk is mislabeled as same-described-entity representation work | exit to `A.6.4` whenever `DescribedEntityRef` changes |
| Starting with latent/distributed cases before recoverability is explicit | decode work overwhelms same-described-entity review | keep decode-mediated cases out until decoding access and evidence class are explicit |

### A.6.3.RT:9 - Consequences

  Same-entity representation shifts get a lawful place without inventing a new heavy pattern.
  Representation factor and reasoning-medium changes become explicit rather than rhetorical.
  Recoverability and decode dependence become reviewable instead of hidden behind cleaner renderings.
  The pattern remains bounded by `A.6.3`, `A.6.4`, explanation governance, and carrier work.

### A.6.3.RT:10 - Rationale

Teams often need a table, diagram, or notation over the same-described-entity, and the nearest error is to treat that representation change either as harmless rewriting or as automatic authority upgrade. `A.6.3.RT` gives the reader one explicit review axis that neighboring patterns do not: what changed in representation-scheme or reasoning-medium, what same-described-entity tether still holds, and when the move must reroute because recoverability, decode evidence, or downstream use has crossed out of lawful same-described-entity viewing.

### A.6.3.RT:11 - SoTA Echoing


**SoTA note.** This section does not mint an independent second rule layer. It stays truthful only when the Solution, Conformance Checklist, boundary rules, and Relations of this pattern still tell the same story about the governed move and its limits.

**Claim 1.** Best known current architecture description and model based practice treats views, representation-schemes, and reasoning media as load-bearing rather than as decorative formatting.
**Practice / source / alignment / adoption.** ISO/IEC/IEEE 42010:2022 and current SysML v2 view practice treat viewpoint, view, model kind, and rendering discipline as explicit review objects rather than mere layout choices. This pattern **adopts** explicit representation-scheme review, **adapts** it to same-described-entity viewing under `A.6.3`, and **rejects** the shortcut where a clearer table, diagram, or notation is treated as if it had automatically earned stronger ontology or authority.

**Claim 2.** Best known contemporary notation and reasoning practice treats tables, diagrams, and structured notations as reasoning media with different affordances, not as neutral surface restyling.
**Practice / source / alignment / adoption.** Post 2015 model based and notation sensitive review practice treats representational form as something that changes what readers can inspect, compare, or replay. This pattern **adopts** reasoning-medium review, **adapts** it through explicit factor and medium deltas, and **rejects** hidden dependency theory uplift or silent semantic strengthening by prose to diagram or diagram to notation moves.

**Claim 3.** Best known representation aware AI practice treats latent geometry and decode-mediated structure as evidence bounded interpretation rather than ontology-by-default.
**Practice / source / alignment / adoption.** Byte Latent Transformer (2024) and Large Concept Model (2024) both reinforce that representation regime matters, but neither supports silent promotion from geometry, cluster structure, or decoder output to canonical object/relation ontology. This pattern **adopts** representation aware review, **adapts** it through `recoverabilityEvidenceClass`, decode route explicitness, and same-described-entity source tethering, and **rejects** the popular shortcut where readable decode output is treated as if it were direct givenness.

**Local stance.** The load-bearing SoTA claim for this pattern is narrow: representation regime and reasoning-medium are lawful review targets, but geometry, notation, or a decode-mediated result do not become ontology-by-default.

### A.6.3.RT:12 - Relations

  **Builds on:** `A.6.3`, `A.6.2`, `A.7`, `E.10.D2`, `C.2.7`, `E.17.0`, `E.17`, `F.9`, `F.18`
  **Coordinates with:** `ConservativeRetextualization`, `ExplanationFaithfulnessProfile`, `E.17.ID.CR ComparativeReading`, `A.6.4`, `A.15`, `A.20`, `A.21`, explicit decoding access review
  **Primary host relation and main exits:** this specialization stays under `A.6.3`; failed same-described-entity or recoverability conditions exit to `A.6.4`, explanation governance, or later world/gate patterns
  **Boundary notes:** textual same-regime rewrites stay with `ConservativeRetextualization`; explanation-facing renderings stay with `ExplanationFaithfulnessProfile`; bounded comparative review units exit to `E.17.ID.CR ComparativeReading`; described entity changes exit to `A.6.4`; deliberately weaker renderings whose narrower use, unsupported use, and reopen card is primary route to `A.6.3.CSC Controlled Semantic Coarsening`; decode-mediated world/gate consequences remain bounded by explicit evidence and downstream exit.

### A.6.3.RT:12a - Boundary with quantum-like state-representation shortcuts

Use RT first when the same-described-entity is represented through a different representation-scheme: text-to-table, model to diagram, diagram to structured record, state vector to typed description, or one notation to another. Ordinary representation-scheme change remains RT even when the new scheme is more compact.

Action path:

1. Confirm that the described entity stays the same. If it changes, leave RT.
2. Name the source representation-scheme and target representation-scheme.
3. State what changed in representation-factor, reasoning-medium, mode, salience, topology, actionability, calibration, or interactivity.
4. State recoverability: what can be recovered from the target representation, by which route, and with which evidence.
5. If the target representation claims to preserve action, intervention, manipulation, explanation, or cross-level structure, state the causal-abstraction or approximate-causal-abstraction mapping before treating the shortcut as QL coarsening.
6. Ask whether the shortcut depends on a QL cue: contextual probability, incompatible probes, instrument-like update, Hilbert-like or orthomodular representation, open-information-system update law/probe-frame/export-lawfulness burden, or declared lossy export of a state that matters to the decision.
7. If no, stay in RT, CSC, ordinary abstraction, compression, diagramming, causal abstraction, approximation, or representation-learning routes.
8. If yes, coordinate with the `C.26` state-representation coarsening support section and state supported use, unsupported use, and return condition.

For ordinary use, start with the standard shortcut mini-form:


| Mini-entry | Question |
| --- | --- |
| Source | Which representation-scheme, state reading, fuller model, or evidence set is being weakened? |
| Shortcut | Which cheaper, typed, quantized, symbolic, lower-detail, or otherwise transformed representation is used? |
| Loss | Which precision, expressivity, compatibility, recoverability, or evidence relation is not carried? |
| Supported use | Which decision, explanation, triage, comparison, or routing move remains supported? |
| Reopen | Which dispute, decision change, stronger-use demand, evidence gap, or recoverability failure sends the reader back to the source representation or stronger model? |

Use a fuller C.26 coarsening record only when the shortcut becomes reusable, formal, empirical, high-stakes, or tied to comparative performance or tractability claims. In that fuller record, add the mechanism, baseline route, unsupported use, and QL cue needed for the stronger claim.

Do not describe ordinary compression, low-bit implementation, diagramming, or representation learning as quantum-like unless the formal cue is load-bearing.

### A.6.3.RT:End
