## A.15 - Role–Method–Work Alignment (Contextual Enactment)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** This pattern is the entry-bearing alignment pattern for engineer-managers when the real confusion is not "what component is this" but `who is responsible`, `how the work is supposed to happen`, `when the plan lives`, and `what actually happened`.

**Use this when.** Use this pattern when the real job is to separate role, method, plan, capability, and actual work before a team treats one cue, one schedule, or one document as if it already counted as execution or authority.
**Start here when.** The dominant ambiguity is role vs method vs schedule vs actual run, and the team keeps arguing about a "process" without separating recipe, plan, capability, and executed work.

**First output.** One explicit Role / Method / MethodDescription / WorkPlan / Work separation, plus one traceable chain from `U.RoleAssignment` through the governing method description to the actual or intended work record.
**Governed object in plain terms.** One alignment frame linking `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` through `U.RoleAssignment`; not a single work occurrence, not a checklist, and not a mere cue note.
**Governing move in plain terms.** Keep design-time role/method/plan distinct from run-time work while making the chain between them inspectable enough for enactment, audit, and reroute.
**What goes wrong if missed.** Teams collapse role, recipe, plan, capability, and actual run into one fuzzy "process" story, then mistake documentation for execution, capability for evidence, or a weaker briefing for executable authority.
**What this buys.** One inspectable enactment frame that lets a team ask who held what role, which method governed, what plan existed, and what work actually occurred before taking action, blame, or approval as if those layers were the same.
**Not this pattern when.** Not this pattern when the honest need is only one dated work occurrence (`A.15.1`), only planning or schedule baseline (`A.15.2`), or only a cue note that has not yet become an enactment-alignment question (`A.16` / `A.16.1`).

**Typical next patterns.** `A.15.1` for dated execution, `A.15.2` for schedule/baseline planning, `A.15.3` for slot-filling plan items, `B.5.1` for the simple lifecycle reading, `F.11` when method/work vocabulary itself must be aligned across contexts, and `F.17` when the result should land on a human-facing work sheet.

**Common wrong escalations / reroutes.** If the first honest artefact is still only a cue, reroute to `A.16` / `A.16.1`; if the problem is boundary language or contract soup, reroute to `A.6`; if you only need one executed occurrence rather than the alignment frame, continue straight to `A.15.1`.

**Boundary to weakened renderings.** A lighter briefing, summary, redacted note, or coarsened rendering may help orient work or cue attention, but it does not become a sufficient action cue, implementation checklist, work plan, work occurrence, approval, gate, or execution authority by convenience alone. If a weaker rendering needs return to a stronger source before work can lawfully proceed, keep that boundary explicit here and use `A.6.3.CSC Controlled Semantic Coarsening` for the weaker-source relation rather than treating the weakened rendering as executable.
**Recognition vs assurance note.** Read **At a glance**, **Start here when**, **First output**, the reroutes, and the weakened-rendering boundary above as the ordinary recognition block. Read the entity distinctions, canonical relations, checklist, and relations below as assurance blocks that tighten that same alignment-frame claim; they do not widen the pattern into one single work occurrence, one cue note, or one undifferentiated "process" object.

### A.15:1 - Problem frame

In any complex system, from a software project to a biological cell, there is a fundamental distinction between **what something is** (its structure), **what it is supposed to do** (its role and specified capability), and **what it actually does** (its work). Confusing these layers is a primary source of design flaws, budget overruns, and failed projects. Teams argue about a "process" without clarifying if they mean the documented procedure, the team's ability to execute it, or a specific execution that happened last Tuesday.

This pattern provides the canonical alignment for modeling contextual enactment in FPF, serving as the ultimate implementation of the **Strict Distinction Principle (A.7)**. It weaves together several foundational concepts into a single, coherent model of how intention becomes action:
*   **A.2 (Contextual Role Assignment):** Provides the `Holder#Role:Context` structure for assigning roles.
*   **A.4 (Temporal Duality):** Provides the strict separation between `design-time` and `run-time`.
*   **A.12 (External Transformer):** Ensures that all actions are attributed to an external agent.

The intent of this pattern is to establish a normative, unambiguous vocabulary and set of relations for describing the entire evolution of an action, from the specification of a capability to its concrete, resource-consuming execution.

