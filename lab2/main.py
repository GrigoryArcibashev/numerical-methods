from math import pi, sqrt

from funcs import f, fi, fp
from qmM import get_M, get_m, get_q


def dichotomy(a: float, b: float, eps: float) -> tuple[float, int]:
    """Метод дихотомии"""
    n = 1
    while True:
        root = (a + b) / 2
        if (b - a) / pow(2, n) <= eps:
            return root, n
        n += 1
        if f(a) * f(root) < 0:
            b = root
        else:
            a = root


def unwalking_chords(x0: float, x1: float, eps: float) \
        -> tuple[float, int]:
    """Метод неподвижных хорд"""
    n = 1
    xn = x1
    m = get_m(x0, x1, eps)
    while True:
        root = xn - f(xn) / (f(xn) - f(x0)) * (xn - x0)
        if abs(f(root)) / m <= eps:
            return root, n
        xn = root
        n += 1


def walking_chords(x0: float, x1: float, eps: float) \
        -> tuple[float, int]:
    """Метод поподвижных хорд"""
    n = 1
    xn_prev = x0
    xn = x1
    m = get_m(x0, x1, eps)
    while True:
        root = xn - f(xn) / (f(xn) - f(xn_prev)) * (xn - xn_prev)
        if abs(f(root)) / m <= eps:
            return root, n
        xn_prev = xn
        xn = root
        n += 1


def newton(x0: float, x1: float, eps: float) \
        -> tuple[float, int]:
    """Метод Ньютона"""
    n = 1
    xn = x0
    m = get_m(x0, x1, eps)
    M = get_M(x0, x1, eps)
    while True:
        root = xn - f(xn) / fp(xn)
        if M * pow(root - xn, 2) / (2 * m) <= eps:
            return root, n
        xn = root
        n += 1


def calc_delta_xn(xn: float, d: int, M: float) -> float:
    """Возвращает △xn"""
    return (-fp(xn) + d * sqrt(pow(fp(xn), 2) + 2 * M * f(xn))) / (-M)


def parabolas(x0: float, x1: float, eps: float) \
        -> tuple[float, int]:
    """Метод парабол"""
    n = 1
    xn = x0
    m = get_m(x0, x1, eps)
    M = get_M(x0, x1, eps)
    while True:
        root = xn + calc_delta_xn(xn, 1, M)
        if root < x0 or root > x1:
            root = xn + calc_delta_xn(xn, -1, M)
        if M * pow(root - xn, 2) / m <= eps:
            return root, n
        xn = root
        n += 1


def simple_iteration(x0: float, x1: float, eps: float) \
        -> tuple[float, int]:
    """Метод простой итерации"""
    n = 1
    xn = x1
    q = get_q(x0, x1, eps)
    while True:
        root = fi(xn)
        if abs(x1 - x0) * pow(q, n) / (1 - q) <= eps:
            return root, n
        xn = root
        n += 1


def main() -> None:
    a = 0.05
    b = pi / 2
    eps = 0.000005

    root, n = dichotomy(a, b, eps)
    print(f'ДИХОТОМИЯ\nx = {root} \nn = {n}\n')
    root, n = unwalking_chords(a, b, eps)
    print(f'ХОРДЫ(Н)\nx = {root} \nn = {n}\n')
    root, n = walking_chords(a, b, eps)
    print(f'ХОРДЫ(П)\nx = {root} \nn = {n}\n')
    root, n = newton(a, b, eps)
    print(f'НЬЮТОН\nx = {root} \nn = {n}\n')
    root, n = parabolas(a, b, eps)
    print(f'ПАРАБОЛЫ\nx = {root} \nn = {n}\n')
    root, n = simple_iteration(a, b, eps)
    print(f'ИТЕРАЦИЯ\nx = {root} \nn = {n}\n')

    print(f'm = {get_m(a, b, eps)}')
    print(f'M = {get_M(a, b, eps)}')
    print(f'q = {get_q(a, b, eps)}')


if __name__ == '__main__':
    main()
