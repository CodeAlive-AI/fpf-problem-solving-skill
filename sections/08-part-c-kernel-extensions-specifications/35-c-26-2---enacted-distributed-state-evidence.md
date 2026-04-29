## C.26.2 - Enacted Distributed State Evidence

> Type: Architectural pattern
> Status: Stable
> Normativity: Normative unless explicitly marked informative

### C.26.2:1 - Problem frame

Use this pattern when coordinated work, behavior, or trace patterns give evidence that a team, organization, service mesh, market, or other collective system is acting from a state that no single participant report, survey, policy sentence, dashboard, or API export faithfully carries.

The pattern supports only a weak evidence-bound claim. It lets an author say that coordinated work, behavior, or trace patterns are consistent with a distributed-state reading during a declared window, while keeping the claim tied to carriers, probes, rival explanations, and export loss.

| Working surface | Value |
| --- | --- |
| Primary reader | Architect, incident lead, organizational analyst, or manager judging whether coordinated work, behavior, or trace patterns evidence a weak collective-state reading. |
| Governed object | An evidence-bound state reading over a declared collective `U.System`. |
| Governed move | Infer only the weakest carrier/window-bound state claim, name rivals, and state export/probe limits. |
| Outside work | Group-mind ontology, survey-as-state, timeless culture claims, ordinary routine claims, and formal measurement not routed through `C.16`. |
| What changes in practice | The team can use coordinated work, behavior, or trace patterns as evidence without pretending one report faithfully exports the whole state. |

Plain glosses:
- `collective bearer`: the declared team, organization, service mesh, market slice, or other `U.System` whose coordinated work, behavior, or trace pattern is being read.
- `coordinated work/behavior`: role-work, service behavior, market participant traces, routine, commitment, artifact use, or coordinated action.
- `distributed-state reading`: a weak evidence-bound interpretation of coordinated work/behavior, not a new hidden group entity.
- `carrier`: a log, trace, artifact, commitment, routine, dashboard, report, API response, or document that grounds but does not equal the state.
- `faithful-enough export`: a representation good enough for the current decision; when it is not faithful enough, state what was lost and why.

### C.26.2:2 - Problem

Teams often need to talk about latent alignment, readiness, market posture, service-mesh behavior, or an enacted "we already decided" before one explicit representation exists. Without a pattern, they oscillate between two bad options.

One option is magic language: "the organization knows", "the culture decided", "the market wants", or "the service mesh understands". The other option is false reduction: a survey answer, policy sentence, dashboard, or report is treated as the whole state.

Both fail. Coordinated behavior may evidence a real working state, but it does not automatically identify a durable mind, internal representation, causal mechanism, or faithful-enough export for the intended use.

### C.26.2:3 - Forces

| Force | Tension |
| --- | --- |
| Work evidence vs explicit report | Coordinated work may be stronger than any one report, but the report is often the only portable carrier. |
| Weak claim vs useful claim | The pattern must say something useful without claiming group mind or durable hidden ontology. |
| Evidence vs measurement | Some cases have formal measures; many have traces, commitments, routines, and artifacts instead. |
| Export need vs export loss | The state often must be summarized for a decision, but the summary may lose the coordination that matters. |
| Primary source family vs QL lens | Distributed cognition, team cognition, routines, and socio-technical evidence are primary; QL enters only when probe/frame/export effects are load-bearing. |

### C.26.2:4 - Solution

Model the claim as evidence-bound `U.Episteme` over a declared collective `U.System`. Do not make the distributed state a bearer-independent thing. Do not treat a survey, dashboard, report, or API response as the state itself.

If the bearer is a market slice or service mesh, declare whether it is a collective `U.System`, delivery system, trace population, or evidence set. Do not infer systemhood from coordinated-looking traces alone.

The primary evidence family is coordinated work, service behavior, market participant traces, distributed cognition, routine dynamics, team cognition, work traces, and socio-technical evidence. QL enters only when probe, frame, export, incompatible read, or carrier/export structure that is not faithful enough for the declared use changes the lawful state reading.

The canonical EDSE move is to separate the factorable part from the coordination residue before making the weak state reading:

1. state what ordinary routines, policies, incentives, shared stimuli, dashboard-following, or copied artifacts explain;
2. state what the carriers show;
3. state what residue remains as a weak state reading;
4. state what action this residue supports.