To keep plan-run separation explicit, this pattern references **A.15.2 `U.WorkPlan`** for **schedules/calendars** and **A.15.1 `U.Work`** for **dated execution**. Ambiguous terms like "process / workflow / schedule" are constrained by **L-PROC / L-FUNC / L-SCHED** (E-cluster): a _workflow_ is a **Method/MethodDescription**, a _schedule_ is a **WorkPlan**, and what _happened_ is **Work**.

**Terminology note (L-ACT).** The words _action/activity_ are **not normative** in the kernel. When a generic "doing" is needed, we use the didactic term **enactment** (not a type). Normative references must be to **`U.Method` / `U.MethodDescription` / `U.Work` / `U.WorkPlan`**. See lexical rules **L-PROC / L-FUNC / L-SCHED / L-ACT**.

### A.15:2 - Problem

Without this formal framework, models suffer from a cascade of category errors:

1.  **Role-as-Part:** A Role (e.g., `AuditorRole`) is incorrectly placed inside a structural bill-of-materials (`ComponentOf`), making the system's architecture brittle and nonsensical.
2.  **Specification-as-Execution:** A `MethodDescription` (the "recipe") is treated as evidence that the work was done. This leads to "paper compliance," where a system is considered complete simply because its documentation exists.
3.  **Capability-as-Work:** A team's *ability* to perform a task (`Capability`) is conflated with the *actual performance* of that task (`Work`). This obscures the reality of resource consumption and actual outcomes.
4.  **Work-without-Context:** An instance of work is logged without a clear link back to the role, capability, and specification that governed it, making the work unauditable and its results impossible to reproduce.
5.  **Ambiguous "Process/Activity":** The overloaded term "process" is used indiscriminately to refer to all of the above, creating a fog of miscommunication that paralyzes decision-making. Activity/action terms must be resolved via L-ACT to Method/MethodDescription (recipe), WorkPlan (schedule), or Work (run).

### A.15:3 - Forces

| Force | Tension |
| :--- | :--- |
| **Structure vs. Function** | The need to model the stable, physical structure of a system (`mereology`) vs. the need to model its dynamic, functional behavior (`roles` and `actions`). |
| **Design vs. Run** | The need for a timeless, reusable description of a capability (`design-time`) vs. the need for a specific, dated record of its execution (`run-time`). |
| **Clarity vs. Jargon** | The need for a precise, formal vocabulary to prevent ambiguity vs. the reality that teams use informal, domain-specific jargon like "process" or "workflow." |
| **Accountability vs. Complexity** | The need for a complete, end-to-end audit trail for every action vs. the desire to keep models simple and avoid excessive documentation. |

### A.15:4 - Solution
The solution is a stratified alignment that cleanly separates the `design-time` and `run-time` for contextual **enactment**. The linking relation between these worlds is the **`U.RoleAssignment`**.

#### A.15:4.1 - The Core Entities: A Strict Distinction

FPF mandates the use of the following distinct, non-overlapping entities to model action. Using them interchangeably is a conformance violation.

**A) Design-Time Entities (The World of Potential):**

*   **`U.Role`:** A contextual "mask" or "job title" (e.g., `TesterRole`). It specifies a function but is not the function itself.
*   **`U.Method`:** The **abstract way-of-doing** inside a context (paradigm-agnostic; may be imperative, functional, logical, or hybrid).
*   **`U.MethodDescription`:** A **`U.Episteme` describing a `U.Method`** (the SOP/algorithm/proof/recipe on a carrier).
*   **`U.Capability`:** An **attribute** of a `U.System` that represents its **ability** to perform the actions described in a `MethodDescription`. This is the "skill" or "know-how."
*   **`U.WorkPlan`:** An **`U.Episteme`** declaring **intended `U.Work` occurrences** (windows, dependencies, intended performers as role kinds, budgets) - see **A.15.2**.

**B) The Bridge Entity:**
*   **`U.RoleAssignment`:** The formal assertion `Holder#Role:Context` that links a specific `U.Holon` to a `U.Role` within a `U.BoundedContext`. This holder-to-role assignment link is what "activates" the requirements associated with a role.

