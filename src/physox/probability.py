"""
Probability resolution engine for Physox.
"""

import random

def resolve_event(base_chance_per_tick: float, ticks: int = 1, sig_chars: int = 38) -> bool:
    """
    Resolve whether an event occurs based on base chance, ticks, and tolerance.

    Args:
        base_chance_per_tick (float): raw probability per tick (0–1).
        ticks (int): number of ticks to accumulate.
        sig_chars (int): tolerance (digits of significance).
                         Lower sig_chars = fuzzier resolution,
                         higher sig_chars = stricter precision.

    Returns:
        bool: True if the event resolves (occurs), False otherwise.
    """
    if base_chance_per_tick <= 0:
        return False
    if base_chance_per_tick >= 1:
        return True

    scale = 10 ** (38 - sig_chars)
    effective_chance = min(1.0, base_chance_per_tick * ticks / scale)

    return random.random() < effective_chance


def cumulative_probability(base_chance_per_tick: float, ticks: int, sig_chars: int = 38) -> float:
    """
    Compute cumulative probability of an event across ticks.

    Args:
        base_chance_per_tick (float): raw probability per tick (0–1).
        ticks (int): number of ticks to accumulate.
        sig_chars (int): tolerance (digits of significance).

    Returns:
        float: probability between 0 and 1
    """
    if base_chance_per_tick <= 0:
        return 0.0
    if base_chance_per_tick >= 1:
        return 1.0

    scale = 10 ** (38 - sig_chars)
    return min(1.0, base_chance_per_tick * ticks / scale)


__all__ = [
    "resolve_event",
    "cumulative_probability",
]