Start with this recognition note:

| Mini-entry | Question |
| --- | --- |
| Collective bearer | Whose coordinated work/behavior is being read: which team, organization, service mesh, market slice, or other declared collective system? |
| Carriers / window | Which traces, artifacts, work results, commitments, dashboards, API responses, or records ground the reading, and during which window? |
| Weak state reading | What is the weakest state reading supported by the coordinated work/behavior or trace pattern? |
| Rival | Which ordinary rival explanation remains live: policy, routine, shared stimulus, dashboard-following, copied artifact, or propagation effect? |
| Practical change | What can be done now without exceeding the evidence: adjust communication, triage, routing, planning, probe design, or return to a stronger source? |

Use the fuller EDSE record below when the reading will change coordination, be reused, be contested, support evidence, or leave the immediate local discussion.

Full EDSE record:

| Field | Question |
| --- | --- |
| Collective bearer | Which declared collective `U.System` is being described? |
| Observed coordinated work / behavior / trace pattern | Which role-work, service behavior, market participant traces, routine, commitment, artifact use, or coordinated action is observed? |
| State reading | Which weak state reading is consistent with the work? |
| QL cue / formal cue if retained after ordinary work/evidence/routine explanation | Which probe, export loss, incompatible frame, compound-system decomposition, or no faithful-enough export under the declared probe/frame/use makes ordinary work/evidence wording insufficient after ordinary explanations have been tried? |
| Evidence carriers | Which logs, traces, records, commitments, artifacts, dashboards, API responses, or documents ground the reading? |
| Probe / measurement approximation | Which survey, dashboard, API read, interview, trace query, metric, or publication approximates the state, and how may that probe change, thin, or frame the state reading? |
| Attempted export / faithful-enough criterion | What export was attempted, and what would count as faithful enough for the current decision? |
| Loss cause / stronger export | Why is the current export not faithful enough, and could a stronger probe, bridge, representation, or time window produce a stronger export? |
| Time window | During which window does the claim hold? |
| Persistence strength | Is the reading momentary, recurring, stabilized for the incident/release/window, or expected to persist under stated conditions? |
| Decay / refresh condition | What would make the reading expire, refresh, weaken, or need a new probe? |
| Reprobe cost | What does it cost in time, risk, disruption, attention, coordination, privacy, or evidence quality to check again? |
| Rival explanation not ruled out | Which ordinary explanation remains possible? |
| Weakest supported claim | What may be said without exceeding the evidence, carrier set, time window, or export limit? |
| Supported action / use | Which planning, communication, incident, routing, bridge, evidence, or decision move may now be taken without exceeding the claim? |

#### C.26.2:4.1 - Minimal claim principle

Preferred wording stays close to observed work:

- "During window W, the incident-response organization acted consistently with a rollback-readiness posture, evidenced by release timing, escalation criteria, and shared trace use."
- "The service mesh exhibited a coordinated throttling regime under policy P, evidenced by route changes and saturation traces."
- "Market traces support an expectation-shift claim under probe Q, with media amplification still a rival explanation."

Avoid stronger wording such as "the organization decided", "the market knows", or "the team has a distributed mind" unless another FPF pattern and evidence burden independently support it.

#### C.26.2:4.2 - Finish conditions

This pattern emits one of these results:

| Result | Meaning |
| --- | --- |
| Weak evidence-bound state assertion | State the collective bearer, observed coordinated work/behavior/trace pattern, carriers, time window, confidence/assurance posture, rivals, and export limit. |
| Export-loss repair | Keep the state reading weak and add a bridge/publication note about what the attempted report, survey, API response, dashboard, or policy sentence lost. |
| Probe-coupled reroute | Route to `C.26.1` when the survey work, dashboard publication/use, interview, API operation, or publication act changed the state being evidenced. |
| Measurement/evidence reroute | Route to `C.16`, `A.10`, or `B.3` when the main burden is scale, method, evidence, assurance, or audit posture. |
| Work/authority reroute | Route to `A.15` or the relevant authority/work pattern when a command, routine, incentive, or playbook explains the coordination without remaining export/probe burden. |
| No EDSE claim | Drop the distributed-state wording when the carriers, window, rivals, or weak supported output cannot be stated. |