**C) Run-Time Entity (The World of Actuality):**

*   **`U.Work`:** An **occurrence** or **event**. It is the concrete, dated, resource-consuming **execution of a `U.MethodDescription`** by a `Holder` acting under a `U.RoleAssignment`; capability checks are evaluated at run time against the holder. This is the only entity that has a start and end time and consumes resources.

**Kinds of Work and the primary target**

**Well-formedness constraint A15-WF-1 (work target and kind).** A `U.Work` occurrence has `primaryTarget: U.Holon` with cardinality `1..1 (total)` and `kind` with cardinality `1..1 (total)`.

Local `kind` values used here:
* Operational - transforms a `U.System` or its environment.
* Communicative (SpeechAct) - transforms a deontic/organizational frame (e.g., commitments, authority states, approvals).
* Epistemic - transforms a `U.Episteme` (e.g., curating a dataset).
The `primaryTarget` disambiguates enactment: what is being acted upon. Example: an approval is `kind=Communicative`, `primaryTarget = Commitment(change=4711)`. A deployment is `kind=Operational`, `primaryTarget = ServiceInstance(prod-us-eu-1)`.

**Didactic Note for Managers: The "Chef" Analogy**

This model can be easily understood using the analogy of a chef in a restaurant.

*   **`ChefRole`** is the **Role**. It's a job title with certain expectations.
*   A **Cookbook (`U.MethodDescription`)** contains the **recipe** for a Souffle. It's a piece of knowledge.
*   The chef's **skill** in making souffles is their **`U.Capability`**. They have this skill even when they are not cooking.
*   The restaurant's rulebook (`U.BoundedContext`) states that anyone in the `ChefRole` *must* have the `Capability` to follow the recipes in the cookbook.
*   The actual act of **making a souffle** on Tuesday evening - using eggs and butter, taking 25 minutes, and consuming gas - is the **`U.Work`**.

Confusing these is like mistaking the cookbook for the souffle. FPF's framework simply makes these common-sense distinctions formal and mandatory.

#### A.15:4.2 - The Canonical Relations: Connecting the Layers

The entities are connected by a set of precise, normative relations that form an unbreakable causal chain. The following diagram illustrates this flow from the abstract context down to the concrete execution.

```mermaid
graph TD
    subgraph Design-Time Scope (Tᴰ)
        A[U.BoundedContext] -- defines --> B(U.Role)
        M[U.Method] -- isDescribedBy --> D[U.MethodDescription]
        Cap[U.Capability] -- supports --> M
        H(U.System as Holder) --> RB(U.RoleAssignment)
        B -- is the role in --> RB
        A -- is the context for --> RB
        A -- bindsCapability(Role,Capability) --> Cap
    end

    subgraph Run-Time Scope (Tᴿ)
        W[U.Work]
    end

    RB -- performedBy --> W
    W  -- isExecutionOf --> D

    style A fill:#e6f3ff,stroke:#36c,stroke-width:2px
    style B fill:#fff2cc,stroke:#d6b656,stroke-width:2px
    style Cap fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    style M fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    style D fill:#f8cecc,stroke:#b85450,stroke-width:2px
    style H fill:#e1d5e7,stroke:#9673a6,stroke-width:2px
    style RB fill:#dae8fc,stroke:#6c8ebf,stroke-width:3px,stroke-dasharray: 5 5
    style W fill:#ffe6cc,stroke:#d79b00,stroke-width:2px,font-weight:bold
```

*   **`bindsCapability(Role, Capability)`:** A `U.BoundedContext` asserts that a given `Role` requires a specific `Capability`. This is a `design-time` rule.
*   **`isDescribedBy(Method, MethodDescription)`:** A `U.Method` is formally described by one or more `MethodDescription`s. This links the abstract way-of-doing to the recipe on a carrier.
*   **`isExecutionOf(Work, MethodDescription)`:** A specific `U.Work` is a `run-time` realization of a `design-time` `MethodDescription`. Capability checks are evaluated against the holder at run time.
*   **`performedBy(Work, RoleAssignment)`:** A `U.Work` is always performed by a specific `Agent` (a `U.RoleAssignment`). This links the action to the actor-in-context.

