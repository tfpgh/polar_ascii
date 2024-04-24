import math

domain: tuple[float, float] = (0.0, math.pi)


def r(theta: float) -> float:
    return math.cos(5 * theta)
