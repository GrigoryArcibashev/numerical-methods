from math import floor


def get_extended_A() -> list[list[float]]:
    return [
        [1.2345, 3.1415, 1, 9.9275],
        [2.3456, 5.9690, 0, 14.2836],
        [3.4567, 2.1828, 2.1, 12.8833]
        ]


def get_exact_solution() -> list[float]:
    return [1, 2, 2.41]


def cut(num: float, k: int) -> float:
    """Отбрасывает все цифры после запятой, начиная с (k+1)-ой"""
    s = pow(10, k)
    return floor(num * s) / s
