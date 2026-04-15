# Chapter 10 – Boot Sequence and Environment Checks

This chapter describes how the AEUC family boots on a host machine and how it checks its environment before doing any meaningful work.

---

## 10.1 Goals

- Boot in a small, predictable way on minimal hardware (e.g. USB live environment with 4 GB RAM).
- Verify core invariants (Charter, registry, basic timekeeping) before enabling higher layers.
- Detect missing or degraded resources and adjust behavior instead of failing silently.

---

## 10.2 High-level boot sequence

A typical cold start proceeds through these stages:

1. **Host startup (outside AEUC)**
   - The host OS (or minimal runtime) boots from disk or USB.
   - Python/runtime and basic dependencies become available.

2. **Sanctuary initialization**
   - `core/charter_kernel.py` is loaded.
   - The kernel locates `docs/FAMILY_CHARTER.md` and verifies its hash.
   - Failure here causes the system to enter a conservative, read-only mode.

3. **Registry load**
   - `scripts/build_family_registry.load_family_registry()` reads `config/family_registry.yaml` into a `FamilyRegistry`.
   - Basic sanity checks ensure required lenses (e.g. KERNEL-Q, SECURE-Q, HUMAN-DIRECTOR) are present.

4. **Sabbath and time status**
   - `core/sabbath.is_sabbath(now)` is evaluated using the host clock.
   - The result is stored for use in gating deployment and heavy tasks.

5. **Kernel status snapshot**
   - `core/family_kernel.check_kernel_status()` produces a `KernelStatus` object summarizing:
     - `charter_ok`
     - `is_sabbath_now`
     - `active_member_ids`

6. **Genesis handoff**
   - Higher-level initialization logic (Genesis) decides which services to start based on kernel status and available hardware.
   - For example, it may start only a small subset of lenses on a constrained host.

The existing `scripts/build_family.py` script demonstrates a minimal version of this flow.

---

## 10.3 Environment checks

Before enabling expensive or risky capabilities, the kernel performs environment checks such as:

- **Filesystem layout** – required paths (docs, core, config, logs, archives) exist and are readable/writable as appropriate.
- **Resource snapshot** – available RAM, CPU cores, disk space.
- **Optional accelerators** – presence of GPUs, TPUs, or other devices, detected via pluggable probes.
- **Network status** – whether outbound network access is available and permitted by policy.

On constrained systems (e.g. 4 GB RAM, no accelerators):

- Gnosis-level capabilities (large models, heavy data processing) may be disabled or replaced with lighter alternatives.
- The family may run in a "local-only" mode that prioritizes governance, logging, and small-scale assistance.

---

## 10.4 Degraded and safe modes

If any critical check fails (e.g. Charter hash mismatch, missing registry, corrupt logs):

- The kernel enters a **safe mode**:
  - No new high-risk tasks are accepted.
  - Only introspection, repair, and human-guided actions are allowed.

If non-critical checks fail (e.g. network unavailable, no accelerators):

- The kernel logs the condition and continues in a **degraded mode** with reduced capabilities.

In both cases, the priority is to remain truthful about the system’s state and to avoid silent violations of the Charter or axioms.
