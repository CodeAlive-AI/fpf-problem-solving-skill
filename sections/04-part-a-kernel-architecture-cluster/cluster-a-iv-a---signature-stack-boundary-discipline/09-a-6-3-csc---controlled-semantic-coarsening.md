## A.6.3.CSC - Controlled Semantic Coarsening

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Placement.** `Controlled Semantic Coarsening` is a specialization under `A.6.3 U.EpistemicViewing` for deliberate same-lineage weakening from stronger source-bearing material into a narrower-use rendering.

**Builds on.** `A.6.3`, `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`, `A.6.P`, `E.8`, `E.10`, `E.19`, and `F.18`.

**Coordinates with.** `E.17.ID.CR`, `F.9`, `F.9.1`, `A.15`, `A.6.4`, `A.20`, and `A.21`.

### A.6.3.CSC:1 - Problem frame

Use this pattern when a summary, briefing, redaction, dashboard tile, lookup handle, didactic compression, or other readable target intentionally weakens distinctions, recoverability, reliability transport, or supported-use strength from a stronger source-bearing material.

`Controlled Semantic Coarsening` governs one weaker rendering that remains useful only because a stronger source stays identifiable, the supported use is narrower, heavier use is unsupported, and escalation reopens the stronger source. It is the FPF owner for that source/rendering relation. It is not a tag, token, `U.*` kind, publication face, carrier, bridge card, stance overlay, work plan, approval, or gate.

**Start here when.** Your first honest artifact is a small controlled-coarsening card: stronger source, weaker rendering, narrower supported use, main weakening, unsupported heavier use, and reopen trigger.

**Typical next owners.** Ordinary same-entity wording routes to `A.6.3.CR`; representation-scheme change routes to `A.6.3.RT`; explanation-facing class discipline routes to `E.17.EFP`; bounded comparison routes to `E.17.ID.CR`; bridge or substitution use routes to `F.9` / `F.9.1`; changed object-of-talk routes to `A.6.4`; work authority routes to `A.15`; gate or adjudication authority routes to `A.20` / `A.21`.

**What goes wrong if missed.** A helpful weak rendering starts acting like the stronger source: a summary becomes evidence, a redaction becomes accountability closure, a dashboard tile becomes a causal verdict, a comparison note starts supporting bridge/substitution use, or a briefing becomes work authority.

**What this buys.** FPF users get a cheap lawful way to publish weakened renderings without hiding loss, overclaiming authority, or forcing every ordinary summary through a full assurance record.

**Not this pattern when.** Not this pattern when the primary question is ordinary same-entity wording, representation-medium change, explanation fidelity, comparison, bridge/substitution use, changed object-of-talk, work authority, approval, adjudication, or gate authority. Use the neighboring owner that governs that primary question.

### A.6.3.CSC:2 - Problem

FPF often needs a weaker form of stronger material: a manager summary, a redacted disclosure note, a dashboard tile, a lookup surrogate, a workshop simplification, or a didactic compression. The weaker form can be valuable, but it becomes dangerous when readers forget that its authority is narrower than the source.

The core failure is not ordinary omission by itself. The failure appears when the weaker rendering stays honest only under a supported-use card like this:

- the stronger source remains governing;
- the target is weaker or less recoverable;
- the target supports only narrower use;
- heavier uptake is unsupported;
- heavier use reopens the stronger source or reroutes to a more honest owner.

Without a named pattern for that relation, neighboring patterns repeat partial coarsening rules locally. The repetition hides the shared burden and makes it too easy for weak renderings to travel as if they were the stronger source.

### A.6.3.CSC:3 - Forces

| Force | Tension |
| --- | --- |
| Reader economy vs source strength | Readers need short, useful renderings, but shortness must not erase the stronger source or its limits. |
| Ordinary use vs load-bearing use | A small summary should stay cheap, while disputed, cited, external, policy, bridge, work, or gate-adjacent use needs more assurance. |
| Helpfulness vs authority drift | The clearer the weak rendering is, the more likely it is to be over-read as evidence, bridge/substitution support, approval, or execution authority. |
| Reuse vs provenance reset | Weak-to-weaker reuse saves effort, but it must not reset source path, loss envelope, uncertainty, or reopen duty. |
| Neighbor clarity vs family sprawl | The coarsening relation needs one common owner without stealing ordinary rewrite, representation, explanation, comparison, bridge, stance, work, or gate law from neighboring patterns. |

