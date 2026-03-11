# fpf-simple-skill

AI coding agent skill for the [First Principles Framework (FPF)](https://github.com/ailev/FPF) by [Anatoly Levenchuk](https://github.com/ailev).

FPF is a transdisciplinary reasoning architecture for systems engineering, knowledge coordination, and mixed human/AI teams. This skill splits the 56,000-line FPF specification into 20 navigable sections with an INDEX that tells the agent which section to load for a given task.

## Install

```bash
npx skills add CodeAlive-AI/fpf-simple-skill -g -y
```

## Sections

| # | Section | Lines |
|---|---------|-------|
| 01 | Title page | 6 |
| 02 | Table of Content | 324 |
| 03 | Preface | 398 |
| 04 | Part A — Kernel Architecture | 5,791 |
| 05 | Cluster A.IV.A — Signature Stack & Boundary Discipline | 8,819 |
| 06 | Cluster A.V — Constitutional Principles | 8,156 |
| 07 | Part B — Trans-disciplinary Reasoning | 4,825 |
| 08 | Part C — Kernel Extensions (CALs, LOGs, CHRs) | 8,280 |
| 09 | Part D — Multi-scale Ethics & Conflict-Optimisation | 137 |
| 10 | Part E — Constitution & Authoring (header) | 2 |
| 11 | Section E-I — FPF Constitution | 6,239 |
| 12 | Part F — Unification Suite (header) | 2 |
| 13 | Cluster F.I — Context of Meaning & Raw Material | 6,150 |
| 14 | UTS Layout A — Cross-context unification table | 13 |
| 15 | UTS Layout B — Base-concept pivot | 798 |
| 16 | Part G — Discipline SoTA Patterns Kit | 6,074 |
| 17 | Part H — Glossary & Definitional Pattern Index | 9 |
| 18 | Part I — Annexes & Extended Tutorials | 10 |
| 19 | Part J — Indexes & Navigation Aids | 8 |
| 20 | Part K — Lexical Debt | 80 |

## Regenerating sections

If the upstream FPF spec changes, pull the submodule and re-run the splitter:

```bash
git submodule update --remote
python3 scripts/split_spec.py
```

## Credits

- **FPF specification**: [Anatoly Levenchuk](https://github.com/ailev) — [github.com/ailev/FPF](https://github.com/ailev/FPF)
- **Skill packaging**: [CodeAlive-AI](https://github.com/CodeAlive-AI)

## License

MIT
