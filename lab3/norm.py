from math import sqrt


def calc_norm(vector: list[float]) -> float:
    """Вычисляет норму"""
    return sqrt(sum(map(lambda x: pow(x, 2), vector)))
