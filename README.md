# fpf-problem-solving-skill

[Русская версия (README-RU.md)](README-RU.md)

AI coding agent skill for the [First Principles Framework (FPF)](https://github.com/ailev/FPF) by [Anatoly Levenchuk](https://github.com/ailev).

FPF is a transdisciplinary reasoning architecture for systems engineering, knowledge coordination, and mixed human/AI teams.

FPF is a **thinking amplifier** — it helps you plan deeper and make better decisions by systematically exploring relevant alternatives instead of anchoring on the first idea.

## How it works

This skill functions as **agentic RAG** — retrieval-augmented generation driven by the agent itself, with no external vector database or embedding pipeline. The FPF specification is split into 14 top-level Parts; Part A additionally contains 2 nested clusters (16 directories, 241 files total). SKILL.md provides a thinking-verb router that maps the user's intent to the right section. The agent then navigates `_index.md` files to pick the narrowest leaf (~300 lines) and loads only that into context. The agent is the retriever, the router, and the reasoner — all in one loop.

## Install

```bash
npx skills add CodeAlive-AI/fpf-problem-solving-skill -g
```

## Structure

```
sections/
  04-part-a-kernel-architecture-cluster/
    _index.md                                       # TOC + sub-cluster links
    01-a-0---onboarding-glossary.md                 # 137 lines
    02-a-1---holonic-foundation.md                  # 185 lines
    ...                                             # 19 leaf files
    cluster-a-iv-a---signature-stack-boundary-discipline/
      _index.md                                     # nested TOC
      01-a-6---signature-stack-boundary-discipline.md
      ...                                           # 22 leaf files
    cluster-a-v---constitutional-principles-of-the-kernel/
      _index.md
      ...                                           # 31 leaf files
  06-part-c-kernel-extensions-specifications/
    _index.md
    ...                                             # 36 leaf files
  ...                                               # 14 top-level Parts
```

The agent reads `_index.md` first, picks the right leaf (or descends into a sub-cluster's `_index.md`), and loads only that file.

## Sections

| # | Section | Sub-sections |
|---|---------|:---:|
| 01 | Title page | 0 |
| 02 | Table of Content | 1 |
| 03 | Preface | 17 |
| 04 | Part A — Kernel Architecture | 19 + 2 sub-clusters |
| 04 | &nbsp;&nbsp;└─ A.IV.A — Signature Stack & Boundary | 22 |
| 04 | &nbsp;&nbsp;└─ A.V — Constitutional Principles | 31 |
| 05 | Part B — Trans-disciplinary Reasoning | 24 |
| 06 | Part C — Kernel Extensions | 36 |
| 07 | Part D — Ethics & Conflict | 1 |
| 08 | Part E — Constitution (incl. Section E-I) | 35 |
| 09 | Part F — Unification Suite (incl. Cluster F.I, UTS) | 20 |
| 10 | Part G — SoTA Patterns Kit | 15 |
| 11 | Part H — Glossary | 0 |
| 12 | Part I — Annexes | 1 |
| 13 | Part J — Indexes | 1 |
| 14 | Part K — Lexical Debt | 2 |

## Updating after FPF spec changes

When the upstream FPF specification changes, two things need updating:

### 1. Regenerate section files

Pull the submodule and re-run the splitter to rebuild the `sections/` hierarchy:

```bash
git submodule update --remote
python3 scripts/split_spec.py
```

### 2. Update SKILL.md navigation

The section files are raw content — `SKILL.md` is the navigation layer on top.
After regenerating, review whether the thinking-verb router, use cases, or Section INDEX
in `SKILL.md` need updating to reflect new, changed, or removed content.

See **[FPF-SKILL-UPDATE-GUIDE.md](FPF-SKILL-UPDATE-GUIDE.md)** for the full
methodology: what to check, how to validate router entries, and how to run an FPF self-audit
on the skill file itself.

## Credits

- **FPF specification**: [Anatoly Levenchuk](https://github.com/ailev) — [github.com/ailev/FPF](https://github.com/ailev/FPF)
- **Skill packaging**: [CodeAlive-AI](https://github.com/CodeAlive-AI)

## License

MIT
