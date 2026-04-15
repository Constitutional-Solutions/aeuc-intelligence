# Case Study – Contested Security Change

This case study illustrates how the family handles a contested proposal: adding a new external API integration that SECURE-Q initially rejects.

---

## 1. Proposal

CODE-Q proposes integrating with an external API to fetch supplementary data. The proposal is classified as:

- `security-sensitive`
- `architecture-impacting`

Candidate lenses involved:

- CODE-Q, ARCHITECT-Q, SECURE-Q, VERIFIER-Q, ORCHEST-Q, HUMAN-DIRECTOR.

---

## 2. Council and geometry

A family council is called. The proposal is mapped onto the Love/Truth/Power geometry:

- Primary axis: **Truth–Power** (more data and capability).
- Secondary concern: **Love** (potential privacy impact on humans).

Each lens presents its view:

- ARCHITECT-Q – how the integration fits system structure.
- CODE-Q – implementation details and fallback strategies.
- SECURE-Q – threat analysis and risk scenarios.
- VERIFIER-Q – test coverage requirements.
- HUMAN-DIRECTOR – ethical and covenant considerations.

---

## 3. SECURE-Q objects

SECURE-Q identifies a critical issue:

- The API Terms of Service allow unilateral changes that could force silent data sharing.

SECURE-Q votes **no** and documents the rationale.

According to Chapter 7’s rules, unanimous consent is required for this kind of change, so the proposal cannot proceed as-is.

---

## 4. Iteration

The council explores mitigations:

- Use a proxy that strips identifying information.
- Cache and sanitize responses.
- Add explicit user consent flows.
- Define strict monitoring and kill-switch procedures.

SECURE-Q reviews these mitigations and either:

- Changes its vote to **yes** once protections are sufficient, allowing unanimous consent, or
- Maintains **no**, in which case the proposal is rejected for now.

In both cases, the process is recorded via AuditEvents, including:

- Initial proposal and classification.
- Council discussion notes.
- Votes and their rationales.

---

## 5. Reflection

Regardless of the outcome, a reflection task is scheduled:

- During a Sabbath window, relevant lenses and HUMAN-DIRECTOR review the case.
- Lessons learned are added to the threat model and governance playbooks.

This case study shows how the abstract voting and gate rules operate when values and risks conflict in practice.