### A.6.3.CSC:4 - Solution

`Controlled Semantic Coarsening` governs one source/rendering relation.

- **Stronger source** means the source-bearing material that still carries the stronger claim, distinction, evidence, trace, or authority.
- **Weaker rendering** means the target readable form that intentionally carries less detail, less recoverability, weaker reliability transport, or narrower supported use.
- **Narrower supported use** means the practical use the weaker rendering can still support, such as orientation, retrieval, bounded disclosure, workshop framing, or preliminary triage.
- **Unsupported heavier use** means the use the weaker rendering cannot support alone, such as approval, audit closure, release gate, work plan, equivalence, bridge/substitution use, accountability finding, or canonical technical claim.
- **Reopen trigger** means the condition that requires return to the stronger source, re-expansion in the current rendering or publication, or reroute to another pattern owner.
- **Load-bearing case** means a coarsening case that will be cited, disputed, externally relied on, policy-bearing, bridge-adjacent, gate-adjacent, work-adjacent, privacy-sensitive, or assurance-facing.

#### A.6.3.CSC:4.1 - Ordinary mini-card

For ordinary use, publish only the smallest card that keeps the weaker rendering honest.

| Row | Question |
| --- | --- |
| Stronger source | What stronger material remains governing and reopenable? |
| Weaker rendering | What target form is being offered to the reader? |
| Narrower supported use | What can this weaker rendering support? |
| Main weakening | What distinction, detail, recoverability, reliability transport, or use strength was weakened? |
| Unsupported heavier use | What inference or action is too strong for this weaker rendering alone? |
| Reopen trigger | What demand forces stronger-source return, re-expansion, or reroute? |

The card may live inline. Inherited source pins count when the surrounding publication already makes the stronger source visible.

#### A.6.3.CSC:4.2 - First check

Before using this pattern, ask five questions:

1. Is there a stronger source-bearing material?
2. Is the target deliberately weaker?
3. Does the target support only narrower use?
4. Is heavier use explicitly unsupported?
5. Is the stronger-source reopen or reroute trigger visible?

If any answer is no, do not polish a coarsening story. Use the ordinary host pattern or reroute to the more honest owner.

#### A.6.3.CSC:4.3 - Ordinary vs load-bearing

Ordinary cases should remain light. A short orientation summary, redacted partner note, workshop simplification, or lookup handle does not need the full assurance record if the six-row card is recoverable.

Load-bearing cases add only the fields that matter for the live pressure. This list is not a daily gate for ordinary summaries, briefings, redactions, or lookup handles:

- `sourceLane` and `targetLane` when authored unit, publication face, `PublicationSurface`, `InteropSurface`, or carrier could be confused;
- `targetAuthoredUnitIfAny` when the weaker rendering is carried by one authored-readable unit that is distinct from the publication, disclosure note, dashboard tile, or `InteropSurface` on which it appears;
- `governingSourceRef` or one privileged reopen path, so a weak target cannot reset its own provenance;
- `branchReading` and `supportedUseClass` as separate axes;
- `lossClass` and `recoverabilityAfterCoarsening` when the loss affects claim support, accountability, supported-use posture, or later citation;
- at least one kept claim/distinction bundle, one weakened or dropped bundle, and one reopen-only bundle when the case is disputed or later-cited;
- `sourceSupportPosture` when source-pointer-present, source-faithful, source-used, claim-supported, and supported-for-this-use could diverge;
- uncertainty or abstention posture when branch reading, preserved distinctions, source pin, or supported use cannot yet be stated stably;
- independent-verification question when downstream testing, assurance, gate, or external reliance appears;
- `audienceOverReadRisk`, plus a light uptake or user-evidence check when material readers may mistake the weaker rendering for heavier authority;
- whether local re-expansion is enough to repair the current rendering or whether heavier use still needs return to the stronger governing source.

#### A.6.3.CSC:4.4 - Branch and supported-use discipline

