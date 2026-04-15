"""
aeuc-harmonic-engine
====================
Harmonic computation layer for the AEUC stack.

Quick start::

    from src.core.engines.harmonic import HarmonicEngine
    engine = HarmonicEngine()
    chord  = engine.resolve_payload({
        "type": "chord",
        "data": {"root": 432.0, "intervals": ["perfect_fifth", "major_third"]}
    })
    # → [432.0, 648.0, 540.0]
"""
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("aeuc-harmonic-engine")
except PackageNotFoundError:
    __version__ = "0.0.0"

from .constants   import HarmonicConstants, DEFAULTS, JUST_RATIOS, TET12_RATIOS
from .intervals   import JustInterval, TET12Interval, IntervalAlgebra
from .engine      import HarmonicEngine
from .transitions import HarmonicTransitionGraph, HarmonicEdge

__all__ = [
    "HarmonicConstants",
    "DEFAULTS",
    "JUST_RATIOS",
    "TET12_RATIOS",
    "JustInterval",
    "TET12Interval",
    "IntervalAlgebra",
    "HarmonicEngine",
    "HarmonicTransitionGraph",
    "HarmonicEdge",
    "__version__",
]