# Part III – Kernel and Substrate Design (Overview)

Part III describes the AEUC family’s kernel and substrate: the minimal code that must exist for the family to boot, verify itself, and coordinate work on any host—from modest local hardware to more exotic platforms.

The design goal is **modularity and frugality**:

- Each module is as small and self-contained as possible.
- The kernel can run in a constrained environment (e.g. from USB with a few gigabytes of RAM).
- Higher-capacity hosts (up to and including future quantum or accelerator-backed systems) can attach additional services without changing the core guarantees.

---

## Chapters in Part III

- **Chapter 9 – Kernel Overview: Sanctuary · Genesis · Gnosis**
- **Chapter 10 – Boot Sequence and Environment Checks**
- **Chapter 11 – Core Services (Time, Logging, Memory, Scheduler)**
- **Chapter 12 – Constitutional Rhythms (Sabbath, Reflection, Buddy)**

Additional chapters may be added for specific substrates (e.g. "USB live environment", "cloud-hosted cluster", "hardware accelerators"), but the core logic should remain unchanged across them.