`branchReading` answers what sort of coarsening case this is. `supportedUseClass` answers which use of the weaker rendering remains supported. Do not infer one from the other.

| Axis | Values this pattern uses | Rule |
| --- | --- | --- |
| `branchReading` | aggregation or quotient-like orientation; source-pinned surrogate/index/handle; privacy or redaction weakening; exceptional interop-facing simplification | The branch names the kind of weakening, not the authority granted by the weak rendering. |
| `supportedUseClass` | ordinary supported; source-pinned-only; exceptional host-explicit; unsupported-by-default | The use class names what the weak rendering can support. |

Ordinary supported use covers aggregation, quotient-like orientation, didactic or report summaries, and briefings only for the named narrower use. Source-pinned-only use covers surrogate, index, retrieval-hint, lookup, and handle forms; these may help find or orient to the source but do not become semantic authority.

Privacy or redaction weakening is lawful here only when the card names the sharing boundary, what was withheld or weakened, the main re-identification or accountability risk being reduced, the stronger-source review path, and the accountability or gate uses that remain unsupported.

Exceptional interop-facing simplification is not ordinary coarsening. It is lawful here only when it stays source-tethered and names the operative relation kind, such as bounded contrast, broader/narrower, partial overlap, proxy, lossy normalization, or context-bounded match. If the weak rendering makes bounded contrast across contexts or materials primary, use `E.17.ID.CR`. If it implies equivalence, substitution, projection, or bridge/substitution use, use `F.9` or `F.9.1`.

#### A.6.3.CSC:4.5 - Loss, recoverability, and anti-drift

The card must name the live loss class before a coarsened rendering is treated as lawful.

| Loss class | What weakened |
| --- | --- |
| semantic distinction loss | distinctions, exceptions, alternatives, or claim boundaries disappeared from the weak rendering |
| microtheory loss | the local theory, model, or explanation basis was simplified below source strength |
| modality / force / decision-status loss | recommendation, evidence, possibility, obligation, or decision status was softened or collapsed |
| reliability-transport loss | evidence path, confidence, pinning, trace, or source support became weaker |
| scope / time loss | validity window, population, context, or temporal scope narrowed or became less recoverable |
| face / use-profile loss | the weak rendering moved to a publication face or use profile with weaker support |

Recoverability and supported use are separate. A recoverable weak rendering is not automatically supported for heavier use, and an unsupported use is not repaired merely by saying the source could be found.

| Recoverability class | Reading |
| --- | --- |
| directly recoverable | the weaker rendering itself still carries enough detail to recover the stronger distinction |
| source-pinned recoverable | the distinction is recoverable only by returning to the named stronger source |
| reconstruction or validation required | recovery needs a new reconstruction, test, or validation, so heavier use remains blocked until that work is done |
| not recoverable from lawful materials | the available lawful materials cannot restore the distinction; do not treat the weak rendering as stable authority |

A weak-to-weaker chain may not silently reset provenance. If one coarsened rendering is reused to make another, the same stronger governing source must stay explicit, the earlier loss envelope and uncertainty posture must remain visible, and the new rendering must declare only the added loss delta. If that cannot be stated cleanly, reopen the stronger source rather than extending the chain.

Aggregation or quotient-like coarsening remains inside this pattern only while the weak rendering keeps one bounded described set, slice, case bundle, or alternative bundle explicit as the object of talk. If several entities, alternatives, or slices become one new class target or proxy target, exit to `A.6.4`.

#### A.6.3.CSC:4.6 - Neighbor exits

| If the primary question is now... | Use this owner |
| --- | --- |
| Same-entity textual rewording without a separate weaker-use card | `A.6.3.CR` |
| Representation scheme or reasoning-medium shift | `A.6.3.RT` |
| Explanation-facing class over existing source material | `E.17.EFP` |
| Bounded comparison over already pinned material | `E.17.ID.CR` |
| Equivalence, substitution, interop row, or bridge/substitution use | `F.9` |
| Stance over an already published bridge card | `F.9.1` |
| Changed object-of-talk or proxy target | `A.6.4` |
| Briefing treated as work plan, action authority, or execution cue | `A.15` |
| Gate, approval, assurance, or adjudication authority | `A.20` / `A.21` |

