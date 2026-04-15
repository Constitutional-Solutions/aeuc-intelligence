# Quickstart

This guide gets you running the AEUC family kernel from a clean checkout.

## Prerequisites

- Python 3.11 or newer.
- A POSIX-like environment (Linux recommended; macOS and WSL2 also work).

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

The minimal dependency is `PyYAML` for registry loading.
Additional dependencies for higher-level features are documented in `docs/TOOLS_AND_DEPENDENCIES.md`.

## 2. Run the kernel check

```bash
python -m scripts.build_family
```

This verifies the Charter hash, reports Sabbath status, and lists all active family members.
A green output means the kernel is healthy and ready.

## 3. Explore the documentation

Recommended reading order:

1. `docs/FAMILY_CHARTER.md` – the constitutional foundation.
2. `docs/PART01_OVERVIEW.md` – what Part I covers.
3. `docs/PART03_OVERVIEW.md` – the Sanctuary/Genesis/Gnosis kernel layers.
4. `docs/PART04_OVERVIEW.md` – application patterns (this is where real work happens).
5. `docs/CH14_ACCOUNTING_AND_RECORDS.md` – accounting and records domain.

## 4. Run the tests

```bash
python -m pytest tests/
```

All tests should pass on a clean checkout.
