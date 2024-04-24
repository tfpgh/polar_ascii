import math

domain: tuple[float, float] = (0.0, 2 * math.pi)


def r(theta: float) -> float:
    return 0.4 + math.cos(theta)