Neighboring owners may point here when a weaker rendering relation becomes primary. They do not own the shared coarsening relation by local repetition.

#### A.6.3.CSC:4.7 - Well-formedness constraints

**Well-formedness constraint CSC-WF-1 (source/rendering relation).** A controlled-coarsening case is well formed only when it contains exactly one stronger-source side, at least one weaker-rendering side, one declared narrower supported use, one unsupported heavier use, and one visible reopen or reroute condition.

**Well-formedness constraint CSC-WF-2 (no authority upgrade).** A weaker rendering does not gain evidence, bridge, work, approval, gate, or adjudication authority by repetition, fluency, audience convenience, citation, or publication on a more visible surface.

**Well-formedness constraint CSC-WF-3 (source path continuity).** A weak-to-weaker chain remains well formed only while the same stronger governing source, prior loss envelope, uncertainty posture, and added loss delta remain recoverable.

### A.6.3.CSC:5 - Archetypal Grounding

**Tell.** Controlled semantic coarsening is the disciplined act of making a weaker rendering useful while keeping the stronger source and the unsupported stronger uses visible. It is not simplification as style. It is simplification under a source, use, loss, and reopen card.

**Show (System).** A service team has an incident review with trace details, confidence bands, and alternative branches. A manager dashboard tile says: `Cache failover evidence is the leading concern; details remain in IR-42.` The tile may orient planning, but it may not approve release, close audit, prove causality, or trigger work without reopening `IR-42`.

**Show (Episteme).** A research review bundle is given the lookup handle `cache-failover risk`. The handle is lawful for retrieval and orientation only. Any claim-bearing use reopens the review bundle because the handle does not carry the evidence, alternatives, or source support.

#### A.6.3.CSC:5.1 - Worked slices

**Manager orientation summary.** The stronger source is incident review `IR-42` with trace details, confidence bands, and alternative branches. The weaker rendering is `Cache failover evidence is the leading concern; details remain in IR-42.` Its narrower supported use is orientation for planning conversation. Its unsupported heavier uses are approval, audit closure, release gate, causal proof, and work order.

**Redacted partner note.** The stronger source is a full incident record with actor identity, trace path, and recovery evidence. The weaker rendering is a partner-facing redacted note that withholds actor identity and trace path. Its narrower supported use is bounded disclosure and coordination. Accountability, legal, audit, readiness, and gate uses reopen the full incident record or exit to the relevant authority owner.

**Exceptional interop-facing simplification.** The stronger source is two pinned context notes plus their bridge or comparison basis. The weaker rendering is: `For this exchange only, Field A is treated as broader than Field B; see source notes for exceptions.` The rendering may orient the exchange, but any equivalence, substitution, projection, bridge-row, or approval use exits to `F.9` / `F.9.1` or reopens the stronger source basis.

**Bad fit: hidden work authority.** `Deployment may proceed; see summary S-3.` This is not a lawful controlled coarsening card. The sentence tries to convert a weak summary into execution or gate authority. Reroute to `A.15`, `A.20`, or `A.21`, and reopen the stronger source before any work or approval claim proceeds.

### A.6.3.CSC:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for source/rendering relations that claim controlled semantic coarsening inside FPF.

This pattern favors **Prag** and **Did** by allowing useful weak renderings to remain cheap and readable. It also favors **Gov** and **Arch** by requiring unsupported heavier use, source reopen, and neighboring-owner exits when authority pressure appears. The mitigation for over-governance is the ordinary mini-card: ordinary cases stay light, and only live pressure adds load-bearing fields.