_At run time, capability thresholds declared by the context/spec are **checked** against the holder; `U.Work` outcomes provide **evidence** for capability conformance._

This chain provides complete traceability: a specific instance of `U.Work` can be traced back to the `U.MethodDescription` that governed it, the `U.Method` it describes, and the `Agent` (`Holder` + `Role` + `Context`) that was authorized and responsible for its execution.

#### A.15:4.3 - Bounded specialization scouting and `CheckpointReturn`

When a human-guided agentic work system faces a new task family or candidate solution corridor, the governed work may temporarily separate utility ownership, exploratory scouting, bounded specialist probing, and commit authority into distinct enactment roles. The payoff is faster lawful specialization of the next move, not disappearance of the human decision point.

For this bounded scouting case, the work system should declare one utility target first, enumerate heterogeneous candidate approaches that may satisfy that target, spend a bounded scout or probe budget before any committed route is chosen, and return one `CheckpointReturn` that compares the tested approaches rather than silently treating one successful probe as a committed rollout. `A.15` owns this enactment-role split only; it does not re-own the checkpoint-record semantics of `C.24` or the budget/guard enforcement of `E.16`. This scouting subsection is not a controlled semantic coarsening case unless a returned briefing or summary is itself being treated as weaker-source authority.

Every `CheckpointReturn` should carry:
- the declared utility target and current `TaskFamily`
- the candidate approaches actually tested
- the evidence observed on each tested approach, including progress toward the named work-measure threshold and important failure signals
- the budget already burned and the residual budget still available
- the recommended next action: continue probing, commit, narrow, hand off, or stop
- the exact commit trigger that would justify leaving the probe state

Low-human-overlap approaches remain admissible here only while they stay tied to the declared utility target, budget guard rails, and evidence basis by value.
### A.15:5 - Archetypal Grounding

The Contextual Action Framework is universal. It applies identically to the modeling of physical engineering processes, knowledge work, and socio-technical systems.

| Archetype | **`U.System` Archetype (Manufacturing)** | **`U.Episteme` Archetype (Scientific Peer Review)** |
| :--- | :--- | :--- |
| **`BoundedContext`** | `FactoryFloor:ProductionLine_B` | `Journal:PhysicsLetters_A` |
| **`Role`** | `WeldingRobotRole` | `ReviewerRole` |
| **`Holder`** | `ABB_Robot_Model_IRB_6700` (`U.System`) | `Dr_Alice_Smith` (modeled as a `U.System`) |
| **`U.RoleAssignment`** | `ABB_Robot#WeldingRobotRole:Line_B` | `Dr_Smith#ReviewerRole:PhysicsLetters_A` |
| **`MethodDescription` (`U.Episteme`)** | `Welding_Procedure_WP-28A.pdf` (SOP) | `Peer_Review_Guidelines_v3.docx` |
| **`Capability` (Attribute of Holder)** | `executeWeldingSeam(Type: 3F)` | `evaluateManuscript(Field: QuantumOptics)` |
| **`Work` (`Occurrence`)** | Manufacturing Work: `Weld_Job_#78345` (15:32-15:34 UTC, consumed 1.2 kWh, 5g Argon) - **isExecutionOf** `Welding_Procedure_WP-28A.pdf` | Peer-review Work: `Review_of_Manuscript_#PL-2025-018` (Completed 2025-08-15, took 4 hours) - **isExecutionOf** `Peer_Review_Guidelines_v3.docx` |

**Key takeaway from grounding:**
This side-by-side comparison reveals the power of the framework. A seemingly different activity like welding a car chassis and reviewing a scientific paper are shown to have the **exact same underlying causal structure**. Both involve a `Holder` (a system) acting in a `Role` within a `Context`, using a `Capability` described by a `MethodDescription` to produce a specific, auditable instance of `Work`. This universality is what allows FPF to compare and align disparate domains without collapsing their local structure.

#### A.15:5.1.a - Briefing is not execution authority
**Source set.** A release team has one governing deployment method description, one current work plan, one approval work item, and the evidence-bearing materials used to decide whether the rollout may proceed. A short rollout briefing is prepared for the daily stand-up.

**Briefing slice.** `Status briefing only: rollback path appears verified in the current source bundle. Deployment authority remains with the governing approval record and work plan.`

