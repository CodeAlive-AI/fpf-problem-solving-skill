## E.19 - Pattern Quality Gates: Review & Refresh Profiles

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative

### E.19:0 - Use this when

Use `E.19` when you need to decide whether one new, substantially revised, or aging FPF pattern is ready for admission, refresh, return for repair, or narrower use. It turns quality review into a repeatable pattern-quality run rather than a matter of reviewer taste.

Use it especially when a draft looks structurally compliant but may still fail on first-minute usability, governed-object stability, terminology, SoTA support, neighbouring-pattern boundaries, examples, anti-patterns, or shipping-facing authority claims.

**Not this pattern when.** Use `E.8` to write the pattern body. Use `E.9` to record the content decision that explains why FPF should change. Use local patterns for the domain law being reviewed. Use project gate or release patterns when the question is whether a project artifact passes a delivery gate rather than whether an FPF pattern is mature.

### E.19:0.1 - What goes wrong if missed

Review collapses into surface compliance or personal taste. A draft can pass because it has the right headings while still being hard for a practitioner to recognise, too thin against current practice, unclear about its governed object, or misleading about neighbouring patterns and authority posture.

### E.19:0.2 - What this buys

`E.19` gives authors, reviewers, and stewards a shared review profile: what must be checked, how deep the check should go, which defects block admission or refresh, and what evidence is needed before a pattern-quality claim is made. It also makes the recognition surface visible before the heavier assurance machinery begins.

**Governed object in plain terms.** The governed object is one FPF pattern-quality review or refresh claim: the reviewed pattern text, the selected profile, the defects found or cleared, and the boundary of the admission or refresh decision.

**Primary working reader.** The first reader is an FPF reviewer, with the pattern author close behind. The review must still be answerable to the eventual practitioner or manager who will rely on the admitted pattern.
### E.19:1 - Problem frame

FPF evolves by adding and revising patterns. Over time, the framework accumulates two kinds of risk:

1. **Admission risk** — a newly authored pattern can be structurally compliant yet still fail on ontology, semantics, terminology conflicts and vagueness, scope, SoTA in related disciplines, or cross-context hygiene.

2. **Staleness risk** — older patterns can remain internally consistent while drifting away from contemporary practice and newer parts of FPF, current internal vocabulary, or updated neighboring patterns. The result is “quiet decay”: the pattern still reads well, but becomes misleading, incomplete, or incompatible.

FPF already contains many checklists and constraints, but they are distributed across patterns and suites. Authors and reviewers therefore lack a single, repeatable way to answer: *What should be checked, and how deep, before a pattern is admitted or kept?*

### E.19:2 - Problem

Without a unified, explicit review pattern:

* Different reviewers optimize for formal/template compliance and miss deeper ontological, semantic, and naming issues, producing bureaucratic output that does not improve the enforceable conformance surface.
* Authors “optimize for the visible checklist” and miss hidden obligations (lexical discipline, Bridge hygiene, SoTA‑Echoing quality, scope claims, delta‑class impact).
* Legacy patterns accumulate “conceptual bit-rot” and diverge from current practice, current terminology, or current internal invariants.
* The specification’s normative surface becomes harder to trust: compliance becomes a matter of reviewer taste rather than a repeatable gate.

### E.19:3 - Forces

| Force                                   | Tension                                                                             |
| --------------------------------------- | ----------------------------------------------------------------------------------- |
| **Uniformity vs Fit**                   | One universal checklist is simple ↔ different pattern kinds carry different risks.  |
| **Rigor vs Editorial cost**             | Deep audits increase quality ↔ they must remain feasible for routine updates.       |
| **Stability vs Evolution**              | Canon should stay stable ↔ it must absorb new SoTA and correct mistakes.            |
| **Conceptual purity vs Enforceability** | Core must stay implementation-agnostic ↔ gates must still be actionable and auditable.     |
| **Local meaning vs Reuse**              | Patterns must remain context‑anchored ↔ authors want to reuse ideas across domains. |
| **Freshness vs timelessness**           | Some claims should be evergreen ↔ others decay and must be refreshed on cadence.    |

### E.19:4 - Solution — Profile-based gates for admission and refresh

Establish **Pattern Quality Gates (PQG)**: a conceptual review mechanism that applies **profiles of checks** rather than a single monolithic checklist.

A **Pattern Check Profile (PCP)** is a named bundle of check families. Profiles are **additive**: every review applies a baseline profile, then adds risk-driven profiles as needed.

**Terminology note (disambiguation).** PQG/PCP are editorial review constructs in the authoring plane (Part E). They are distinct from enactment/runtime gating constructs such as `OperationalGate(profile)` / `GateProfile` (A.21), which govern Work transitions and gate decision policies elsewhere in FPF.

**Mint vs reuse.** This pattern mints **PQG**, **PCP**, and the profile IDs `PCP-BASE`, `PCP-MOD`, `PCP-PRAG`, `PCP-NORM`, `PCP-SOTA`, `PCP-BRIDGE`, `PCP-SUITE`, `PCP-P2W`, `PCP-TERM`, `PCP-DEONT`, `PCP-REFRESH`, and `PCP-ENTRY`. It reuses existing FPF terms (e.g., **Delta‑Class**, **DRR**, **Bridge**, **CL**, **SoTA Synthesis Pack**) without changing their meanings.

#### E.19:4.1 - Define the review target

A review **SHOULD** leave one findings-first run record against a named target pattern or landing subset. The run MAY propose didactic restructuring or compact repair direction, but its primary obligation is to leave an independent review record that improves downstream usage and interoperability without relying on chat memory or reviewer taste.

Formal/template defects (e.g. non-compliance with E.8 structure or not conforming to RFC deontic terminology) have lower review priority than semantic/ontological defects or non-SoTA Solutions, but they also **MUST** be recorded and routed into the active repair boundary.