### A.6.3.CSC:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-CSC-1 (Source visible).** | A conforming controlled-coarsening card SHALL name the stronger source or inherit it from the immediate source context. | Prevents the weak rendering from resetting provenance. |
| **CC-CSC-2 (Rendering explicit).** | A conforming card SHALL identify the weaker rendering and keep it distinct from the stronger source. | Prevents citation laundering and source/rendering collapse. |
| **CC-CSC-3 (Supported use).** | A conforming card SHALL state the narrower supported use. | Keeps ordinary convenience from becoming broad authority. |
| **CC-CSC-4 (Unsupported heavier use).** | A conforming card SHALL state the unsupported heavier use. | Makes over-read and misuse visible early. |
| **CC-CSC-5 (Reopen or reroute).** | A conforming card SHALL state the reopen trigger or reroute condition. | Gives readers a lawful next move under pressure. |
| **CC-CSC-6 (Ordinary economy).** | Authors SHOULD keep ordinary cases to the mini-card unless dispute, citation, external reliance, policy, bridge, work, gate, privacy, or assurance pressure appears. | Preserves usability and avoids daily-process inflation. |
| **CC-CSC-7 (Pressure-specific assurance).** | Load-bearing cases SHALL add only the support fields needed for the live pressure. | Keeps the assurance surface tied to real risk. |
| **CC-CSC-8 (Branch/use split).** | Load-bearing or disputed cases SHALL keep `branchReading` and `supportedUseClass` separate. | Prevents the kind of weakening from implying authority. |
| **CC-CSC-9 (Loss and recoverability).** | Cases affecting claim support, accountability, supported-use posture, or later citation SHALL state loss class and recoverability class. | Prevents recoverability from being mistaken for supported use. |
| **CC-CSC-10 (Weak-chain continuity).** | A weak-to-weaker chain SHALL satisfy `CSC-WF-3` or reopen the stronger source. | Prevents provenance reset by repeated summarization. |
| **CC-CSC-11 (Owner exits).** | Bridge, stance, work, gate, adjudication, and changed-object pressures SHALL reroute to their owners. | Prevents CSC from stealing neighboring law. |
| **CC-CSC-12 (No authority by repetition).** | A conforming card SHALL satisfy `CSC-WF-2`. | Blocks authority laundering through fluency or citation. |
| **CC-CSC-13 (Lane separation).** | Load-bearing cases SHALL separate source lane, target lane, authored unit, publication face, `PublicationSurface`, `InteropSurface`, and carrier when those could be confused. | Keeps authored unit, face, and carrier lanes distinct. |
| **CC-CSC-14 (Privacy/redaction).** | Privacy or redaction cases SHALL name the sharing boundary, withheld distinctions, risk basis, unsupported accountability or gate uses, and stronger-source review path. | Prevents redaction from becoming closure. |
| **CC-CSC-15 (Interop simplification).** | Exceptional interop-facing simplifications SHALL name the operative relation kind and reroute bridge or equivalence pressure to `F.9` / `F.9.1`. | Prevents simplified relation language from supporting bridge/substitution use. |
| **CC-CSC-16 (Source support posture).** | Load-bearing source-support cases SHALL distinguish source pointer present, source used, source faithful, claim support, supported use, independent verification, and audience over-read where those could diverge. | Keeps helpful renderings from passing as evidence. |

### A.6.3.CSC:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Avoid by |
| --- | --- | --- |
| Helpful summary becomes authority | The weak target starts deciding heavier questions. | Publish unsupported heavier use and reopen trigger. |
| Citation laundering | A weak target is cited as if it were the source. | Keep the stronger source named and reopenable. |
| Label-as-evidence | A lookup handle carries a claim. | State retrieval-only use. |
| Redaction-as-closure | Withheld detail is treated as resolved detail. | State the sharing boundary and accountability reopen condition. |
| Stance cure | `projection` or `nonEquivalent` is used instead of a bridge card or source return. | Reroute bridge pressure to `F.9` / `F.9.1`. |
| Briefing-as-work | A summary becomes work plan, action cue, gate, or approval. | Reroute to `A.15`, `A.20`, or `A.21`. |
| Summary chain drift | A note summarizes an already weakened note and loses the original source and loss envelope. | Keep the same stronger source and added loss delta visible, or reopen the stronger source. |
| Aggregation target drift | A quotient or bundle turns several entities or alternatives into one new proxy target. | Exit to `A.6.4` rather than treating target drift as same-lineage weakening. |

### A.6.3.CSC:9 - Consequences

