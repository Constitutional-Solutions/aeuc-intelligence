# Part III Appendix – Substrate Profiles

These profiles describe how the AEUC kernel and family can run on different kinds of hosts while preserving core guarantees.

---

## Minimal USB / Low-RAM Host

Target: machines with ~4 GB RAM, booting from a USB drive or small disk.

- Runtime: Python 3.11+ and minimal system utilities.
- Enabled layers:
  - Sanctuary (Charter kernel, registry, basic logging).
  - Thin Genesis (boot script, kernel status, simple scheduler).
- Disabled or minimized by default:
  - Heavy models and external integrations.
  - Non-essential Gnosis services.

Recommended entrypoints:

- `python -m scripts.build_family` – verify Charter and registry.
- A small TUI/CLI for local assistance and governance tasks.

---

## Local Workstation / Developer Machine

Target: laptops and desktops with more RAM and storage.

- All minimal USB features, plus:
  - Richer logging (tailing audit streams into developer tools).
  - Local experiments in `src/research/` and `experiments/`.
  - More lenses active simultaneously.

---

## Cloud / Cluster Deployment

Target: servers or clusters with managed storage and networking.

- All workstation features, plus:
  - External log aggregation.
  - Distributed scheduling and orchestration.
  - Stronger hardware-level security controls.

Gnosis-level components (ORCHEST-Q, provisioner) are fully active here.

---

## Accelerator / Quantum-Adjacent Hosts (Research)

Target: systems with GPUs, TPUs, or emerging quantum-like accelerators.

- Sanctuary and Genesis behavior remain unchanged.
- Gnosis may:
  - Offload heavy computations.
  - Experiment with advanced harmonic/quantum-inspired modules under `src/research/`.

These integrations are governed by the same separation-of-concerns and security rules as any other research track.
