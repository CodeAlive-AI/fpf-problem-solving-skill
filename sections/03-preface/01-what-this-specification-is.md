## What this specification is (and how to use it)

This document is the **Core Conceptual Specification** of the **First Principles Framework (FPF)**. It defines a small, domain-agnostic kernel and a set of extension patterns for **publishing, checking, and evolving conceptual work** about *systems* and *epistemes* (knowledge claims) — and about the organisations and communities that build them. In FPF terms these are all **holons**: things that can be treated as wholes and as parts.

FPF is written as a **pattern language**. A pattern is not a tutorial and not a “best practice” blog post; it is a **contract**: *Problem frame → Problem → Forces → Solution*, ending with a **Conformance Checklist**. The canonical template, terminology registers, and the interpretation of RFC-2119/8174 keywords live in **E.8**.

One important cluster of the Core deals with a recurrent real-world problem: teams often have to work with language that is **not yet stable enough** to count as a finished claim, endpoint judgement, or action record, but is already too important to leave as private intuition or carrier noise. In engineering, inquiry, and operator work this shows up as weak cues, partial formulations, route pressure, abductive prompts, and later endpoint publications.

FPF therefore treats this not as one vague maturity ladder but as a governed region of a declared **language-state chart** over `U.CharacteristicSpace`, with explicit facet owners, lawful transduction moves, route-bearing seam publications, and explicit handoff to later endpoint owners. That cluster is what lets an engineer-manager say, in a disciplined way, not only *what is already known*, but also *what is emerging, how far it is articulated, how closed it is, how it is anchored, which routes remain live, and which later owner should receive it next*.

**What is in this document (map)**
- **Part A — Kernel Architecture:** holons, bounded contexts, roles, transformers (Method/Work), time and evolution, modularity, and the core boundary disciplines.
- **Part B — Reasoning Cluster:** aggregation algebra (Γ), trust and assurance (F–G–R), decision cycles, creative abduction, and cross-vocabulary bridges.
- **Part C/D — Extension Specs:** CAL/LOG/CHR packages, plus ethics, conflict topology, and trust-aware mediation scaffolds.
- **Part E — Constitution & Authoring:** pillars, artefact architecture, lexical rules (LEX-BUNDLE), authoring protocol, evolution records (DRR), and quality gates.
- **Part F/G — Publication & Discipline:** the Unification Suite (cards/tables/records like UTS), multi-view publication, and SoTA discipline patterns that operationalise the kernel.
- **Language-state cluster (C.2.2a–C.2.7, A.16–A.16.2, B.4.1, B.5.2.0, A.6.Q, A.6.A):** how FPF models positions in a language-state chart, lawful transduction trajectories between those positions, early seam publications, route publication, abductive handoff, and later precision-restoration or endpoint patterns without flattening them into one vague maturity story.
- **Parts H–K:** glossary, annexes, indexes and navigation aids, and tracked lexical or migration debt.

**Where to start**
- If you want the “why”: **E.1–E.2** (Vision/Mission + Pillars).
- If you want to use FPF on a project tomorrow: **A.0**, then **A.1–A.3**, then **B.3**, then **F.17 (UTS)** and **E.9 (DRR)**.
- If you want to write or review patterns: start with **E.8** and **E.19**.
- If your real situation is “we know something is there, but it is still only partly said”: start with **C.2.2a** for the shared language-state chart, then **C.2.LS / C.2.4–C.2.7** for the facet owners, then **A.16 / A.16.1 / A.16.2** for lawful moves and early preservation, then **B.4.1 / B.5.2.0** for route publication and abductive handoff, and only then move into endpoint owners such as **A.6.Q**, **A.6.A**, or **C.25**. Use **A.16.0** only when branch, loss, handoff, or lineage history itself must be published as an explicit trajectory account.

Everything in the Core is intentionally **tool-agnostic**; implementation details belong to Tooling and worked examples belong to the Pedagogical Companion. The rest of this Preface provides non-normative motivation and reading heuristics for the patterns that follow.