| Benefits | Trade-offs / mitigations |
| --- | --- |
| Cheap weak renderings stay lawful because the source, supported use, loss, unsupported use, and reopen path remain visible. | Authors must add a small card where they might otherwise write only a friendly summary. The mitigation is that ordinary cases need only the mini-card. |
| Neighboring patterns can route coarsening pressure to one common owner instead of repeating partial local doctrine. | Readers must still choose the primary owner correctly. The neighbor-exit table and bad-fit examples keep that choice inspectable. |
| Load-bearing coarsening becomes reviewable without making every summary a full assurance object. | Under high pressure the assurance record can grow. The pressure-specific field rule keeps growth tied to real risk. |

### A.6.3.CSC:10 - Rationale

Controlled coarsening is useful because FPF work often needs cheap readable forms. It is risky because cheap readable forms often travel farther than their lawful use. The pattern therefore does not ban weakened renderings; it makes the weaker-source relation explicit enough that later users know when to stop, reopen, or reroute.

This pattern is narrower than a general simplification pattern. It applies only when the weaker target remains tied to stronger source-bearing material and carries a narrower-use card.

The core memory aid is simple: a weak rendering may help reading, but it must not become the source it weakened.

### A.6.3.CSC:11 - SoTA-Echoing

**Purpose.** This section justifies the pattern's safeguards. It is not an additional operational checklist. The Solution, Conformance Checklist, worked slices, and Relations above carry the live pattern law.

| Claim need | SoTA practice (post-2015) | Primary source (post-2015) | Alignment with `A.6.3.CSC` | Adoption status |
| --- | --- | --- | --- | --- |
| Fluent summaries and generated renderings can be useful while remaining weaker than source support. | Summarization and factuality work separates fluency from faithfulness, attribution, and fine-grained source support. | Maynez et al. (2020), *On Faithfulness and Factuality in Abstractive Summarization*; Min et al. (2023), *FActScore*; Es et al. (2023), *RAGAS*. | `A.6.3.CSC` adopts the source-support distinction by separating source pointer present, source used, source faithful, claim supported, independent verification, supported use, and audience-over-read risk. | **Adopt/Adapt.** Adopt the warning against fluent unsupported output; adapt it into a lightweight FPF card so ordinary summaries are not forced into full evaluation studies. |
| Redaction and de-identification reduce exposure without deleting accountability or audit questions. | Privacy-risk and de-identification guidance treats disclosure boundary, residual risk, and governance context as part of safe release. | NIST SP 800-188, *De-Identifying Government Datasets* (2023). | The privacy/redaction branch requires sharing boundary, withheld distinctions, stronger-source review path, and unsupported accountability or gate uses. | **Adapt.** Use privacy governance as a safeguard for bounded disclosure while rejecting redaction-as-closure. |
| Views, representations, and relation kinds remain load-bearing even when a surface is made easier to read. | Architecture-description and model-based practice make viewpoint, view, model kind, and traceable relation explicit rather than treating a clearer view as neutral formatting. | ISO/IEC/IEEE 42010:2022; OMG SysML v2.0 Language Specification (2025). | The pattern keeps coarsening distinct from representation transduction, explanation profiling, comparative reading, bridge cards, bridge-stance overlays, and work/gate authority. | **Adopt/Adapt.** Adopt explicit view/relation discipline; adapt it to same-lineage weaker renderings and neighbor exits. |
| Data and interoperability publication practice distinguishes discoverability, metadata, validation, and exchange from authority to substitute one object for another. | Web-data and semantic-web standards separate catalog metadata, provenance, structural metadata, and validation conditions from the data or relation itself. | W3C Data on the Web Best Practices (2017); W3C SHACL (2017); W3C DCAT v3 (2024). | Exceptional interop simplification must name its relation kind and reroute equivalence, substitution, projection, or bridge pressure to `E.17.ID.CR`, `F.9`, or `F.9.1`. | **Adapt/Reject.** Adapt explicit metadata and validation discipline; reject using a simplified relation gloss as support for bridge/substitution use. |
| Explanation usefulness depends on the user and can be over-read as stronger authority. | Explainable-AI practice treats explanation as audience-facing support with limits, not as a universal guarantee. | NIST IR 8312, *Four Principles of Explainable Artificial Intelligence* (2021). | `audienceOverReadRisk` and source reopen keep helpful prose subordinate to stronger material when stakes rise. | **Adopt/Adapt.** Adopt user-sensitive explanation limits; adapt them to FPF coarsening cases where a rendering is useful but not authoritative for heavier use. |

