# Tools, Dependencies, and Libraries

This document summarizes the core runtime requirements and libraries used by the AEUC family.

---

## Runtime

- **Python**: 3.11 or newer.
- **Operating system**: any environment capable of running Python and providing a POSIX-like filesystem (Linux is the primary target; others may work with minor adaptations).

---

## Python libraries

Minimal kernel dependencies:

- `PyYAML` – used by `scripts/build_family_registry.py` to load and dump `config/family_registry.yaml`.

These are listed in `requirements.txt` at the repository root.

Research and higher-level components may introduce additional optional dependencies; they should be documented in their own README files and kept out of the minimal kernel set.

---

## Command-line tools

- `python -m scripts.build_family` – boot/check command: verifies Charter hash, reports Sabbath status, and lists active members.

As the system evolves, this document should be updated with any new required tools or libraries.
