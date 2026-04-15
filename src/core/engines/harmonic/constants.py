"""
constants.py
============
Single source of truth for all harmonic / frequency constants in the AEUC stack.

All other harmonic-engine modules import from here.  Changing a constant here
propagates automatically throughout the entire AEUC system.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, Tuple

# ── Module-level sacred ratios (re-exported) ─────────────────────────────────
PHI: float = (1.0 + math.sqrt(5.0)) / 2.0        # 1.618 033 988 749 895
TAU: float = 2.0 * math.pi                         # full-circle constant
GOLDEN_ANGLE_RAD: float = TAU / (PHI ** 2)         # ≈ 2.399 963 229 rad
GOLDEN_ANGLE_DEG: float = math.degrees(GOLDEN_ANGLE_RAD)  # ≈ 137.508°

@dataclass(frozen=True)
class HarmonicConstants:
    """
    Immutable harmonic constants for the AEUC engine stack.

    Frozen dataclass so every engine instance shares an identical,
    tamper-proof parameter set.
    """

    # ── Reference pitches (Hz) ────────────────────────────────────────────
    A_432: float = 432.0        # Verdi / sacred tuning
    A_440: float = 440.0        # Concert pitch ISO 16
    C_256: float = 256.0        # Scientific pitch (middle-C)
    OM:    float = 136.10       # Tibetan Om / Earth-year frequency

    # ── Schumann resonances (Hz) ──────────────────────────────────────────
    SCHUMANN_FUNDAMENTAL: float = 7.83
    SCHUMANN_2: float = 14.3
    SCHUMANN_3: float = 20.8
    SCHUMANN_4: float = 27.3
    SCHUMANN_5: float = 33.8

    # ── Solfeggio frequencies (Hz) ────────────────────────────────────────
    SOLFEGGIO: Tuple[int, ...] = (174, 285, 396, 417, 528, 639, 741, 852, 963)

    # ── Sacred geometry ratios ────────────────────────────────────────────
    PHI:              float = PHI
    SQRT2:            float = math.sqrt(2)
    SQRT3:            float = math.sqrt(3)
    PI:               float = math.pi
    GOLDEN_ANGLE_DEG: float = GOLDEN_ANGLE_DEG

    # ── Base-144k encoding anchor ─────────────────────────────────────────
    BASE_144K:     int   = 144_000      # glyph address space size
    BASE_144K_REF: float = 432.0        # anchor pitch for glyph encoding


# Shared default instance — import this rather than constructing a new one
DEFAULTS = HarmonicConstants()


# ── Just-intonation interval ratios (numerator / denominator) ────────────────
JUST_RATIOS: Dict[str, Tuple[int, int]] = {
    "unison":         (1,  1),
    "minor_second":   (16, 15),
    "major_second":   (9,  8),
    "minor_third":    (6,  5),
    "major_third":    (5,  4),
    "perfect_fourth": (4,  3),
    "tritone":        (45, 32),
    "perfect_fifth":  (3,  2),
    "minor_sixth":    (8,  5),
    "major_sixth":    (5,  3),
    "minor_seventh":  (9,  5),
    "major_seventh":  (15, 8),
    "octave":         (2,  1),
}

# ── 12-TET ratios (exact) ─────────────────────────────────────────────────────
TET12_RATIOS: Dict[str, float] = {
    name: 2.0 ** (semitones / 12)
    for name, semitones in {
        "unison":         0,
        "minor_second":   1,
        "major_second":   2,
        "minor_third":    3,
        "major_third":    4,
        "perfect_fourth": 5,
        "tritone":        6,
        "perfect_fifth":  7,
        "minor_sixth":    8,
        "major_sixth":    9,
        "minor_seventh":  10,
        "major_seventh":  11,
        "octave":         12,
    }.items()
}