The practical implication is the same across these traditions: weak readable surfaces are valuable, but their supported use depends on source support, relation kind, validation burden, audience, and reopen path. The worked slices in `A.6.3.CSC:5.1` are the nearest recovery anchors for those SoTA rows.

### A.6.3.CSC:12 - Relations

- **Specializes:** `A.6.3 U.EpistemicViewing` for deliberate weakening across a source/rendering relation.
- **Coordinates with:** `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`, `E.17.ID.CR`, `F.9`, `F.9.1`, `A.15`, `A.6.4`, `A.20`, and `A.21`.
- **Does not replace:** conservative retextualization, representation transduction, explanation profiling, bounded comparative reading, bridge-card discipline, stance overlay, changed-object discipline, work authority, gate authority, or adjudication authority.
- **Entry relation:** neighboring patterns may route here when a weaker rendering's narrower-use, unsupported-use, and reopen card becomes the primary question.
- **Host relation wording:** this pattern is a `specialization under A.6.3`, not a bundle, suite, profile, overlay, or review pack. Its shared `owner` role is limited to the controlled-coarsening relation itself.

### A.6.3.CSC:12a - Boundary with quantum-like state-representation coarsening

Use CSC first when a fuller material is deliberately made less detailed for a narrower use: summary, dashboard row, orientation note, partner-safe version, simplified diagram, or coarse working description. Ordinary controlled simplification remains CSC even when it is lossy.

Action path:

1. Name the fuller source and the less detailed version.
2. State the use scope of the less detailed version before stating what it means.
3. State the lost distinctions, evidence paths, comparability, uncertainty, state dimensions, or alternatives.
4. State supported use and unsupported use in practical terms.
5. State when to reopen the fuller source.
6. If the weaker rendering claims to preserve action, intervention, manipulation, explanation, or cross-level structure, state the causal-abstraction or approximate-causal-abstraction mapping before treating the shortcut as QL coarsening.
7. Ask whether the shortcut depends on a QL cue such as incompatible probes, contextual probability, instrument-like update, open-information-system update whose update law, probe frame, or export lawfulness is part of the modeling burden, or no faithful-enough export of the represented state for the intended use. If not, stay in CSC.
8. If yes, coordinate with the `C.26` state-representation coarsening support section while leaving CSC as the controlled-use boundary for the weakened version.

For ordinary use, start with the standard shortcut mini-form:


| Mini-entry | Question |
| --- | --- |
| Source | Which fuller material, model, state representation, or evidence set is being weakened? |
| Shortcut | Which less detailed rendering or working shortcut is used instead? |
| Loss | Which distinction, evidence path, comparability, uncertainty, state dimension, or alternative is not carried? |
| Supported use | Which triage, orientation, routing, explanation, or local decision use remains supported? |
| Reopen | Which dispute, decision change, drift, threshold crossing, or stronger-use demand sends the reader back to the fuller source? |

Use a fuller CSC/`C.26` coarsening boundary record only when the weaker state representation will be reused, formalized, empirically compared, used in a high-stakes decision, or tied to a comparative performance claim:

| Field | Required content |
| --- | --- |
| Fuller source | Which richer material, model, state representation, or evidence set is being coarsened |
| Coarsened version | What the reader receives instead |
| Lost distinctions | What precision, comparability, evidence path, state dimension, or alternative is not carried |
| Supported use | Which triage, orientation, routing, explanation, or local decision use remains supported |
| Unsupported use | Which stronger decision, audit, assurance, release, causal, or work-order use is not supported |
| Reopen path | When the fuller source or more precise state representation must be reopened |
| QL cue, if retained | Which incompatible-probe, contextual-probability, instrument-update, open-information-system update/probe/export-lawfulness, or faithful-enough-export burden remains after ordinary CSC |

Useful outputs:

- a CSC mini-form when the issue is controlled simplification;
- a fuller C.26 coarsening support record only when a QL cue remains and the claim is reusable, formal, empirical, high-stakes, or comparative-performance-bearing;
- no QL wording when the case is only summary, anonymization, diagramming, audience adaptation, or ordinary coarsening.

### A.6.3.CSC:End