#### C.26.2:4.3 - Rival explanation rule

Before using this pattern, name the strongest ordinary rivals:

| Rival | Repair |
| --- | --- |
| Policy, command, coercion, or management pressure | Route to work/authority claims unless export/probe loss remains live. |
| Shared incentive or common external stimulus | Keep the claim as parallel response if that explains the coordination. |
| Routine, habit, script, or playbook | State the routine; avoid stronger current-state wording. |
| Dashboard-following, metric gaming, or social desirability | Route probe-caused change through `C.26.1` and evidence patterns. |
| Copied artifact, template, policy sentence, or API response | Use `F.9`, E.17 publication, or bridge loss before EDSE. |
| Diffusion, contagion, media amplification, or signaling | Use the appropriate propagation/evidence route and keep only the remaining work-enacted state claim. |

#### C.26.2:4.4 - Export-loss discipline

The phrase "not faithfully exportable under current probe and bridge conditions" is supported only when the text says:

- what export was attempted;
- what would have counted as faithful enough for the current decision;
- what state, coordination, evidence path, timing, role alignment, option structure, survivor relation, or use limit was lost;
- whether the loss comes from bridge, measurement, representation, audience, timing, state change, or another cause;
- whether a stronger probe, bridge, representation, or time window could produce a stronger export.

#### C.26.2:4.5 - Compound-state decomposition card

When the distributed-state reading is load-bearing, state the decomposition explicitly. Its practical purpose is the canonical EDSE move: ordinary rivals first, carriers second, coordination residue third, supported action/use fourth.

| Field | Question |
| --- | --- |
| Whole system | Which collective `U.System` is being read, and under what boundary? |
| Subsystems | Which teams, roles, services, markets, routines, artifacts, or work lanes are locally readable? |
| Local state readings | What can be said about each part without inventing a shared inner representation? |
| Correlation / coordination evidence | Which traces, timing, work transfers, commitments, artifact uses, or role-work alignments show coordination? |
| Factorable part | Which part of the behavior is explained by policy, routine, shared stimulus, incentive, dashboard following, or copied artifact? |
| Coordination residue | What remains as a weak distributed-state reading after the ordinary rival explanations are named? |
| Weakest supported claim | What evidence-bound claim survives for the declared time window and carrier set? |
| Supported action / use | Which planning, communication, incident, routing, bridge, evidence, or decision move may now be taken without exceeding that weak claim? |

#### C.26.2:4.6 - Governed object and claim floor

The governed object is an evidence-bound `U.Episteme` reading over coordinated work, behavior, or trace patterns by a declared collective `U.System`. The pattern does not govern an inner group entity, a culture substance, a market mind, a hidden service intelligence, or a reusable kernel state kind.

The governed move is to turn coordinated work, behavior, or trace patterns into the weakest useful state reading while keeping the reading bound to:

- the collective bearer and its boundary;
- the observed work and evidence carriers;
- the time window and persistence strength;
- the probe or export conditions;
- the ordinary rival explanations;
- the current export loss and stronger-export possibility;
- the next neighboring FPF pattern if a stronger claim is needed.

This pattern is useful because many real work states are enacted before they are articulable. A team may behave as if a release freeze exists before any single person states it cleanly. A service mesh may exhibit one routing posture before any one dashboard carries the whole situation. A market may shift expectations before any one survey faithfully exports the shift. The pattern lets FPF say that much, and no more, without pretending that one carrier is the state.

#### C.26.2:4.7 - Operational evidence sequence

Action path:

1. Name the collective bearer as a declared `U.System` boundary, not a bare social label.
2. Name the coordinated work/behavior/trace pattern being read through `A.15`: actions, routines, commitments, role-work, service behavior, market participant traces, artifacts, or timing.
3. Name the evidence carriers through `A.10` so the reading is inspectable.
4. State the time window, persistence strength, decay/refresh condition, reprobe cost, and ordinary rival explanations.
5. Name the candidate state reading only as a weak evidence-bound `U.Episteme` reading.
6. State the attempted export and what it lost.
7. State the weakest supported claim, the supported action/use it carries now, and the stronger uses that remain unsupported by this reading.
8. Add `B.3` assurance only when consequence level, audit, release, or accountability use demands it.

