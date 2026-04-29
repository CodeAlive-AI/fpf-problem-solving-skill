## What this specification is (and how to use it)

This document is the **Core Conceptual Specification** of the **First Principles Framework (FPF)**. It defines a small, domain-agnostic kernel and a set of extension patterns for **publishing, checking, and evolving conceptual work** about *systems* and *epistemes* (knowledge claims) — and about the organisations and communities that build them. In FPF terms these are all **holons**: things that can be treated as wholes and as parts.

FPF is written as a **pattern language**. A pattern is not a tutorial and not a “best practice” blog post; it is a **contract**: *Problem frame → Problem → Forces → Solution*, ending with a **Conformance Checklist**. The canonical template, terminology registers, and the interpretation of RFC-2119/8174 keywords live in **E.8**.

One important cluster of the Core deals with a recurrent real-world problem: teams often have to work with language that is **not yet stable enough** to count as a finished claim, endpoint judgement, or action record, but is already too important to leave as private intuition or carrier noise. In engineering, inquiry, and operator work this shows up as weak cues, partial formulations, route pressure, abductive prompts, and later endpoint publications.

FPF therefore treats this not as one vague maturity ladder but as a governed region of a declared **language-state chart** over `U.CharacteristicSpace`, with explicit facet owners, lawful transduction moves, route-bearing seam publications, and explicit handoff to later endpoint owners. That cluster is what lets an engineer-manager say, in a disciplined way, not only *what is already known*, but also *what is emerging, how far it is articulated, how closed it is, how it is anchored, which routes remain live, and which later owner should receive it next*.

The first operational wave of that cluster is now already present inside the Core. It includes corridor-reading notes in `C.2.2a`, `C.2.LS`, and `A.16`; the checked language-state support branches `A.16.0`, `A.16.1`, and `A.16.2`; naming and lexical host law in `F.18`, `E.10`, and `A.6.P`; the checked downstream burden-family specializations `A.6.Q` and `A.6.A`; same-described-entity textual re-expression in `A.6.3.CR`; the **non-latent branch** of same-described-entity representation-scheme transition in `A.6.3.RT`; explanation classification over existing MVPK faces in `E.17.EFP`; authored-unit umbrella routing in `E.17.AUD`; local pressured-head repair in `E.17.AUD.LHR`; authored-unit stability over one primary object of talk in `E.17.AUD.OOTD`; and bounded comparative reading over comparative review units in `E.17.ID.CR`. In other words, the monolith now carries not only the early language-state corridor itself, but also the checked language-governance and support-branch families that keep that corridor lawful, plus the first downstream families for same-entity rewrites, representation changes, explanation-facing renderings, authored-unit umbrella routing, local authored-unit repair, authored-unit stabilization, and bounded comparative review units. This first wave is now integrated as **Stable under guard** Core material: it is already part of the checked baseline for this corridor, its checked language-governance and support branches, and its first downstream families, but it is not yet the final semioarchitecture settlement or a license to treat latent/decode-mediated `A.6.3.RT` cases as part of that settled path. Those latent or decode-mediated `A.6.3.RT` cases remain outside this first-wave path.

**What is in this document (map)**
- **Part A - Kernel Architecture Cluster:** holons, bounded contexts, role and scope discipline, transformers, time/evolution, work-planning and plan-to-work seams, measurement/comparability foundations, and the signature-stack / boundary-discipline family.
- **Part B - Trans-disciplinary Reasoning Cluster:** aggregation, emergence, trust and assurance, canonical evolution and reasoning cycles, pre-abductive routing, abductive prompting, creative search entry, and bridge-use families.
- **Part C - Kernel Extension Specifications:** the extension calculi and characterization families - Sys/KD/Kind/Method/LOG/CHR, measurement, creativity, NQD, explore/exploit policy, discipline health, problem typing, method-maturity, agentic tool-use, and quality-bundle patterns.
- **Part D - Multi-scale Ethics & Conflict-Optimisation:** axiological neutrality, multi-scale ethics, conflict topology, trust-aware mediation, and bias / ethical-assurance overlays.
- **Part E - The FPF Constitution and Authoring Guides:** vision, pillars, guard-rails, didactic architecture, authoring protocol, lexical law, human-facing working-model discipline, multi-view describing/publication governance, transduction-graph architecture, review gates, and DRR-based evolution governance.
- **Part F - The Unification Suite (U-Suite):** concept-set building, local naming, role descriptions, mint/reuse discipline, bridges, status mappings, method-quartet harmonisation, harnesses, and human-facing publication surfaces such as UTS.
- **Part G - Discipline SoTA Patterns Kit:** CG-Spec, CG-Frame kit authoring, SoTA harvesting and synthesis, lawful characteristics/calculi authoring, selector/dispatcher patterns, shipping surfaces, and telemetry / refresh discipline for repeatable domain packs.
- **Parts H-K:** glossary, annexes and extended tutorials, indexes and navigation aids, and tracked lexical or migration debt.

The navigation clusters below are **reading clusters**. They are not new owner families and do not relocate semantics out of the patterns they reference.

