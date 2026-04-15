# Example – Admitting a New Lens

This example walks through admitting a new lens, `STORY-ARCHIVIST`, from proposal to registry update.

---

## 1. Draft the LensSpec

A candidate spec is authored and proposed (status `candidate`):

```yaml
- id: "STORY-ARCHIVIST"
  display_name: "Story Archivist"
  lens: "Narrative"
  role: "Collects, curates, and synthesizes narrative reports from the family’s work."
  status: "candidate"
  scope:
    - "Read audit logs and reflections."
    - "Produce summaries for human members."
  tool_surface:
    - "logging_read_only"
    - "report_writer"
  invariants:
    - "Never alters primary audit logs."
    - "Marks all synthesized stories as derived."
  test_plan: "tests/test_story_archivist.py"
  escalation:
    - "ARCHITECT-Q"
    - "HUMAN-DIRECTOR"
  created_at: "2026-04-15T00:00:00Z"
  updated_at: "2026-04-15T00:00:00Z"
  hash: ""  # populated by LensSpec
```

This entry is added to `config/family_registry.yaml` in a proposed changeset.

---

## 2. Vetting

Relevant lenses review the proposal:

- ARCHITECT-Q – checks that the role fits the overall architecture.
- SECURE-Q – ensures the tool surface is read-only where appropriate.
- HUMAN-DIRECTOR – confirms the role aligns with covenant commitments.

Concerns (if any) are addressed and the spec is updated.

---

## 3. Voting

Each active member records a vote (`True` or `False`) on the proposal. A simple representation:

```python
votes = {
    "DEBUG-1": True,
    "ARCHITECT-Q": True,
    "CODE-Q": True,
    # ... all other active members ...
    "HUMAN-DIRECTOR": True,
}
```

These votes are stored in a governance record and may be referenced in future audits.

---

## 4. Admission via `admit_member`

In code, the family calls:

```python
from core.family_registry import FamilyRegistry, LensSpec, admit_member

registry = load_family_registry()  # helper from scripts/build_family_registry.py
candidate = LensSpec(
    id="STORY-ARCHIVIST",
    display_name="Story Archivist",
    lens="Narrative",
    role="Collects, curates, and synthesizes narrative reports from the family’s work.",
    status="candidate",
    scope=[
        "Read audit logs and reflections.",
        "Produce summaries for human members.",
    ],
    tool_surface=["logging_read_only", "report_writer"],
    invariants=[
        "Never alters primary audit logs.",
        "Marks all synthesized stories as derived.",
    ],
    test_plan="tests/test_story_archivist.py",
    escalation=["ARCHITECT-Q", "HUMAN-DIRECTOR"],
    created_at="2026-04-15T00:00:00Z",
    updated_at="2026-04-15T00:00:00Z",
)

admit_member(registry, candidate, votes)
```

`admit_member` ensures:

- The candidate is not already active.
- Every active member has a vote.
- All votes are `True`.

On success, the candidate’s status becomes `"active"` and the registry is updated.

---

## 5. Registry and audit update

After admission:

- `scripts/build_family_registry.py` is used to dump the updated registry back to `config/family_registry.yaml`, filling in the `hash` field.
- An `AuditEvent` is emitted with category `governance`, summarizing the admission, listing voters, and linking to the updated registry.

This example illustrates how the narrative in Chapter 5 maps to concrete YAML and Python.