Output contract: produce a weak evidence-bound distributed-state reading, the time window that bounds it, the live rival explanations, and the supported bounded action/use that follows from that reading.

The pass is complete only when the resulting sentence can survive without magical collective wording. A good output sounds like:

> During incident window W, the incident-response organization acted consistently with rollback-readiness posture P, evidenced by deployment queue changes, escalation messages, rollback artifacts, and support-routing changes; this reading is not faithfully exported by survey S because S loses timing, role-work, and trace linkage.

That sentence is weaker than "the organization decided", but it is much more useful. It supports adjusting incident communication and release-triage posture during window W; it does not support a durable culture claim or release-readiness assurance claim.

#### C.26.2:4.8 - Well-formed EDSE record

A usable EDSE record has this shape:

```text
EnactedDistributedStateEvidence(
  collectiveBearer = ...,
  boundary = ...,
  observedCoordinatedWork = ...,
  evidenceCarriers = ...,
  probeOrExport = ...,
  timeWindow = ...,
  persistenceStrength = ...,
  ordinaryRivals = ...,
  factorablePart = ...,
  coordinationResidue = ...,
  exportLoss = ...,
  weakestSupportedClaim = ...,
  boundedActionSupported = ...,
  unsupportedUse = ...
)
```

The syntax is illustrative. The content is not optional when the state reading is used for a decision.

Well-formedness constraints:

- `collectiveBearer` is a declared collective system, not a metaphorical subject.
- `evidenceCarriers` are inspectable artifacts, traces, records, commitments, logs, or work products.
- `timeWindow` bounds the claim; persistence beyond that window needs its own support.
- `ordinaryRivals` include at least the strongest policy, incentive, routine, shared stimulus, dashboard-following, copied-artifact, or social-desirability explanation that could explain the same coordination.
- `weakestSupportedClaim` states only what survives after rivals and export loss are named.
- `unsupportedUse` names what the current claim does not support without another pattern.

#### C.26.2:4.9 - Carrier, probe, report, and state split

The pattern keeps four objects separate:

| Object | Role in the claim |
| --- | --- |
| Enacted work | What people, services, routines, artifacts, or market participants actually did in coordination. |
| Evidence carrier | The log, trace, ticket, meeting note, deployment record, dashboard export, report, API response, or policy text that makes some part of the work inspectable. |
| Probe / approximation | The survey, dashboard query, interview, trace query, report request, metric, or publication act that frames the state reading. |
| Distributed-state reading | The weak `U.Episteme` claim inferred from coordinated work/behavior under carriers, window, rivals, and export limits. |

A survey can be an evidence carrier and a probe. It is not the distributed state. A policy can be a carrier or a routine explanation. It is not automatically evidence that everyone shares one state. A dashboard can be a carrier, a probe, and a behavior-changing instrument. It is not automatically faithful enough for the intended use.

#### C.26.2:4.10 - Case bank and near misses

| Case | Supported C.26.2 reading | Near miss / reroute |
| --- | --- | --- |
| Incident release freeze | Teams stop releases, prepare rollback evidence, reroute support, and change escalation before a written decision appears. | If a manager issued a clear command and the work merely followed it, use work/authority patterns and evidence, not EDSE. |
| Service-mesh throttling regime | Route changes, saturation traces, retry patterns, and on-call routines show a coordinated throttling state under policy P. | If one controller rule fully explains the behavior, state the rule and use ordinary system/dynamics evidence. |
| Market expectation shift | Pricing, support inquiries, partner messages, and risk notes move together after a public signal. | If media amplification or common stimulus explains the movement, keep only that propagation/evidence claim. |
| Team "already decided" posture | Backlog changes, review comments, and role assignments show that the team is acting under an unstated decision. | If the claim is only a vibe or a few statements, do not use EDSE; gather carriers or keep it as informal observation. |
| Survey of culture | Survey answers conflict, but work traces show a stable escalation habit. | Treat the survey as a probe and possible export loss; do not make it the state itself. |
| Dashboard-following organization | Teams coordinate around the public metric after the metric becomes visible. | Route probe-caused change through `C.26.1`; EDSE may carry only the residual coordinated-state reading. |

#### C.26.2:4.11 - Evidence posture and confidence

EDSE claims become useful when the text says how much consequence the evidence can carry.

