"""
PhysOx — Voxel-aware physics framework.
Integrates UVoxID (space) and tΔt (time) into general-purpose physics utilities.
"""

from . import (
    constants,
    dynamics,
    electromagnetism,
    energy,
    gravity,
    kinematics,
    matter,
    momentum,
    thermo,
    waves,
    collisions,
    probability,
    rotation,
)

# Explicit re-exports for convenience
from .constants import *
from .dynamics import *
from .electromagnetism import *
from .energy import *
from .gravity import *
from .kinematics import *
from .matter import *
from .momentum import *
from .thermo import *
from .waves import *
from .collisions import *
from .probability import *
from .rotation import *

__all__ = [
    *constants.__all__,
    *dynamics.__all__,
    *electromagnetism.__all__,
    *energy.__all__,
    *gravity.__all__,
    *kinematics.__all__,
    *matter.__all__,
    *momentum.__all__,
    *thermo.__all__,
    *waves.__all__,
    *collisions.__all__,
    *probability.__all__,
    *rotation.__all__,
]
