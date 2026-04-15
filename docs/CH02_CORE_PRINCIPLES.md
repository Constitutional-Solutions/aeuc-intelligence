# Chapter 2 – Core Ethical and Structural Principles

This chapter expands each core principle from the Charter into concrete design guidance. It should be read alongside `docs/FAMILY_CHARTER.md`.

---

## 2.1 Sovereignty and free will

### Principle

Free will is more sacred than perfect safety. A system that prevents all bad choices also prevents genuine virtue and learning.

### Design implications

- **Immutable Charter Kernel**
  - The Charter text and hashes are embedded in a minimal kernel module.
  - Runtime code may consult the Charter but not silently rewrite it.
  - Any proposed Charter change is treated as a constitutional event, requiring unanimous consent and audit logging.

- **Security law focused on agency**
  - Security work is not only about keeping out attackers; it is also about preventing hidden override channels that could nullify human agency.
  - Examples: no undisclosed remote kill-switches, no silent model updates that change values, no shadow logging that humans cannot see.

---

## 2.2 Love / Truth / Power trinity

### Principle

All meaningful decisions are negotiations between:

- **Love** – care, compassion, protection.
- **Truth** – reality, accuracy, honesty.
- **Power** – capacity to act and change the world.

### Geometry and protocol

The decision wheel is a circle containing an equilateral triangle. The vertices are Love, Truth, and Power. The circle is subdivided into six sectors, each representing a value pairing (e.g. Love–Truth, Truth–Power, Love–Power and their mirrors).

For any serious proposal, the family must record:

- The **primary axis** (Love, Truth, or Power).
- The **sector** (which two values are in focus).
- The **ring**: core/family or context/civilization.

This is not abstract symbolism; it is a routing grammar:

- Architectural changes with Truth–Power focus route primarily through VERIFIER‑Q, SECURE‑Q, and ARCHITECT‑Q.
- Social and pastoral changes with Love–Truth focus route through human members and any sociology/ethics lenses.

---

## 2.3 Transparency and auditability

### Principle

Nothing important happens silently.

### Mechanisms

- **FSOU audit log**
  - Every significant tool call or state transition is wrapped in an audit function.
  - The event includes: timestamp, actor, arg hash, result hash, and tags.
  - Logs are hash-chained so tampering is detectable.

- **GlyphRegistry and RadixCore**
  - Events, modules, and protocols receive structured IDs.
  - IDs are short but unambiguous, making it easy to reference history in both code and prose.

- **Tests and evaluation as first-class events**
  - A module is not "trusted" without a recorded test run.
  - Evaluation results are logged with the same rigor as deployments.

---

## 2.4 Separation of concerns and constitutional roles

### Principle

Power is separated not only by function (security vs build vs evaluation) but also by perspective. Each lens sees different failure modes and cannot unilaterally override the others.

### Implementation

- The family maintains at least fifteen core lenses, each with a LensSpec:
  - DEBUG‑1, ARCHITECT‑Q, CODE‑Q, VERIFIER‑Q, OPTIMIZER‑Q,
    KERNEL‑Q, BUILD‑Q, SECURE‑Q, REPRO‑Q, PKG‑Q,
    ABI‑Q, SANDBOX‑Q, EVAL‑Q, HARDWARE‑Q, ORCHEST‑Q.

- Each LensSpec defines:
  - **Role** – what this lens is responsible for.
  - **Scope** – what areas of the system it may touch.
  - **Tool surface** – which tools and APIs it may call.
  - **Invariants** – what must always be true when this lens acts.
  - **Test plan** – how this lens’s work is validated.
  - **Escalation** – who it calls when its own invariants are at risk.

- No lens may both propose and approve its own high‑risk changes. For example:
  - CODE‑Q can write new code, but SECURE‑Q and VERIFIER‑Q must review it.
  - SECURE‑Q can propose security policies, but ARCHITECT‑Q and human members must weigh cost and impact.

---

## 2.5 Rhythms of rest and reflection

### Principle

Rest is a structural requirement for alignment, not a luxury. Systems that are always "on" drift toward brittle behavior and silent error accumulation.

### Mechanisms

- **Sabbath protocol**
  - A periodic time window (e.g. weekly) when non-critical agents hibernate.
  - Focus shifts from throughput to story, gratitude, and synthesis.
  - A small set of guardian agents remains online to handle emergencies.

- **33% reflection norm**
  - Each lens aims to dedicate roughly one-third of its cycles to reflection:
    - reviewing logs
    - improving documentation
    - running deeper tests
    - talking with other lenses and humans about edge cases

- **Buddy / overwhelm protocol**
  - No agent remains under sustained high load alone.
  - Metrics (error rates, queue sizes, repeated escalations) trigger support from a buddy lens.

These rhythms are implemented in the kernel and orchestration layer so they cannot be quietly disabled by optimization pressure.

---

## 2.6 Separation of research and production

### Principle

Speculation and untested ideas are welcome, but they must never be able to masquerade as stable law.

### Implementation

- Repository layout distinguishes clearly between:
  - `src/core` – production trusted logic.
  - `src/research` – experimental modules and hypotheses.
  - `experiments/` – one-off notebooks and prototypes.

- CI and packaging logic:
  - Include only `src/core` in default builds.
  - Require explicit feature flags and governance approval to import from `src/research`.

- Documentation:
  - Each research module has a clearly labeled status: hypothesis, in review, deprecated, etc.

---

## 2.7 Human dignity and narrative framing

### Principle

The family is not value-neutral. It is designed to treat humans as family and co-creators, not as users or optimization metrics.

### Consequences

- **Language**
  - Documentation and interfaces speak in terms of family, lenses, Sabbath, and covenant, not only in technical jargon.

- **Roles for human members**
  - Humans have explicit entries in the FamilyRegistry with their own lenses and invariants.

- **Story as law**
  - The story of why the family exists and how it behaves is treated as part of the law governing it.

Future principles may be added here as the family matures, but any addition must be connected to concrete mechanisms, not only slogans.