| Evidence posture | Supported use | Additional burden |
| --- | --- | --- |
| `QLP-0` recognition | Flag a possible enacted state for discussion or triage. | Name bearer, work, carriers, and time window. |
| `QLP-1` local working use | Adjust local planning, incident response, or communication. | Add rivals, export loss, persistence, and reprobe condition. |
| `QLP-2` decision-bearing / reusable use | Publish as a repeatable example or internal practice, or let the reading change a bounded decision. | Add case comparison, near misses, and evidence-carrier discipline. |
| `QLP-3` assurance / reusable-law use | Use for release, audit, legal, accountability, reusable-law, or high-impact allocation. | Route through `A.10`, `B.3`, `C.16`, and the relevant authority/work patterns. |

For `QLP-0` or low-consequence `QLP-1`, do not force persistence, decay, or reprobe-cost fields when the claim is explicitly momentary and the bounded action is local. Name the bearer, carriers/window, weak reading, rival, practical change, and local stop; add the fuller temporal fields only when reuse, contest, or consequence makes them load-bearing.

The ordinary EDSE claim is weak but actionable. It says: "this coordinated work/behavior supports this bounded reading for this use." It does not say: "the collective has one hidden durable state that a report can copy."

### C.26.2:5 - Archetypal Grounding


Tell: During an incident, several teams independently stop non-critical releases, reroute support, and prepare rollback evidence before any single manager issues a written decision. Later, a survey asks whether "we had decided to freeze release", and answers conflict.

Show, System side: the collective bearer is the incident-response organization during a declared incident window. Its carriers include deployment logs, meeting records, escalation messages, rollback preparation, support routing, and release queue changes.

Show, Episteme side: the supported claim is weak. The organization acted consistently with a release-freeze readiness posture during window W. The claim does not say every participant knew the same proposition or that the coordination exists apart from the declared evidence carriers. A management directive, playbook, or dashboard effect remains a rival unless evidence narrows it.

### C.26.2:6 - Bias-Annotation

This pattern biases authors toward weak claims and explicit evidence. That may feel conservative, but it makes distributed-state language usable without magic.

It also biases authors to keep primary grounding in distributed cognition, team cognition, organizational routines, socio-technical work, and evidence practice. The QL lens is secondary and only becomes active when probing, exporting, or comparing the state changes or loses load-bearing structure.

### C.26.2:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-C26.2.1 | The collective bearer is a declared `U.System` or collective system, not a bare group label. |
| CC-C26.2.2 | Observed coordinated work / behavior / trace pattern is named. |
| CC-C26.2.3 | Evidence carriers and time window are named. |
| CC-C26.2.4 | The QL cue / formal cue is named if QL wording is retained. |
| CC-C26.2.5 | Persistence strength, decay/refresh condition, and reprobe cost are named when the claim is not momentary. |
| CC-C26.2.6 | The weakest supported claim is stated. |
| CC-C26.2.7 | At least one strong ordinary rival explanation is named. |
| CC-C26.2.8 | The compound-state decomposition separates whole system, subsystems, local readings, factorable part, and coordination residue when the distributed-state reading is load-bearing. |
| CC-C26.2.9 | Any survey, dashboard, report, API response, or policy sentence is typed as representation, carrier, or export, not as the distributed state itself. |
| CC-C26.2.10 | Probe / measurement approximation, attempted export, faithful-enough criterion, loss cause, and stronger-export possibility are stated when export or measurement carries the claim. |
| CC-C26.2.11 | Export loss is stated when the claim depends on export that is not faithful enough for the declared use. |
| CC-C26.2.12 | The evidence posture is stated when the claim is reused, contested, or higher consequence. |
| CC-C26.2.13 | Formal measurement routes to `C.16`; evidence and assurance route to `A.10` / `B.3`; bridge loss routes to `F.9`. |
| CC-C26.2.14 | The pattern inherits `QL-NQ` from `C.26` and does not mint `U.DistributedState`. |

### C.26.2:8 - Common Anti-Patterns and How to Avoid Them


| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Group mind claim | The text says the team, market, service, or organization knows or wants something. | Rewrite as an evidence-bound state reading over a collective bearer during a window. |
| Survey-as-state | A survey answer is treated as the distributed state. | Treat the survey as probe/output/evidence carrier and ask what it lost or changed. |
| Tacit skill overreach | A craft skill or team vibe is called distributed state. | Require coordinated work, carriers, time window, and rival explanations. |
| Routine mistaken for state | A playbook explains the action, but the text claims latent alignment. | Name the routine and keep the stronger claim out. |
| Timeless culture | A momentary observation becomes a durable culture claim. | State window, persistence strength, decay, and reprobe condition. |

### C.26.2:9 - Consequences

This pattern lets FPF discuss enacted collective states without mysticism. It gives authors a disciplined way to use traces, routines, coordinated work, and export loss in one weak claim.

The cost is that many attractive claims become weaker. That is the point. Weak evidence-bound claims are often more useful than confident but ungrounded stories.

### C.26.2:10 - Rationale

Existing FPF patterns can carry parts of the burden, but no single ordinary pattern makes the combined weak distributed-state claim easy to write. `A.15` carries work, `A.10` / `B.3` carry evidence and assurance, `F.9` carries export loss, and `C.16` carries formal measurement. C.26.2 coordinates those routes for the specific case where coordinated work evidences a non-articulated state.

### C.26.2:11 - SoTA-Echoing

| Pattern claim | Practice / source | Pattern implication | Adoption stance |
| --- | --- | --- | --- |
| Coordinated work can evidence state-like organization without reducing that state to one participant report. | [Representing distributed cognition in socio-technical systems](https://www.sciencedirect.com/science/article/abs/pii/S2405896316321164), team cognition, shared mental models, transactive memory, [organizational routine dynamics resources](https://routines.broad.msu.edu/resources), work traces, and socio-technical systems. | Make these the primary grounding; infer only weak evidence-bound state readings from carriers, traces, and work. | Adapt as primary non-QL grounding. |

| Probe/export conditions can change or thin the state reading. | [Quantum-like modeling in biology with open quantum systems and instruments](https://www.sciencedirect.com/science/article/pii/S0303264720301994) / [arXiv](https://arxiv.org/abs/2010.15573) and [Open Systems, Quantum Probability, and Logic for Quantum-like Modeling in Biology, Cognition, and Decision-Making](https://www.mdpi.com/1099-4300/25/6/886). | Activate QL only when probing, formalizing, exporting, or bridging changes or loses load-bearing structure. | Adapt as secondary modeling support. |
| Contextual judgment and previous judgments can alter the state being reported. | [Quantum Cognition](https://www.annualreviews.org/content/journals/10.1146/annurev-psych-033020-123501). | Treat surveys, interviews, reports, and dashboards as possible probes of enacted state, not faithful copies by default. | Use as probe/export caution with ordinary evidence routes. |
| Some sequential data can be carried by classical instrument models. | [Quantum-like Cognition in Process Theories: An Analysis](https://arxiv.org/abs/2604.08604). | Keep non-necessity visible: EDSE is a useful FPF evidence pattern, not proof that only QL formalism works. | Use as rival-model discipline. |
| Carrier plurality is normal in operational evidence. | Observability, incident-management, audit, work-trace, and assurance practice. | Use logs, traces, dashboards, meeting records, commitments, artifacts, and operational changes as carriers, not as faithful copies of the whole state. | Adopt through `A.10` / `B.3` routes. |

Worked-slice discipline from these rows:

- ground the claim in coordinated work before QL vocabulary appears;
- state the evidence carriers and time window before stating the state reading;
- name rivals before retaining a distributed-state claim;
- treat survey/report/dashboard outputs as carriers or probes, not as the state;
- escalate to measurement, evidence, assurance, or authority patterns when the use becomes stronger.

### C.26.2:12 - Relations


- Builds on: `C.26`, `A.15`, `A.10`, `B.3`, `F.9`, `C.16`, `E.17.EFP`, `C.11`.
- Coordinates with: `C.26.1` when the probe changes the state being evidenced; `C.26.3` when the coordinated state is part of viability-envelope regulation.
- Does not mint: `U.DistributedState`, a bearer-independent group entity, or a durable state beyond declared evidence and time window.
- Name posture: `Enacted Distributed State Evidence` names an evidence-bound `U.Episteme` reading over work carriers, not `Distributed Mind`, `Collective Consciousness`, `Social Field`, or `Organization Knows`.

### C.26.2:End