This briefing may orient the team and cue attention, but it is not the governing execution authority by itself. Lawful work still depends on the underlying method description, current work plan, and any required approval records or evidence-bearing materials staying explicit and reopenable. If the team wants to treat the briefing as sufficient to execute, the case leaves simple orientation and must reopen the stronger governing materials rather than treating the shortened note as the work-enactment authority.

### A.15:6 - Bias-Annotation


Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for contextual enactment across engineering, operational, and knowledge-work settings.

Bias risks and mitigations:

* **Governance bias (Gov):** teams may over-treat role or approval records as enough evidence that work happened.
  *Mitigation:* keep `U.RoleAssignment`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` distinct, and let only `U.Work` carry actuals and resource use.
* **Architectural bias (Arch):** modelers may pull roles or capabilities into structural part hierarchies because those diagrams are already present.
  *Mitigation:* preserve role and capability as contextual-functional entities, not parts.
* **Epistemic bias (Onto/Epist):** a documented recipe or schedule can be mistaken for proof of execution.
  *Mitigation:* require the traceability chain from `U.RoleAssignment` and `U.MethodDescription` to dated `U.Work`.
* **Pragmatic bias (Prag):** teams may keep using one overloaded "process" word because it feels faster.
  *Mitigation:* resolve "workflow / schedule / what happened" through `U.Method` / `U.MethodDescription`, `U.WorkPlan`, and `U.Work`.
* **Didactic bias (Did):** the chef analogy can make the pattern seem intuitive while hiding the need for explicit model links.
  *Mitigation:* pair the analogy with the canonical relations and checklist.

### A.15:7 - Conformance Checklist

To ensure the integrity of action modeling, all FPF-compliant models must adhere to the following normative checks.

| ID | Requirement (Normative Predicate) | Purpose / Rationale |
| :--- | :--- | :--- |
| **CC-A15-1 (Entity Distinction)** | The entities `U.Role`, **`U.Method`**, **`U.MethodDescription`**, `U.Capability`, **`U.WorkPlan`**, and `U.Work` **MUST** be modeled as distinct, non-overlapping types. | This is the core enforcement of **Strict Distinction (A.7)**. It prevents the category errors outlined in the "Problem" section. |
| **CC-A15-1a (Work target/kind predicate)** | A conforming `U.Work` record SHALL satisfy `A15-WF-1`; validators SHOULD report missing `primaryTarget` or missing `kind` as an invalid work record. | Keeps target and work kind enforceable as artifact validity without stating modeled-world admissibility through a free RFC sentence. |
| **CC-A15-2 (Temporal Scope)** | `U.Method`/`U.MethodDescription`/`U.WorkPlan` exist in **design-time**; `U.Work` exists in **run-time**. Design artifacts are not mutated by operational events. | Enforces **Temporal Duality (A.4)**. Blueprints cannot be mutated by operational events. |
| **CC-A15-3 (RoleAssignment Mandate)** | Every `U.Work` **MUST** be linked via `performedBy` to a valid `U.RoleAssignment`. | Guarantees that every action has a clearly identified, context-bound actor, ensuring accountability. |
| **CC-A15-4 (Traceability Chain)** | For every `U.Work`, an unbroken chain **MUST** exist: `Work -performedBy-> RoleAssignment` and `Work -isExecutionOf-> MethodDescription -describes-> Method`. Capability checks are evaluated against the holder at run time. | Ensures end-to-end auditability from a specific action back to the recipe that governed it. |
| **CC-A15-5 (No Roles in Mereology)** | A `U.Role` or `U.Capability` **SHALL NOT** be part of a mereological (`partOf`) hierarchy. | The "Role-as-Part" anti-pattern is a violation. Roles and capabilities are functional, not structural. Enforces **A.14**. |
| **CC-A15-6 (Resource Honesty)** | Resource consumption (`U.Resource`) **MUST** only be associated with `U.Work`, never with `U.MethodDescription` or `U.Capability`. | Enforces that costs are tied to actual events, not to plans or potential. Aligns with **Resrc-CAL (C.5)**. |
| **CC-A15-7 (Plan/Run Split)** | Schedules/calendars **MUST** be represented as `U.WorkPlan` (A.15.2). A `U.WorkPlan` SHALL NOT be used as evidence of execution; only `U.Work` carries actuals. | Preserves plan/run separation and prevents schedule-as-actual drift. |
| **CC-A15-8 (Lexical Sanity)** | Unqualified "process/workflow/schedule" **MUST** be interpreted per **L-PROC / L-FUNC / L-SCHED**: workflow -> `Method/MethodDescription`; schedule -> `WorkPlan`; what happened -> `Work`. | Keeps process vocabulary auditable and reduces lexical ambiguity. |
| **CC-A15-9 (Realisation)** | A valid `U.Work` realizes a `U.MethodDescription` under a `U.RoleAssignment`. Spontaneous physical evolution without a `MethodDescription` is modeled as `U.Dynamics`, not as `U.Work`. | Prevents background dynamics from being miscast as governed work. |
| **CC-A15-10 (GateSplit)** | A SpeechAct that changes a Role's state (e.g., "Approve", "Authorize") MUST be modeled as a distinct `U.Work` step (`kind=Communicative`). It may open the Green-Gate for a subsequent operational step, but it SHALL NOT be conflated with that step. | Preserves authority-state changes as distinct communicative acts. |
| **CC-A15-11 (KindFit)** | The `U.Role` named in the `performedBy` assignment SHALL be appropriate for the `U.Work` kind (e.g., `ApproverRole` for communicative approvals; `DeployerRole` for operational deployments). | Prevents kind-mismatched role attribution. |
| **CC-A15-12 (Weakened Rendering Non-Authority)** | A lighter briefing, summary, redacted note, or coarsened rendering **SHALL NOT** be treated as sufficient action cue, implementation checklist, work plan, work occurrence, approval, gate, execution authority, or executable work authority by convenience alone. If lawful work still depends on stronger method or evidence-bearing material, that stronger source **MUST** be reopened or explicitly linked before work proceeds. | Prevents orientation notes or disclosure renderings from silently becoming implementation cues, action checklists, approvals, gates, or authority substitutes. |

### A.15:8 - Common Anti-Patterns and How to Avoid Them

- **Role-as-part.** Do not place `U.Role` or `U.Capability` inside structural `partOf` decomposition; keep them contextual and functional.
- **Recipe-as-evidence.** Do not treat a `U.MethodDescription` or SOP as proof that work occurred; record dated `U.Work` instead.
- **Plan-as-actual.** Do not let schedules, calendars, or intended assignments stand in for actual execution; use `U.WorkPlan` for intent and `U.Work` for actuals.
- **Capability-as-work.** Do not treat possession of a capability as if the task has already been performed; capability supports execution but is not execution.
- **Approval collapse.** Do not merge approval or authorization speech acts into the operational step they open; model them as distinct communicative `U.Work` when they change authority state.
- **Process soup.** Do not leave "process / workflow / activity" uninterpreted in load-bearing passages; resolve the word to method, plan, or work.
- **Briefing-as-execution-cue.** Do not treat a lighter review note, rollout summary, or redacted operations note as if it already authorized execution, approval, gate passage, or a work plan. Reopen the stronger governing method or evidence-bearing material before work proceeds.

### A.15:9 - Consequences

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Unambiguous Communication:** Provides a shared, precise vocabulary for teams to discuss roles, processes, and results, eliminating the ambiguity of terms like "process." | **Initial Learning Curve:** Requires teams to learn and internalize the distinctions between the core entities. *Mitigation:* The "Chef" analogy and clear archetypes serve as powerful didactic tools. FPF tooling should guide users with templates. |
| **End-to-End Auditability:** The framework creates a "digital thread" that links every operational event (`Work`) back to its authorizing role, context, and specification. This is critical for regulated industries and for root cause analysis. | **Increased Formality:** Requires more explicit modeling than informal approaches. *Mitigation:* This is a strategic investment. The upfront cost of formal modeling is offset by massive savings in debugging, re-work, and compliance efforts later. |
| **Enables True Modularity:** By separating capability from execution, the framework allows for easier substitution. A `MethodDescription` can be updated without invalidating past `Work` records. A `Holder` can be replaced with another, as long as it possesses the same `Capability`. | - |
| **Foundation for Governance:** The model makes it possible to build powerful governance rules. For example: "Only an `Agent` with `AuditorRole` can execute `Work` that instantiates the `ApproveRelease` capability." | - |

### A.15:10 - Rationale

This pattern solves a problem that has plagued systems modeling for decades: the conflation of what a system *is* with what it *does*. Its rigor is not arbitrary but is grounded in several key intellectual traditions.

*   **Ontology Engineering:** The pattern is a direct application of best practices from foundational ontologies (like UFO), which have long insisted on the distinction between *endurants* (objects like a `U.System`) and *perdurants* (events/processes like `U.Work`), and between intrinsic properties and relational roles. FPF makes these powerful distinctions accessible to practicing engineers.
*   **Process Theory:** Formalisms like the Pi-calculus or Petri Nets model processes as dynamic interactions. The FPF Contextual Action Framework provides a higher-level, more semantically rich layer on top of such formalisms. The `U.Work` entity can be seen as an instance of a process, but FPF adds the crucial context of the `Role`, `Capability`, and `MethodDescription` that govern it.
*   **Pragmatism and Practice:** The framework is deeply pragmatic. The distinctions it makes (e.g., between a `MethodDescription` and `U.Work`) are precisely the ones that matter in the real world of project management, compliance, and debugging. When a failure occurs, a manager needs to know: was the recipe wrong (`MethodDescription`), did the chef lack the skill (`Capability`), or did they just make a mistake this one time (`U.Work`)? This framework provides the vocabulary to ask and answer that question precisely.

By creating this clean, stratified alignment for enactment, FPF provides a stable and scalable foundation for all of its more advanced patterns, from resource management (`Resrc-CAL`) and decision theory (`Decsn-CAL`) to ethics (`Norm-CAL`).

### A.15:11 - SoTA-Echoing

**SoTA note.** This section does not mint an independent work-management layer. It stays truthful only when the Solution, Conformance Checklist, briefing non-authority slice, and Relations still keep role, method, plan, approval, and executed work distinct.

| Claim need | SoTA practice (post-2015) | Primary source (post-2015) | Alignment with `A.15` | Adoption status |
| --- | --- | --- | --- | --- |
| Recipe, plan, case, decision, and executed occurrence must stay separable. | Case-management, decision-modeling, and service-change practice distinguish discretionary case work, decision logic, planned change support, and the realized service/product change. | OMG CMMN 1.1 (2016); OMG DMN 1.5 (2024); ITIL 4 Practitioner: Change Enablement (2023). | The manufacturing, peer-review, and rollout slices keep `U.MethodDescription`, `U.WorkPlan`, approval work, and `U.Work` separate so a calendar or procedure never counts as the weld, review, deployment, or actual run. | **Adopt/Adapt.** Adopt the separation of case, decision, plan, and occurrence; adapt it to FPF's `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work`; reject an undifferentiated "process" object. |
| Architecture and digital-thread practice need traceable views without confusing description, authority, and occurrence. | Architecture-description and model-based systems practice treat descriptions, viewpoints, requirements, behavior, verification, and traceability as explicit review objects. | ISO/IEC/IEEE 42010:2022; OMG SysML v2.0 Language Specification (2025). | `A.15` uses actor-in-context, role assignment, method description, and work occurrence so post-hoc review can ask whether the problem was assignment, capability, recipe, plan, approval, or run. | **Adopt/Adapt.** Adopt explicit trace and viewpoint discipline; adapt it to role/method/work alignment; reject attributing work to a role label or document alone. |
| Approval and execution are distinct practical acts. | Change-enablement and decision-modeling practice separates risk assessment, authorization, scheduling, decision logic, and the work that realizes change. | ITIL 4 Practitioner: Change Enablement (2023); OMG DMN 1.5 (2024). | In the release and gate examples, an approval or authorization changes authorization state; it is not the same work as deployment, welding, or other operational occurrence. | **Adopt.** Adopt the communicative/operational split and reject collapse of approval into the thing approved. |
| Fast bounded exploration must not become committed rollout by convenience. | Contemporary service and modeling practice supports adaptive work while preserving explicit authorization, traceability, and reviewable transition from option exploration to committed change. | ITIL 4 Practitioner: Change Enablement (2023); ISO/IEC/IEEE 42010:2022; OMG SysML v2.0 Language Specification (2025). | The scout/probe moment returns evidence, budget posture, and a commit trigger rather than only a winner label. The practical safeguard is that successful exploration still needs explicit commit authority before it becomes work enactment. | **Adapt/Reject.** Adapt adaptive-change and traceability practice to FPF role/method/work splits; reject the shortcut where an early probe silently becomes a committed rollout. |

The nearest recovery anchors are the manufacturing, peer-review, and rollout briefing slices above, plus `CC-A15-7`, `CC-A15-10`, and `CC-A15-12`. If a SoTA row cannot be recovered through those local checks, do not let the source citation stand in for live `A.15` law.
### A.15:12 - Relations

*   **Directly Implements:** `A.7 Strict Distinction`.
*   **Builds Upon:** `A.2 (U.Role)`, `A.2.1 (U.RoleAssignment)`, `A.4 (Temporal Duality)`, `A.12 (External Transformer)`.
*   **Is Used By / Provides Foundation For:**
    *   `C.4 Method-CAL`: Provides the formal definition of `U.MethodDescription` and the `Gamma_method` operator for composing them.
    *   `C.5 Resrc-CAL`: Provides the `U.Work` entity to which resource consumption is attached.
    *   `B.1.6 Gamma_work`: The aggregation operator for `U.Work`.
    *   `B.4 Canonical Evolution Loop`: The entire loop is a sequence of `U.Work` instances that modify `MethodDescription`s.
    *   `A.15.2 U.WorkPlan`: plan-run split, baselines and variance against `U.Work`.
*   **Constrains:** Any FPF pattern that models actions or processes must use this framework to be conformant. It serves as the canonical alignment for **contextual enactment** in the FPF ecosystem.
*   **Coordinates with:** `L-PROC / L-FUNC / L-SCHED` (E-cluster) for lexical disambiguation of _process / workflow / schedule_; `A.6.3.CSC Controlled Semantic Coarsening` when a briefing or summary is primarily a weaker-source rendering rather than an enactment authority-bearing publication.

### A.15:12a - Coordinated-work evidence and quantum-like route note

Use A.15 first when the claim is about who acts, by which method, under which role, producing which work result. Coordinated work, routine skill, team alignment, tacit knowledge, and role-method fit are not quantum-like by default.

Action path:

1. Name the role, method, and work result before naming any distributed state.
2. State which work traces, artifacts, events, observations, reports, metrics, or role enactments make the coordination visible.
3. Ask whether role-method-work alignment alone explains the case. If yes, stay in A.15.
4. If no participant statement, local component report, single carrier, dashboard, or exported representation carries the inferred state faithfully enough for the intended use, add a `C.26.2` distributed-state reading.
5. State the weakest claim, time window, rival explanations, and export loss.
6. Route evidence strength through `A.10` and assurance strength through `B.3` when the claim supports action, audit, readiness, release, or compliance.

Add a `C.26.2` distributed-state reading only when coordinated work is being used as evidence for a state that no participant statement, local component report, single carrier, dashboard, or exported representation carries faithfully enough for the intended use. That evidence-bound claim states:

| Field | Required content |
| --- | --- |
| Carrier | Work trace, artifact, event, observation, report, metric, or role enactment that bears the evidence |
| Time window | When the reading holds and when it decays or must be refreshed |
| Probe or occasion | What question, task, workshop, incident, handover, dashboard, or coordination situation made the state readable |
| Weakest claim | The minimal distributed-state reading supported by the carriers |
| Rival explanations | Routine compliance, policy, command, coincidence, incentive, documentation artifact, or local skill that could explain the same work |
| Export loss | What is lost when the state is summarized into one report, score, or statement |

Useful outputs:

- an A.15 work-alignment claim when work roles explain the case;
- a C.26.2 weak distributed-state reading when coordination evidence survives ordinary rivals;
- an A.10/B.3 evidence or assurance route when the reading will support stronger use;
- no distributed-state claim when carriers, rivals, or time window cannot be named.

### A.15:End