E.g. if the header block is missing or incomplete, **continue with ontology and semantic review first**. Treat missing header fields as one mechanical defect to record and route for repair (PCP-BASE #7), not as a reason to stop.

The run **SHOULD** give best-known **Delta-Class (Δ-0…Δ-3)** and record an initial **impact radius** (dependent patterns/tests/relations that need be changed due to pattern norms), using existing definitions where available (e.g., the LEX-AUTH protocol).

If the local workflow separates review from repair, direct target-text patching, unified-diff output, or immediate remediation edits are optional local tactics rather than part of the core `E.19` artifact. The core obligation is one findings-first run record plus sufficiently precise repair direction.

#### E.19:4.2 - Apply the baseline profile to every run


Every run MUST include **PCP‑BASE** as a triage baseline. Full-depth checking
is selected only where the relevant risk is live; reviewer depth SHOULD
prioritize the load-bearing sections and obligations in E.19:4.2.1.

1. **Internal coherence (problem ↔ conformance claim ↔ solution)**
   The Conformance Checklist matches Problem statement and the Solution (no “orphan requirements” and no “unclaimed obligations”).
2. **Lexical discipline & reserved vocabulary**
   Terms and registers follow lexical rules; ambiguous “everyday” synonyms do not silently replace kernel vocabulary.
3. **SoTA‑Echoing minimum compliance (E.8)**
   SoTA‑Echoing satisfies the E.8 obligations applicable to the pattern kind (Architectural vs Definitional), including post‑2015 sourcing and explicit adopt/adapt/reject stances. If a SoTA Synthesis Pack exists for the topic, SoTA‑Echoing binds to it rather than forking an untracked narrative; any divergence of pattern norms from contemporary practice is explicitly stated as such. SoTA‑Echoing **MUST** be non‑decorative and **MUST** reflect best-known current practice rather than merely popular defaults for the declared problem. It does not create a second rule layer, but it **MUST** govern the Solution and other load-bearing sections, or those sections **MUST** justify divergence explicitly.
4. **Cross-pattern compatibility & impact radius**
   Relations are consistent with declared dependencies and dependents; declared scope/impact is compatible or explicitly limited.
5. **Didactic grounding**
   Archetypal Grounding is present and teaches the concept with concrete anchors, not only abstractions.
6. **Reader-role fit**
   The live pattern body stays addressed to the intended FPF user rather than to FPF developers or package architects. Load-bearing sections explain lawful use, costs, boundaries, reroutes, and neighbouring relations in user terms. Architecture-placement, freeze/merge posture, and broader package-development rationale stay in separate companions or clearly marked informative placement notes when needed.
7. **Template & section integrity**
   This is lowest priority for review depth and **SHOULD NOT** consume effort that would displace ontology/semantics/modularity/slots/SoTA checks.
8. **Modularity & contradiction hygiene**
   The pattern **SHOULD NOT** be overloaded or significantly expand obligations/dependencies without an explicit reason and impact record.
   Checks include: scope containment, split/refactor recommendations when warranted, and contradiction scans against neighbor patterns in Relations.
   The pattern SHOULD balance cohesion and coupling across FPF.
   If the pattern defines specialization or layering, it SHOULD NOT mix slot interfaces or parameters from different levels; use explicit `⊑/⊑⁺` or `Uses` cuts instead.

##### E.19:4.2.1 - Triage: spend depth on load-bearing sections without making reviews heavier

PQG is meant to increase *semantic and ontological trust*, not to turn every review into an exhaustive editorial audit on form. To keep reviews feasible while improving the important parts:

* Treat **load-bearing sections and obligations** as the primary depth targets:
  * the pattern’s **Problem frame**, **Rationale**, and **worked slices** when a new family/profile/specialization would otherwise be intelligible only from project context,
  * reader-role fit in **Problem**, **Solution**, **Consequences**, **Rationale**, and worked slices whenever the draft risks mixing user guidance with package-development rationale,
  * the pattern’s **Conformance Checklist** (the enforceable conformance surface): keep items universal, cognitively ergonomic, not overly prohibitive, and avoid duplicating checks that belong to other patterns (modularity),
  * **deontic clauses** (`MUST/SHALL/SHOULD/MAY`) that define obligations on the authoring/validation plane (not laws of nature or mathematical facts; ensure an explicit conformance subject),
  * **admissibility constraints** (`Invariant:` / `Well-formedness constraint:`) that define valid models (cardinality, typing/kinds, totality) and are written as non-deontic predicates (no RFC keywords inside the predicate),
  * **definitions and mint/reuse decisions** (new terms, renamed terms, scope claims baked into names, names that are not overloaded and are properly chosen),
  * **cross-context / cross-plane claims** (Bridge hygiene and “sameness” assertions),
  * **SoTA** (when the pattern claims state-of-the-art rather than a popular-but-outdated solution or vocabulary),
  * **modularity and Slot discipline of A.6.5** that provide evolvability of FPF,
  * **absence of contradictions in a pattern**,
  * **Relations** that define compatibility and impact radius.
* Treat **low-signal text** as “quick-pass” unless it changes meaning: headings, micro-typos, stylistic polish, and non-load-bearing narrative refactors, including RFC-form deontic cleanup.
* **Do not block semantic review on template and RFC compliance defects.** Missing header block fields (E.8 H-5), missing canonical sections, or a missing footer marker are fixable integrity defects. Record them as repair items and continue with the load-bearing section checks in the same run.
* **Sentence-level precision matters on load-bearing prose.** Reviewers SHOULD inspect load-bearing sentences for generic heads, burden-carrying qualifiers, overloaded trigger words, bare relation shorthand, and hidden process/API metaphors. The default repair order is: restore head kind, then qualifier burden, then comparison/escalation axis homogeneity, and only then judge whether a later Plain or coarsened rendering is lawful.
* **Design-time and run-time both count.** The same precision discipline applies to live FPF pattern prose and to any target publication text, worked slice, or governed runtime exemplar when that text is being assessed for stronger admissibility, guidance, reuse, or gating.
* **Report ordering (impact-first).** In run outputs and remediation direction, prioritize findings on ontology, semantic, modularity and SoTA-related load-bearing sections first; group low-signal formatting/typos into one compact tail finding unless they change meaning.

#### E.19:4.3 - Add risk-driven profiles

**PCP‑PRAG (Pragmatic utility & adoption)** — Trigger: the pattern is Normative and claims practice guidance.
Checks include: a visible first-reading recognition surface early enough for a cold working reader; a recognisable first-minute working situation; one short `Use this when` or equivalent entry; a plain statement of what goes wrong if the pattern is missed; a plain statement of what the pattern buys in practice; a visible ordinary `not this pattern when` boundary; a minimally viable example; non-decorative Consequences/Anti-Patterns; at least one worked slice when the pattern is easy to misuse; a visible assurance surface carrying declaration, law, modeling, and review burden; role consistency so that the assurance surface does not silently strengthen or universalize the recognition-surface claim; explicit practical payoff in user-facing prose; a short user-facing statement of the governed object and any minimal modeling lens when typed declaration support is load-bearing; nearby pairwise plain glosses for high-pressure technical terms that appear before the heavier harness; a short working-reader implication for any `SoTA-Echoing` rows that carry live explanatory load plus visible linkage to the worked cases or boundary slices they discipline; an explicit primary working reader / concern / viewpoint when several reader families are being served; an explicit `So what?` adoption test; and, when the pattern claims universal or transdisciplinary reach, at least three heterogeneous recognition-surface situations with `F.16` preferred as the compact example-matrix template.
**PCP‑MOD (Modularity & layering discipline)** — Trigger: the review target shows scope creep or level-mixing (e.g., one pattern bundles universal core rules with frame-specific content and discipline-specific method semantics; or it mixes Intension/Description/Spec roles in one object).
Checks include:

* an explicit **core vs extensions** cut (universal invariants are factored into one stable “core”, and extensions reference it rather than re-stating or mutating it),
* no conflation of **specialization vs dependency**: use `⊑/⊑⁺` for refinement/extension and `Uses` for pipelines; do not mix their semantics,
* no conflation of package-form and host-relation roles: **Pack vs Kit vs Suite vs Family vs Bundle vs Cluster vs Profile vs Overlay vs Record vs Umbrella** are not interchanged, and the review states carrier status / host relation explicitly instead of leaving it implicit or varying it for style,
* level hygiene: Description-level artefacts do not grow mechanism semantics; MVPK faces remain projections and do not become “the place of truth”,
* slot-discipline hygiene for any ladder: SlotKind invariance is preserved and inherited operations do not gain new mandatory inputs (A.6.5 / A.6.1 specialization discipline).

**PCP‑REFRESH (Staleness & compatibility refresh)** — Trigger: staleness signals are present (e.g., outdated SoTA rows, renamed/superseded Relations targets, terminology drift, or an explicit refresh window in LAT/DRR).
Checks include:

* refresh‑sensitive claims are identified (time‑bounded or ecosystem‑bounded) and either (a) updated with post‑2015 evidence **and** matching Solution changes, or (b) explicitly scope‑limited and labeled as historical lineage,
* Relations are updated to current pattern IDs; deprecations/renames are handled via explicit continuity notes (no silent relabeling),
* when one new or substantially revised pattern subset is being prepared for send or landing, the run explicitly checks which neighboring patterns, host-pattern constraints, companion patterns, Relations targets, or monolith-backed loci require aligned edits so the subset does not land as one isolated local improvement; the run record states which of those updates are inside the claimed boundary now and which therefore remain outside that claimed boundary,
* the run records a Delta‑Class and impact radius; if the refresh causes Δ‑2/Δ‑3, it emits/updates a DRR pointer and triggers any required refresh and Bridge obligations defined elsewhere (E.15/F.15/F.9).

Trigger overrides are permitted but intentionally rare: a run MAY override a triggered profile only when it can show the trigger’s risk is genuinely absent *in this case*, and the record MUST name (a) why the trigger is a false positive here and (b) what compensating check(s) were applied instead.

**PCP‑NORM (Normative contract integrity)** — Trigger: the pattern introduces or changes normative requirements, introduces new conformance items, or shifts downstream obligations.
Checks include:

* **Delta‑Class (Δ‑0…Δ‑3)** and **impact radius** are explicit (what breaks, who depends on this),
* requirements are testable in principle (conceptually), scoped, and non-contradictory,
* downstream patterns cited in Relations are compatible with the new contract.
* where the change is Δ‑2/Δ‑3 or a new normative pattern is being admitted: a DRR exists and references the PQG findings (pointer is sufficient; no duplicated prose).

**PCP‑SOTA (Evidence & SoTA alignment)** — Trigger: the pattern’s Solution asserts “best practice”, “state-of-the-art”, or introduces new synthesis claims.
Checks include:

* each “best practice / SoTA” claim in the Solution is explicitly **bound** to SoTA‑Echoing rows (or to SoTA Synthesis Pack identifiers when used), rather than floating as ungrounded prescription, and those rows identify best-known current practice rather than popularity alone,
* novel synthesis is not presented as established SoTA: it is either (a) framed as a scoped hypothesis with explicit limits, or (b) promoted into/registered as a SoTA Synthesis Pack entry before the pattern is admitted as normative guidance; a merely explanatory SoTA note that leaves the load-bearing sections untouched is non-conforming,
* where traditions disagree materially, the pattern makes the disagreement visible and states why it adopts/adapts/rejects (instead of silently selecting one tradition),
* refresh‑sensitive claims (those likely to decay) are explicitly marked with scope limits, timespan notes, or lineage labeling when appropriate.

**PCP‑BRIDGE (Cross‑context/plane reuse integrity)** — Trigger: the pattern imports claims, terms, or norms across contexts, disciplines, or reference planes.
Checks include:

* explicit Bridge usage where required (no silent identity by spelling),
* Congruence / loss is surfaced where applicable,
* any cross-plane reuse is explicitly acknowledged and its penalties do not leak into unrelated assurances.

**PCP‑SUITE (Mechanism-suite integrity)** — Trigger: the review target introduces or revises a suite-level Description that enumerates multiple distinct mechanisms (e.g., `MechSuiteDescription` or a suite specialization) and/or changes suite obligations, conformance pins, or suite protocols.
Checks include:

* the suite remains a **Description-level** object: it enumerates member `U.Mechanism.Intension` refs and declares shared obligations/pins, but does **not** define mechanism blocks (`OperationAlgebra`, `Transport`, `Audit`, …) and is not used as a mechanism node,
* membership has **set semantics**: `mechanisms` is duplicates-free and order carries no semantics; any intended ordering is expressed only in `suite_protocols`,
* suite protocols are **closed over membership**: if `suite_protocols` is present, each protocol step references a member mechanism (no “step points outside the suite”),
* the suite is not a family of implementations: it MUST NOT be encoded as a `MechFamilyDescription` (families remain “many realizations of one mechanism”, not “many mechanisms”),
* the suite does **not** mint transport exceptions: any cross-context/plane/kind obligation remains Bridge-only; loss/penalties route to `R/R_eff` only; the suite does not embed CL/Φ/Ψ/Φ_plane tables (references/pins only),
* CG/CN contract pins remain explicit references to the single governance card and legality gate: if suite protocols include numeric comparison/aggregation/scoring, they cite `CG‑Spec` (SCP + Γ-fold + MinimalEvidence) and (where applicable) `CN‑Spec`, rather than duplicating “local CG‑Spec-like” content,
* suite protocols contain **no hidden tails**: if UNM/UINDM/ULSAM are required, the protocol expresses them as explicit `Uses` steps and suite audit obligations cite the chosen mechanism ids/refs (no “implicit normalization/aggregation inside score/compare/select”),
* gate separation is preserved: mechanisms/guards use tri-state `GuardDecision := {pass|degrade|abstain}` and MUST NOT publish `GateDecision` / `DecisionLog`; `block` remains gate-level only (`OperationalGate(profile)`),
* defaults remain single-sourced: portfolio mode, dominance regime, and unknown/failure behavior are either pinned in `TaskSignature` / a single policy map or not claimed; the suite does not define competing defaults,
* when the suite claims reusable outputs, publish/telemetry is explicit and terminates via existing publication surfaces (e.g., G.10 and/or PTM), not as a hidden tail inside a selection step.

**PCP‑P2W (Planned baseline & slot-fillings seam integrity)** — Trigger: the review target introduces or revises WorkPlanning artifacts that pin planned fillers for an owner’s slots (e.g., `SlotFillingsPlanItem` or specializations), and/or introduces view projections of such artifacts.
Checks include:

* the PlanItem remains a **WorkPlanning baseline** (`U.WorkPlan.PlanItem`, `kind = SlotFillingsPlanItem`), not an execution log and not a mechanism,
* planned slot filling stays **WorkPlanning-only**: plan items publish planned fillers/pins (ByValue or `<RefKind>`) and MUST NOT include launch values, `FinalizeLaunchValues` witnesses, gate decisions, or decision logs (these are `U.WorkEnactment` / gate-level only),
* ownership and scope are explicit and non-leaky:
  * the item targets exactly one slot owner via `target_slot_owner_ref`,
  * `target_slot_owner_ref` is a **Description-level, edition-addressable** slot-owner ref (kit/suite) and MUST NOT be a `U.Mechanism.IntensionRef`,
  * the item carries explicit P2W anchors (bounded context; and CG-frame/path-slice/scope anchors when used for legality/selection baselines),
* time is explicit: the item includes `Γ_time_selector` or `Γ_time_rule_ref` (XOR); implicit “latest/current” is nonconformant,
* `planned_fillings` is the authority: duplicate `slot_kind` rows are nonconformant unless the slot owner declares the slot multi-valued; any “indices” are derivable projections and are not maintained independently,
* crossing information is referenced, not duplicated: the plan item (and any associated views) cite CrossingBundle/Bridge/policy-id pins rather than embedding CL/Φ/Ψ/Φ_plane tables or defining transport edges,
* MVPK projections remain projections: any `U.View` face (TechCard/PlainView/InteropCard/AssuranceLane) over a plan item MUST NOT add new claims, MUST NOT introduce “shadow defaults”, and MUST avoid “signature” language (signatures belong to intensional objects),
* if a view publishes edition pins or makes claims about crossing/comparability/selection/launch, it MUST also carry the required audit/ownership pins (UTS + Path pins, crossing pins, applicable guard-owner pins); missing pins are treated as nonconformance and read fail-closed downstream.

**PCP-TERM (Terminology & naming protocol)** — Trigger: the pattern introduces new terms, new U.Types, new “unified names”, redefines existing labels, or leans on load-bearing phrases whose head kind or qualifier burden is not yet restored.
Checks include:

* “mint vs reuse” decision is explicit,
* naming follows the local-first naming protocol and avoids scope smuggling (roles/metrics/stages baked into labels; overloaded words used as terms with a local sense). Remediation **SHOULD** use F.18,
* when PCP-TERM is live, `F.18` winner selection and `A.6.P` follow-through are one mandatory chain rather than two optional passes: the run records candidate heads or phrases reviewed, any kind-conflict / lexical-conflict findings, the provisional F.18 winner plus rejected candidates, and the resulting `A.6.P` survival result on the repaired phrase,
* generic heads and burden-carrying qualifiers are not accepted at face value in load-bearing prose: the review restores the head kind first, and a narrowing qualifier by itself does **not** count as that restoration; only then does the review restore the qualifier burden before deciding whether the phrase is lawful,
* if a sentence compares, escalates, downgrades, or otherwise puts pressure on a phrase after that restoration, the review checks that the comparison axis is ontologically homogeneous,
* the run leaves one explicit account of the resulting governed object, governed move, outside work, and any role-word / package-form decision when the repaired wording still carries architectural burden,
* deprecated aliases and continuity rules are respected.

**PCP‑DEONT (Deontic clause hygiene: RFC keywords)** — Trigger: the pattern conflates admissibility/validity constraints with deontic obligations (e.g., uses RFC keywords where a non-deontic Invariant: predicate is required).
Checks include:
* Deontic requirements are expressed with RFC-style keywords (see H-8);
* obligations are not smuggled into prose as informal imperatives. Admissibility/validity constraints are stated non‑deontically as `Invariant:` / `Well‑formedness constraint:` predicates and referenced from the Conformance Checklist when enforceable.
* **Subject discipline for RFC keywords.** If a sentence uses RFC keywords, its grammatical subject **MUST** be an agent or a publishable artefact (author, reviewer, record, published model). RFC keywords **MUST NOT** modify modeled‑world entities (e.g., “Earth”, “RoleAssignment”, “Role”, “holon”) — express those as `Invariant:` / `Well‑formedness constraint:` predicates instead, and (if needed) reference them from CC items.

**PCP-ENTRY (Pattern-entry discoverability and entry-orientation changes)** —
Trigger: one change materially affects how one reader recognizes, selects,
rejects, or reclassifies one strongest pattern home, strongest projection role,
entry-neighborhood, Problem-frame recognition signature, worked entry reading,
or entry-lexeme-support cue.

Trigger posture:

`PCP-ENTRY` is an explicit profile identifier under the existing Pattern Check Profile family. It reuses the `PCP` profile kind; it is an editorial review profile, not a runtime gate, not `GateProfile`, not a workflow state, and not a new route registry.
PCP-ENTRY is risk-triggered rather than universal.
Use one lead review profile for the change, and import other profiles only for
their specific failure mode.

Use this risk-trigger model:

* **Trigger class 0 — micro-edit**
  punctuation, formatting, typo repair, grammar, or meaning-preserving
  compression with unchanged pattern force.
  No `PCP-ENTRY`, no compact host note, no evidence mode, and no parity scan
  are required.

* **Trigger class 1 — local recognition wording repair**
  one improved `Use this when`, `Not this pattern when`, or one removed
  workflow-smelling phrase with unchanged candidate-pattern set and unchanged
  strongest-home / strongest-projection-home boundary.
  Only the four-question core check is required.

* **Trigger class 2 — material entry-support change**
  one new or changed `J.4` row, one pattern or strongest projection role
  newly treated as entry-bearing, one changed wrong-pattern or
  strongest-home / strongest-projection-home boundary, one changed local
  first-entry force, or one material lexical-query cue change.
  The author leaves one compact host-note, runs the core check, and adds at
  most one selected risk check if needed.

* **Trigger class 3 — multi-role or high-risk public entry change**
  one change affecting several live projection/support roles together, one
  public-entry rewrite, one often-misclassified burden, or one newly
  introduced entry-neighborhood.
  The author runs the core check and adds only the relevant selected risk
  check, usually parity, wrong-pattern, public-entry, or worked-reading
  adequacy.

* **Trigger class 4 — retrieval-facing, observed-failure, or measured-improvement change**
  one retrieval-facing support role changes, one observed misretrieval or repeated
  search failure is being repaired, or the patch itself claims measured
  discoverability improvement.
  One selected evidence mode may be required, but benchmark-style reporting is
  not the default.

* **Trigger class 5 — normative authority, kind, or durable-name change**
  one entry-selection split, stable-name settlement, label-family change, or other
  normative architectural rewrite is in scope.
  `DRR`, `PCP-TERM`, and `PCP-MOD` are the lead decision or review homes as applicable;
  `PCP-ENTRY` reviews only the entry-facing effects.

Ordinary non-triggers include:

* punctuation, formatting, and typo fixes;
* meaning-preserving prose tightening;
* one bare mention of a pattern without changed entry-selection force;

* local wording repair that preserves the current first honest burden,
  candidate-pattern set, strongest-home / strongest-projection-home boundary,
  and entry-neighborhood membership.

`PCP-ENTRY` stays one narrow additive review profile, not one super-profile
that absorbs `PCP-PRAG`, `PCP-MOD`, `PCP-TERM`, `PCP-NORM`, and every other
review burden.
It composes with `PCP-PRAG`, `PCP-TERM`, and `PCP-MOD`; it does not replace
them.
Its distinctive object is changed pattern-selection force, changed first-use
burden, changed entry-neighborhood membership, changed tempting-wrong-pattern
boundary, changed Problem-frame recognition surface, changed worked-entry-reading
force, changed entry-lexeme support, and changed semantic support-role parity.

Its default burden is one small core triggered check:

1. **No workflow implication**
   Entry text does not imply mandatory sequence, control transfer, handoff, or
   artefact pipeline unless another strongest home or strongest projection role
   explicitly governs that semantics.

2. **Strongest-home boundary preserved**
   Entry/index/lexical support roles do not redefine the strongest home's `Problem`
   or `Solution`.

3. **First honest burden preserved**
   The change does not make the first burden or case signal misleading.

4. **No duplicate strong support role**
   The change does not create one new stale echo or one second high-detail
   support role outside the one strongest home or strongest projection role already
   named for the claim.

A change pays only the review cost of the concern it actually changes.
Learning-order edits do not trigger `PCP-ENTRY` unless they also change
candidate-pattern force, strongest-home / strongest-projection-home boundary,
first honest burden, or entry-neighborhood membership.
Lexical-only edits do not trigger extra entry-review burden unless they change
pattern-selection force or entry recognition.
Retrieval fixtures are not required unless retrieval-facing behavior is
explicitly claimed, one machine-consumed projection is in scope, or one
observed misretrieval is being repaired.

When the risk warrants more than that core check, the run may add only the
relevant selected risk checks:

* one parity check when more than one pattern-entry
  discoverability-bearing projection changes;
* one wrong-pattern check when known misclassification is live;
* one lexical check when subject-language divergence is material;
* one worked-reading check when `I.2` changes or one high-risk neighborhood
  still lacks depth;
* one public-entry check when coarse public entry wording materially changes
  entry force or carries high public-entry risk;
* one retrieval check when the change is retrieval-facing or repairs one
  observed retrieval failure.

Substantial discoverability changes leave one compact host note in the host
record.
That host-note may stop at one explicit rationale when the risk is already
controlled by strongest-home / strongest-projection-home inspection, support-role
partition, or one local wording repair.
It is not a separate artefact unless the change is high-risk, disputed,
public-facing with material entry risk, or retrieval-facing.

When one compact host note is needed, it names only the changed support role, the
affected entry neighborhood or pattern, the changed first-use burden or
recognition signature, the strongest home or strongest projection role for the
claim or projection role, and the selected check if any.

One compact risk-triggered gate is enough here:

| Change shape | Default check | Acceptance signal |
| --- | --- | --- |
| typo, grammar, formatting, meaning-preserving compression | no evidence run beyond ordinary review | current burden, strongest-home / strongest-projection-home boundary, and support role remains unchanged |
| one Problem-frame recognition-signature wording change or one wrong-pattern clarification | reviewer-only entry check | no workflow implication and no strongest-home / strongest-projection-home drift |
| one `J.4` row change or one changed candidate-pattern set | pattern-selection or wrong-pattern check | intended strongest pattern home or one lawful candidate-pattern set is recoverable without one false mandatory sequence |
| one lexical-hook change | lexical query check | subject-domain phrasing recovers the strongest home or strongest projection role without uncontrolled alias drift |
| two or more projection/support roles change together | support-role parity check | one strongest home or strongest projection role stays unique and the changed support roles agree on first-use burden, wrong-pattern boundary, projection-only status, and no stronger claim than the Core pattern body; they need not share identical wording or examples |
| one high-risk public-facing or materially changed first-entry support role changes | cold-reader recognition task | one reader can recover the intended strongest pattern home or lawful candidate-pattern set under the named first honest burden |
| one retrieval-facing support role changes or one observed misretrieval is repaired | retrieval / `RAG` fixture | retrieval returns the strongest home or intended projection support before one stale echo, and answer-to-strongest-home faithfulness remains intact |

Empirical evidence is required only when the change is:

* high-risk;
* disputed;
* retrieval-facing;
* repeatedly misclassified;
* public-facing with material entry-force change, repeated failure, or one
  measured-improvement claim;
* or itself claims measured discoverability improvement.

`PCP-ENTRY-E4` is selected only when retrieval-facing behavior is explicitly
claimed, one machine-consumed projection is in scope, or one observed
misretrieval is being repaired.
Public-facing changes with material entry-force risk usually select `PCP-ENTRY-E1`.
Lexical-hook changes usually select `PCP-ENTRY-E3`.
Changes across multiple projections or support roles usually select `PCP-ENTRY-E5`.
Observed search or query failures usually select `PCP-ENTRY-E6`, optionally
together with `PCP-ENTRY-E3` or `PCP-ENTRY-E4` when the failure is lexical or
retrieval-facing.

The following evidence modes are selected high-risk tools, not one suite to
exhaust on ordinary authoring passes.
Selected evidence modes may include:

1. **PCP-ENTRY-E1 — cold-reader recognition or pattern-selection task**
   Given one real case signal, can one reader recover the intended strongest
   pattern home or one lawful candidate-pattern set?
   One tiny micro-task is enough:

   ```text
   Given this burden phrase, name:
   1. the first candidate pattern,
   2. one tempting wrong pattern,
   3. the lawful entry stop,
   4. the strongest home or strongest projection role.
   ```

2. **PCP-ENTRY-E2 — wrong-pattern / wrong-home trap**
   Does the support role actively prevent the most tempting wrong pattern or wrong
   family?

3. **PCP-ENTRY-E3 — lexical query check**
   Does subject-domain phrasing retrieve the strongest home or strongest
   projection role without uncontrolled aliases?

4. **PCP-ENTRY-E4 — retrieval / `RAG` fixture**
   Does retrieval recover the strongest home or strongest projection role under
   exact-ID or keyword phrasing, under semantic paraphrase phrasing, and under
   projection-vs-strongest-home ambiguity, while keeping retrieved support,
   source faithfulness, stale echoes, and post-rationalized citation-like
   support from being treated as the semantic source of truth?

5. **PCP-ENTRY-E5 — support-role parity check**
   Do the live support/projection roles, plus any explicit absence note, preserve
   the same first-use burden, strongest-home / strongest-projection-home role,
   wrong-pattern boundary, projection-only status, and no-stronger-than-Core
   claim without requiring identical wording, rows, or examples?

6. **PCP-ENTRY-E6 — observed failure or query-log capture**
   Does one observed misretrieval, wrong-pattern loop, or repeated query miss
   still survive after the repair, or has the live failure actually been
   removed?

#### E.19:4.3.1 - Tiny golden case bank for regression and worked examples

One tiny golden case bank is enough here. It is a review-regression echo, not the canonical entry inventory: rows 1-4 mirror `J.4` / `I.2` entry neighborhoods that already carry entry support, while rows 5-6 add review-specific search and retrieval stress cases. `J.4` and `I.2` remain the strongest entry-support surfaces; this bank only tests whether a change preserved them.
It is not one benchmark suite and does not force universal empirical review for ordinary wording or support-role/projection edits.
A run may cite one relevant golden case or state that none is relevant. It does
not need to execute the whole bank.
It keeps a stable set of recurring entry burdens recoverable across hardening
passes:

| Case | case_signal | expected_entry_neighborhood | candidate_patterns | tempting_wrong_pattern_or_wrong_home | lawful_entry_stop | support_roles_that_help | projections_that_do_not_define_semantics |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | “we need a shortlist, not one winner” | comparison / pool / selected-set publication neighborhood | `A.19.CN`, `A.17-A.19`, `C.18`, `C.19`, `G.0`, and `G.5` when selected-set publication is live | treating `C.11` as one one-off choice when the real burden is selected-set publication or candidate-set stabilization | lawful candidate-pattern set stabilised or selected-set publication opened | `J.4`, one pattern `Problem frame`, one worked entry reading if compact cues still fail | one README blurb, one thin echo, one lexical-query row alone |
| 2 | “we have a vague cue, not yet a claim” | pre-articulation cue neighborhood | `C.2.LS`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0` | forcing the cue into one endpoint-claim, quality, or assurance pattern too early | `burden-reclassified` or cue preserved for the lawful next burden | `J.4`, one pattern `Problem frame`, one case-linked `I.2` reading when needed | one coarse public entry projection alone |
| 3 | “this is the same object rewritten for another audience” | same-entity rewrite neighborhood | `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`, `E.17.ID.CR` | minting one second semantic object or one second competing explanatory lane instead of one same-entity rewrite | `wrong-pattern-rejected` or same-entity rewrite opened | one worked entry reading, one pattern `Problem frame`, strongest-home pointer | one parallel explanatory blurb treated as one second governing home |
| 4 | “the API/contract says X” | boundary-contract unpacking neighborhood | `A.6`, `A.6.B`, `A.6.C`, `A.6.P`, `A.6.Q`, `A.6.A`, `E.17` | treating one boundary phrase as one agent duty, promise, or generic contract paragraph without atomic claim routing | `boundary-claim-pattern-opened` or routed atomic claim set opened | one boundary-focused `J.4` row, one pattern `Problem frame`, one worked entry reading where interface/access confusion is common | one query cue or public entry projection treated as the strongest home |
| 5 | “I found a pattern by search, but I am not sure it is the right one” | one pattern-local recognition-signature case under the live neighborhood | one candidate strongest pattern home plus one nearby pattern if truly live | one lexical near-match or same-family pattern without strongest-home fit | `non-use-confirmed` or `pattern-selected` | one pattern `Problem frame`, one `J.4` row, one lexical-query support hook | one search-query row alone |
| 6 | “the LLM retrieved a helpful-looking paragraph but not the pattern” | one retrieval-facing entry-neighborhood case | one strongest pattern home plus one strongest projection role | one stale thin echo or one projection-only support role answered as if it were the strongest home | `strongest-home-opened` or `worked-reading-needed` | one strongest-home anchor, one projection-only status marker, one retrieval-facing pointer to the strongest pattern home | one thin echo chunk without strongest-home anchor or projection-only cue |

These six cases are enough to keep:

* burden-oriented entry recognition;
* wrong-pattern or wrong-home rejection;
* lawful entry-stop honesty;
* lexical-query support discipline;
* thin-echo retrieval hygiene;
* and strongest-home / projection separation recoverable as the amendment
  lands.

When one empirical or retrieval evidence run is actually selected, the run
makes recoverable only the fields needed by that run, such as:

```text
viewpoint_class
task_prompt_or_query
expected_strongest_home_or_lawful_candidate_set
near_miss_patterns_or_projection_roles_if_any
time_budget_if_relevant
success_criterion_if_relevant
success_or_failure_note
observed_failure_mode_if_any
rationale_or_repair_action
```

When retrieval evidence is selected, keep retrieval result, answer
faithfulness, and stale-echo result distinct without forcing benchmark-style
reporting on ordinary edits.
One minimal retrieval fixture checks exact ID or keyword retrieval, semantic
paraphrase retrieval, projection-vs-strongest-home disambiguation,
and, when thin echoes are live, thin-echo anchor presence.
Ordinary local guidance stays prose-only rather than minting one stable
anchor by default.

#### E.19:4.3.2 - Common hardening accounts are triggered by live burden

When one common hardening burden is load-bearing, disputed, or explicitly invoked by the target, the run record names the checked source and finding. Otherwise absence is ordinary and does not require a by-value `not applicable` recital.

Use triggered accounts only for the burden that is live:

1. **Usability and working-reader fit.** Record this when first-reading recognition surface, assurance surface, first-minute working-reader usability, practical payoff, worked slices, primary-reader fit, or `E.8` / `E.12` / `E.13` / `E.14` / `E.17.*` / `F.16` checks carry the finding or acceptance decision.
2. **Scenario / anti-case / utility-fit basis.** Record this when a scenario pack, anti-case corpus, pilot bank, utility tree, fitness catalog, or analogous source is actually used or materially disputed.
3. **Packaging / host-relation / shipping-fit.** Record this before any send-facing, landing-facing, monolith-facing, or host-relation posture claim. Do not require it for ordinary local wording repairs.
4. **Domain-tightened profile depth.** Record this when a domain-specific mapping note or support stack actually tightens a selected profile or resolves a live finding.

For `PCP-ENTRY`, the ordinary compact host note remains enough unless one of the triggered burdens above is genuinely live.

#### E.19:4.4 - Decision outcomes

A PQG run **MUST** end with (a) one compact list of blocking findings and (b) one concrete remediation-direction account.

**Remediation payload.** The run **MUST** provide repair direction precise enough that one independent repair pass can adopt it into the target text without reinventing the diagnosis. The core obligation is findings-first traceability, not direct patch emission.

**Precision-remediation order.** When a defect sentence combines a generic head, a burden-carrying qualifier, and mixed-axis comparison pressure, remediation SHOULD repair them in that order: restore head kind, then qualifier burden, then comparison-axis homogeneity. A narrowing qualifier does **not** by itself repair the head-kind defect. Only after those repairs may the run keep or reintroduce a Plain, didactic, or coarsened restatement, and only if the more precise upstream reading remains recoverable.

**Report ordering (impact-first).** The blocking findings are the primary artifact. Remediation directions accompany them and SHOULD be listed in descending order of expected impact on semantic trust (load-bearing sections first). Template-only issues belong at the end unless they hide missing content.

**Budget discipline (anti-form-only review).** If the run identifies semantic defects in load-bearing sections, remediation direction **MUST** prioritize those fixes; purely mechanical edits (formatting, micro-typos) **MUST** be minimized and **MUST NOT** dominate the review by volume.

**Noise discipline.** The run record is a human-facing audit trail. It **SHOULD** stay sparse: list findings, boundary exceptions when any exist, repair direction, and decisions; no per-check pass recital is needed when no defect was found.

### E.19:5 - Archetypal Grounding — Tell–Show–Show: System / Episteme


| Scenario | U.System grounding | U.Episteme grounding |
|---|---|
| **Tell** | A safety-critical engineering team proposes a new pattern describing how to gate a subsystem before deployment. The draft looks polished, but it quietly imports domain terms, assumes cross-team equivalences, and introduces obligations that are not listed in its own checklist. | A research group refreshes an older pattern that summarizes how to evaluate evidence strength. The pattern still reads well, but its SoTA references and terminology no longer match current practice, and its Relations point to patterns that were renamed or superseded. |
| **Show (failure without PQG)** | Reviewers focus on whether the idea is good and whether the template exists. The pattern is admitted, but later users disagree on what it requires because the Conformance Checklist is incomplete and key constraints are only in prose. | The pattern remains unchanged because “nothing looks broken”. Over time, it becomes a conceptual fossil: newcomers treat it as current guidance, but it encodes an outdated stance and stale vocabulary. |
| **Show (repair with PQG profiles)** | PCP‑BASE finds missing internal coherence (requirements in prose not reflected in CC). PCP‑TERM finds naming drift and scope-smuggling in new terms. PCP‑BRIDGE finds implicit cross-context identity claims without explicit alignment. The findings-first run record then routes one repair pass before admission, and the final CC becomes the canonical contract. | The run record leaves one explicit decision: update SoTA‑Echoing with post‑2015 guidance and appropriate Solution changes, limit the scope to “historical lineage” where appropriate, and update Relations to current dependencies. The refreshed pattern becomes trustworthy again, and any remaining historical material is clearly labeled as such. |

### E.19:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** (applies to all patterns and all clusters).

Bias risks and mitigations:

* **Governance bias (Gov):** reviewers may over-prioritize “compliance posture” and under-prioritize teaching value.
  *Mitigation:* PCP‑BASE includes didactic grounding and internal coherence checks and priority for ontology and semantics, not to form.
* **Epistemic monoculture (Onto/Epist):** SoTA‑Echoing can become single-tradition name-dropping.
  *Mitigation:* require explicit multi-tradition coverage and usage of F.18 for neutral naming.
* **Pragmatic bias (Prag):** a pattern can be “correct” yet unusable.
  *Mitigation:* consequences and anti-patterns remain mandatory sections, surfacing trade-offs and misuse paths.
* **Didactic bias (Did):** narrative quality can be mistaken for truth.
  *Mitigation:* conformance and SoTA‑Echoing sections bind claims to explicit obligations and lineage.

### E.19:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-E19-1 (Baseline is mandatory).** | Every PQG run **MUST** apply **PCP-BASE** to the review target. | Ensures a uniform minimum gate across all pattern kinds. |
| **CC-E19-2 (Profile selection is auditable).** | The run record **MUST** state (a) the selected PCPs, (b) the trigger(s) for each non-BASE profile, and (c) any override decisions. Any override of a triggered profile **MUST** record why the trigger is a false positive and what compensating check(s) were applied instead. The run record **MUST** account for the whole current profile set rather than only the selected profiles or the easiest visible trigger family; a deontic-only or selected-stack-only recital is nonconforming. | Makes depth decisions repeatable and reviewable. |
| **CC-E19-3 (Delta-Class & impact for breaking change levels).** | If the run proposes or accepts a change that is **Δ-2/Δ-3** (per E.15), the run record **MUST** include Delta-Class, an impact radius, and a DRR pointer; it **MUST** confirm that required refresh and Bridge obligations are triggered where applicable. | Keeps evolution controlled and compatible with downstream dependencies. |
| **CC-E19-4 (Conformance-claim coherence is enforced).** | Remediation **MUST** eliminate “orphan” obligations and “unclaimed” requirements by aligning the target pattern’s Conformance Checklist, deontic clauses, and admissibility constraints with its Solution. | Preserves the CC as the enforceable conformance surface. |
| **CC-E19-5 (Triage & noise discipline).** | The run **SHOULD** prioritize load-bearing sections and obligations (e.g. CC, content of deontic clauses and content of admissibility constraints, definitions, Relations, SoTA, modularity) and keep purely mechanical edits (e.g. RFC-form deontic cleanup) minimal. Template defects **MUST** be fixed before admission (or before closing a refresh run) but **MUST NOT** be used to skip semantic review. | Improves semantic trust without turning review into form-only compliance. |
| **CC-E19-6 (Findings-first remediation direction).** | The run output **MUST** include one compact list of blocking findings plus concrete remediation direction, ordered by semantic impact (load-bearing sections first). Findings stay primary; direct patch text is optional local workflow, not the core `E.19` artifact. | Ensures actionability and independent repeatability without collapsing review into repair. |
| **CC-E19-7 (Recognition surface, assurance surface, and self-containment).** | Admission or refresh runs for new and substantially revised patterns **MUST** check that a first-reading recognition surface appears early enough for the intended reader, that the heavier assurance surface remains visibly second rather than becoming the first real point of entry, and that the assurance surface does not silently shift the recognition-surface claim. The run **MUST** check for a recognisable working situation, what goes wrong if the pattern is missed, what the pattern buys, and an ordinary `not this pattern when` boundary; for any load-bearing typed declaration or modeling lens, the run **MUST** confirm that a short user-facing statement exposes the governed object and the minimal lens that keeps it reviewable; the run **MUST** also check that the governed object keeps one stable kind across title, opening role, declaration role, worked slices, and neighbouring-pattern or support-surface guidance rather than drifting between object, act, work-product, and carrier-placement labels. When a broader umbrella name and a narrower operative branch are both live, the run **MUST** check that the recognition surface makes that stack explicit enough to identify the umbrella, the active branch, the governed object, the move, and the wider work or process that still remains outside. The recognition surface **MUST** start from a recognisable problem-owning domain or practice moment whenever that can be done without loss of precision, rather than opening first with internal package architecture or taxonomy language. Early high-pressure technical terms **MUST** receive nearby pairwise plain glosses; transform-like families **MUST** carry concrete worked slices plus ordinary-vs-load-bearing guidance where needed; and any `SoTA-Echoing` used as live explanatory support **MUST** state a short practitioner or manager implication plus visible linkage to the worked cases or boundary slices it disciplines. If SoTA or practice tradition is load-bearing, the run **MUST** check that governed-object choice, narrowed-branch choice, and practical payoff remain answerable to the relevant domain or practice rather than only to internal package architecture. If a pattern claims universal or transdisciplinary usefulness, the run **MUST** check that this breadth is already demonstrated in the recognition surface through at least three heterogeneous situations, with `F.16` preferred as the example-matrix template. | Prevents architecturally correct but reader-opaque patterns and keeps broad claims from appearing only late in the assurance surface. |
| **CC-E19-8 (Sentence-level precision restoration).** | Load-bearing sentences **MUST** be reviewed for generic heads, burden-carrying qualifiers, overloaded trigger words, bare relation shorthand, and hidden process/API metaphors. A narrowing qualifier does **not** by itself restore head kind. The default repair order is head kind first, qualifier burden second, comparison-axis homogeneity third. When broad umbrella words such as `interpretation`, `reading`, `review`, `surface`, `document`, or `artifact` are carrying live architectural or semantic load, the run **MUST** also restore whether the text names an umbrella, a narrowed branch, a governed object, a move, or a wider work or process outside the governed object before that wording is allowed to carry architectural burden. When naming or terminology repair is load-bearing, the run record **MUST** leave one explicit `F.18 -> A.6.P` account on disk: candidate heads or phrases reviewed, mint-vs-reuse decision, provisional F.18 winner plus rejected candidates, any kind-conflict / lexical-conflict findings, the `A.6.P` survival result on the repaired phrase, and the resulting governed object / governed move / outside-work reading if the wording still carries architectural burden. | Keeps controlled technical writing from collapsing into free shorthand or false precision. |
| **CC-E19-9 (Package-form and host-relation role-word discipline).** | Reviews **MUST** check that role words such as `primary carrier`, `specialization`, `profile`, `overlay`, `family`, `bundle`, `cluster`, `suite`, `pack`, `kit`, `record`, and `umbrella` match the actual ontology of the case and do not drift by stylistic substitution. When naming or ontology repair introduces or retains one head already occupied elsewhere in FPF, the run **MUST** explicitly account for that occupied-kind / occupied-head conflict and say whether the same occupied meaning is intentionally reused or instead blocked as a collision. | Keeps host relations, review roles, and package forms semantically legible. |
| **CC-E19-10 (Reader-role discipline).** | Reviews **MUST** check that live pattern sections are written for the intended FPF user, that any multi-reader draft makes its primary working reader / concern / viewpoint explicit enough, and that package-development reasoning about isolation, landing form, freeze, merge posture, later promotion, safest move, blast radius, or defer posture stays in separate companions or clearly marked informative placement notes. The run record **MUST** name the user-facing sections scanned for this leak family and any repaired or still-informative exceptions. | Keeps reviews from accepting conceptually correct but role-confused patterns. |
| **CC-E19-11 (Precision before relaxation).** | If remediation preserves or introduces a Plain, didactic, or coarsened restatement of a repaired load-bearing sentence, the run **MUST** keep a more precise upstream reading recoverable and must not let the softened form become the only authority-bearing wording. | Keeps later readability aids subordinate to an explicit stronger reading. |
| **CC-E19-12 (Integration impact is accounted for).** | Before send or monolith-facing motion for one new or substantially revised pattern subset, the run record **MUST** explicitly account for neighboring patterns, host-pattern constraints, companion notes, Relations targets, or current monolith sections that now require aligned edits. The run **MUST** say which such updates are inside the claimed boundary now and which therefore remain outside that claimed boundary. | Prevents one locally stronger pattern from landing as an isolated mismatch in the wider FPF pattern set. |
| **CC-E19-13 (Usability account is explicit).** | For one new or substantially revised live pattern subset, the run record **MUST** leave one explicit usability / working-reader-fit account by value: recognition surface vs assurance surface verdict, first-minute working situation, practical payoff, ordinary boundary, worked-slice coverage, primary reader or viewpoint, and the applicable pattern-side human-facing checks used (`E.8`, `E.12`, `E.13`, `E.14`, `E.17.*`, `F.16`, or clearly named local equivalents). | Prevents cold-reader usability from being treated as something the reviewer “just kept in mind”. |
| **CC-E19-14 (Scenario / anti-case / utility-fit account is explicit).** | When the current domain or workstream has a scenario pack, anti-case corpus, pilot bank, utility tree, fitness catalog, or analogous common check source, the run record **MUST** explicitly state which of those sources were consulted, which scenarios or anti-cases were actually checked, which qualities or fitness pressures were load-bearing, and what remains outside the claimed review boundary. | Prevents scenario, anti-case, and fitness checks from disappearing into reviewer memory or external-review folklore. |
| **CC-E19-15 (Packaging / host-relation / shipping-fit account is explicit).** | Before any send-facing, landing-facing, or monolith-facing posture claim, the run record **MUST** explicitly account for host relation, package form, authority-bearing publication role, send posture, landing posture, monolith posture, and other shipping-facing claims that matter for this target. It **MUST** say what was checked, what was blocked, what was cleared, and why the claimed boundary is valid now. | Keeps packaging and shipping checks from being inferred loosely after one local text improvement. |
| **CC-E19-16 (Domain-tightened profile depth is explicit).** | When a domain-specific mapping note or support stack exists under `E.19` (for example semio `FIT-*` or equivalent local depth checks), the run record **MUST** explicitly state which such local checks were used, which PCP load they tightened, and what they found or explicitly did not find. | Keeps local review depth auditable and prevents domain-specific checks from becoming optional folklore around the PCP stack. |
### E.19:8 - Common Anti-Patterns and How to Avoid Them


| Anti-pattern | Symptom | Why it fails (force violated) | How to avoid / repair |
| ---------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------- |
| **Governed-object drift** | The draft appears to govern one thing in the opening, another in the declaration block, and a third in the examples or neighbouring-pattern / support-surface guidance. | Review cannot tell whether the pattern governs an object, a reading move, a work-product, or a whole process, so later naming and boundary decisions become unstable. | Stabilise one governed object early, keep its head kind explicit, and mark note/sheet/UI/rendering/process labels as either examples of that object or separate neighbouring entities rather than stylistic substitutes. |
| **Role-clean but pragmatically foggy** | The draft is addressed to the right reader in principle, but cold working readers still cannot recognise the situation, practical payoff, governed object, or first useful move early enough. | The run passes role hygiene while still failing pragmatic fit and first-minute usability. | Pull a recognisable working situation upward, add one minimally viable worked case, make the practical payoff explicit in nearby user-facing prose, expose the governed object and any minimal modeling lens in plain terms, add plain glosses for early high-pressure terms, and require `SoTA-Echoing` rows that carry live load to name the practitioner or manager implication plus the case they discipline. |
| **Architecture-clean but domain-thin** | The text is internally well placed in the package, but the governed object, narrowed branch, or practical payoff are justified mainly through package architecture while the problem-owning domain, practice, or SoTA appears late or decoratively. | The pattern passes internal architecture checks while drifting away from the domain whose work it claims to improve. | Pull the problem-owning domain moment into the recognition surface, make the narrowed branch and governed object answerable to the relevant domain or practice, and require load-bearing `SoTA-Echoing` to discipline the practical cases rather than merely bless them after the fact. |
| **Verdict-only review** | The run ends with “pass/fail” and prose complaints, but no precise findings-first repair direction. | Raises editorial cost; reduces repeatability. | Require one findings-first run record plus concrete remediation direction; do not rely on direct patch text as the primary artifact. |
| **Single giant checklist** | Review becomes a long, unfocused ritual that few complete. | Increases cost; reduces fit and rigor in practice. | Use a minimal baseline plus triggered profiles. |
| **Template-only compliance** | All headings exist, but obligations are vague and untestable. | Looks uniform; fails enforceability and auditability. | Enforce normative clause hygiene and CC/Solution coherence. |
| **SoTA name-dropping** | SoTA-Echoing is a list of buzzwords with no stance. | Breaks evidence lineage; invites monoculture. | Require adopt/adapt/reject with reasons per item. |
| **Terminology drift by “synonym”** | Authors swap kernel terms for nicer-sounding words. | Increases ambiguity; harms cross-pattern composability. | Apply PCP-TERM and require explicit mini-definitions on first use. |
| **Form-only review** | Review time goes to formatting and micro-edits while the normative surface, terms, Bridges, modularity, slot discipline and SoTA stance are barely checked. | Raises editorial cost without raising semantic trust. | Use the triage rule: treat load-bearing sections as depth targets and keep mechanical cleanup subordinate to semantic correction. |
| **Architecturally right, didactically thin** | The family is lawful, but readers still need project notes to understand what the pattern really governs. | Trust in the monolith depends on external context rather than the pattern text. | Strengthen problem frame, worked slices, local definitions, and reroute guidance before admission. |
| **Scenario-name grounding** | Grounding names a situation but does not show what the source and resulting publication actually look like. | Readers cannot tell why the case stays in the family or where it exits. | Add concrete source/result slices, especially for transform families and easy boundary confusions. |
| **Generic-head underspecification** | A load-bearing phrase uses a generic head such as `note`, `view`, `guidance`, `output`, or `artifact`, but the run leaves that head uninterpreted. | Review discusses the sentence before the object kind is even stable. | Restore the head kind first in host-local terms before accepting or comparing the sentence. |
| **Qualifier-smuggled burden** | A modifier such as `comparative`, `safe`, `interactive`, `reliable`, or `faithful` is doing the semantic work while the run treats the phrase as already precise. | The review blesses apparent precision without recovering the actual burden. | Unpack the qualifier into explicit burden, comparison basis, or stronger-use boundary before acceptance. |
| **Mixed comparison axis** | One sentence compares or ranks artifact-like, process-like, authority-like, or owner-like things on one axis. | The sentence remains ontologically incoherent even after local wording is polished. | Restore head kind, then qualifier burden, then rewrite the comparison through a homogeneous burden/threshold/handoff axis. |
| **Sentence-level shorthand drift** | A few innocent-looking words (“species”, “branch”, “flow”, “input/output”) quietly carry the semantic burden. | Review passes while key relations remain implicit or wrong. | Inspect load-bearing sentences one by one and replace shorthand with explicit host relations or publication language. |
| **Package-form and host-relation drift** | The text slides between `family`, `bundle`, `cluster`, `profile`, `overlay`, `suite`, `kit`, or `record` without showing that the ontology changed. | Reviews miss owner blur because each local sentence still sounds plausible. | Require one intended role word, check host relation explicitly, and treat stylistic noun-swapping as a semantic defect. |
| **Reader-role leakage** | Live sections explain why the pattern was isolated, what landing form is safest, or why merge/freeze is premature. | Review accepts a package memo disguised as a user pattern. | Move package-development reasoning to companions; rewrite live sections in terms of what the user may do, must avoid, and when the case reroutes. |

### E.19:9 - Consequences

| Benefits                                                                         | Trade-offs / Mitigations                                                                   |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Repeatable admission decisions** — reviewers share a common gate language.     | More explicit editorial work; mitigated by a small baseline and triggered profiles.        |
| **Higher trust in the normative surface** — CC becomes the enforceable conformance surface. | Authors must align prose and CC carefully; mitigated by coherence checks.                  |
| **Controlled evolution** — runs prevent conceptual bit-rot.              | Periodic workload; mitigated by prioritizing high-dependency and high-risk patterns first. |
| **Less hidden drift** — terminology and cross-context reuse become explicit.     | Some drafts will be delayed; mitigated by early profile selection during authoring.        |

### E.19:10 - Rationale

Patterns are both **teaching artifacts** and **normative surfaces**. A specification that grows without explicit quality gates becomes a patchwork: locally good, globally inconsistent. A profile-based gate is the smallest structure that keeps reviews repeatable while remaining sensitive to risk and pattern kind.

The baseline profile protects cross-pattern comparability and editorial sanity. Triggered profiles keep depth where it matters: norms, SoTA claims, cross-context reuse, terminology changes, legacy refresh, and reader-role fit. A pattern that is lawful in package terms but speaks to the wrong reader is still a review defect.

### E.19:11 - SoTA-Echoing — post-2015 review/validation practice alignment

**Evidence binding note.** If a SoTA Synthesis Pack exists for review/validation or refresh discipline in your Context, cite it and keep this section consistent with it; otherwise treat the table below as a provisional seed that should not be duplicated elsewhere without an explicit update record.

| Claim (E.19 need)                                                      | SoTA practice (post‑2015)                                                                                   | Primary source (post‑2015)                                                                  | Alignment with E.19                                                                       | Adoption status                                                                                              |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Reviews need explicit criteria, not informal taste.                    | Move from folklore validation to explicit validation methods and documented criteria.                       | Riehle et al. (2020), “Pattern Discovery and Validation Using Scientific Research Methods”. | PCPs make criteria explicit; CC coherence is enforced.                                    | **Adopt.** Keep methods lightweight but explicit.                                                            |
| A stable structure improves comparability and reduces ambiguity.       | Standards specify required viewpoints/concerns and consistency rules for descriptions.                      | ISO/IEC/IEEE 42010:2022 (architecture description).                                         | PCP‑BASE includes structural integrity and internal consistency.                          | **Adopt/Adapt.** Adopt conformance mindset; adapt to pattern-language template and didactic grounding.       |
| Pattern writing benefits from explicit guidance plus critique culture. | Pattern-language communities emphasize clear template usage, consequences, and critique for quality.        | Iba (2021), “How to Write Patterns …” (PLoP 2021).                                          | Baseline checks enforce meaningful sections; anti-patterns make critique concrete.        | **Adopt.** Directly supports admission quality.                                                              |
| “Living” guidance needs refresh discipline.                            | Reporting and review guidance is updated and versioned; reviewers track changes and report deltas clearly. | Page et al. (2021), PRISMA 2020 statement and explanation papers.                           | Runs require explicit decisions and deltas in SoTA‑Echoing. | **Adapt.** Use the “versioned guidance + explicit deltas” principle without importing implementation or process mandates. |
| Retrieval-facing entry changes need selected evidence dimensions, not universal benchmarks. | RAG evaluation practice separates context relevance, answer faithfulness, answer relevance, and support quality. | Es et al. (2023), `RAGAS`; Saad-Falcon et al. (2023), `ARES`. | `PCP-ENTRY-E4` and related evidence modes select tiny retrieval fixtures only when retrieval-facing behavior or observed misretrieval is live. | **Adopt / lightweight.** Keep hit/support/authority/faithfulness dimensions; ordinary entry prose remains prose-only. |

### E.19:12 - Relations

* **Builds on:**

  * `E.8` (authoring conventions; canonical section order; SoTA‑Echoing obligations)
  * `E.10` (lexical discipline and reserved vocabulary)
  * `E.9` (design rationale records for changes that affect semantics)
  * `E.15` (authoring/evolution protocol; harness mindset; refresh planning)
  * `A.6.5` (slot discipline; SlotKind/ValueKind/refMode invariants)
* **Coordinates with:**

  * `F.8` (mint vs reuse decisions)
  * `F.18` (local-first naming protocol)
  * `F.9` (cross-context alignment discipline)
  * `F.15` (conceptual harness and regression framing)
  * `E.17` (MVPK / `U.View` projection discipline)
  * `E.11` (pattern-entry discoverability discipline, for `PCP-ENTRY` only as a review hook, not as a semantic prerequisite)
  * `A.6.7` (`MechSuiteDescription` suite-level semantics)
  * `A.15.3` (`SlotFillingsPlanItem` P2W planned-baseline seam)
  * `G.11` (refresh/decay orchestration principles, where applicable)

### E.19:End