- **Language-state navigation cluster (C.2.2a-C.2.7, A.16-A.16.2, B.4.1, B.5.2.0, A.6.3.CR, A.6.3.RT, E.17.EFP, E.17.ID.CR, E.17.AUD.LHR, E.17.AUD.OOTD, A.6.Q, A.6.A):** how FPF models positions in a language-state chart, lawful transduction trajectories between those positions, early seam publications, route publication, local authored-unit repair, authored-unit stabilization, abductive handoff, and the first same-entity textual, representational, explanation-facing, local-repair, authored-unit-stability, and bounded comparative-reading families without flattening them into one vague maturity story.
- **Project-alignment navigation cluster (A.1.1, A.15, A.15.2, A.15.3, B.5.1, F.9, F.11, F.17):** how FPF establishes local semantic framing, role-method-work alignment, plan/run separation, a simple project lifecycle reading, bridge-aware alignment, and a first human-facing work sheet.
- **Boundary-discipline navigation cluster (A.6, A.6.B, A.6.C, A.6.P, A.6.Q, A.6.A):** how FPF unpacks contract-language and interface boundaries into routed atomic claims, claim registers, precision-restoration branches, and auditable publication faces without contract-soup drift.
- **Comparability & selection navigation cluster (A.17-A.19, A.19.CN, A.19.CPM, A.19.SelectorMechanism, G.0, G.5):** how FPF declares characteristics, governs comparability, keeps comparison distinct from selection, and produces lawful selected-set / set-surface outcomes without hidden scalarization or hidden thresholds.
- **Generator / SoTA / set-surface navigation cluster (A.0, G.0, G.1, G.2, G.5, G.11, C.17-C.19):** how FPF authors a reusable generation / harvest / selector / set-surface scaffold with explicit comparability governance, set-return selection, and open-ended search discipline.
- **Same-entity rewrite / explanation / comparative-reading navigation cluster (A.6.3.CR, A.6.3.RT, E.17.EFP, E.17.ID.CR, E.17.AUD.LHR, E.17.AUD.OOTD):** how FPF restates, re-renders, explains, repairs, stabilizes, and compares already-authored material without silently changing the object of talk or minting a second semantic track.

**Where to start**

The order of Parts in this document follows the didactic architecture of the
Core. A first practical entry does not have to follow that macro-order.

This guidance is coarse entry orientation only. It introduces no new norms and
does not change authoritative pattern meaning.

> **Preface is high-recall, low-detail.**
> `J.4` is the compact canonical entry index.
> `I.2` is the worked-reading depth role.
> The pattern's own `Problem frame` is the local high-precision first-reading
> role.

Choose the first entry by what you are really trying to decide, publish, or
stabilize, not by chapter order.

Consider a human-facing stabilizing result early when vocabulary, decision
criteria, or publication need to stay shareable. A typical lawful stabilizing
result is `F.17 (UTS)` when vocabulary alignment is live; other burdens have
their own publication or review forms.

Use `B.3` when assurance / trust / evidence transport is already part of the
present burden. Use `E.9 (DRR)` when a change to normative content,
authoritative pattern meaning, or durable canon rationale must actually be
published; do not treat it as a universal day-one gate.

- For the **why**: inspect `E.1-E.2`.
- For **writing or reviewing patterns**: inspect `E.8` and `E.19`.
- For **project alignment** - contexts, roles, method, plan, run, and a first
  shared work or vocabulary stabilizer: inspect `A.1.1`, `A.15`,
  `A.15.2 / A.15.3`, and `B.5.1`. Consider `F.11` when method/work vocabulary
  must be aligned across contexts, `F.9` when bridge discipline matters, and
  `F.17` when term stabilization is the live burden.
- When the real situation is **partly-said / language-state discovery**:
  inspect `C.2.2a`, `C.2.LS / C.2.4-C.2.7`,
  `A.16 / A.16.1 / A.16.2`, and `B.4.1 / B.5.2.0`. Consider endpoint patterns
  such as `A.6.Q`, `A.6.A`, or `C.25` only when the burden is actually
  endpoint-owned.
- For **boundary unpacking** - API, contract, protocol, `SLO/SLA`, acceptance
  clause, compliance text, or interface language: inspect `A.6`, `A.6.B`, and
  `A.6.C`. If the first question is only "what description is this?", inspect
  `A.6.RSIG` before routed claim structure. Add `A.6.P`, `A.6.Q`, or `A.6.A`
  only when relation, quality, or action wording is the live burden.
- For **lawful comparison / pool / selection / selected-set publication**:
  inspect `A.19:0`, `A.17-A.19`, `A.19.CN`, `G.0`, `C.18`, `C.19`, and `G.5`.
  Consider `C.11` only when the burden has narrowed to one local decision
  doctrine, and `C.24` only when the next honest artifact is a call plan or
  checkpoint return.
- For a **reusable generator / SoTA / portfolio kit** as the first deliverable:
  inspect `A.0`, `G.0`, `G.1`, `G.2`, and `G.5`. Consider `B.5.2.1` and
  `C.17-C.19` when creative search, novelty, or explore/exploit policy is
  already central. Consider `G.10` / `G.11` when shipping or refresh is live.
- For **same-entity rewrite, explanation, representation change, repair, or
  bounded comparative reading** without minting a new object of talk: inspect
  `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`, and `E.17.ID.CR`. Consider
  `E.17.AUD.LHR` for pressured-head local repair and `E.17.AUD.OOTD` for
  authored-unit stability.

`Preface` helps the reader begin entry; it does not become one second `J.4`.
Update `Preface` when the global entry map changes or the center of gravity of
`FPF` shifts materially. If only one local nearby-pattern cue or one
worked-reading branch changes, that is not automatically one reason to rewrite
`Preface`.

Everything in the Core is intentionally tool-agnostic. Implementation details
belong to Tooling and worked examples belong to the Pedagogical Companion. The
rest of this `Preface` provides non-normative motivation and reading heuristics
for the patterns that follow.

