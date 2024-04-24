import math

domain: tuple[float, float] = (-math.pi, math.pi)


def r(theta: float) -> float:
    return (
        (math.sin(theta) * math.sqrt(abs(math.cos(theta))))
        / (math.sin(theta) + (7 / 5))
        - (2 * math.sin(theta))
        + 2
    )
