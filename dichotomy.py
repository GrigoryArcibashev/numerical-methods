from math import e, pi, sin, cos


def f(x):
    return 1 + sin(x) - 1.2 / (e**x)


def check(a: float, b: float, n: int, eps: float) -> bool:
    return (b - a) / pow(2, n) <= eps 


def dichotomy(a: float, b: float, eps: float) -> tuple[float, int]:
    n = 1
    while True:
        root = (a + b) / 2
        if check(a, b, n, eps):
            return root, n
        n += 1
        if f(a) * f(root) < 0:
            b = root
        else:
            a = root

def main() -> None:
    root, n = dichotomy(0, pi/2, 0.000005)
    print()
    print(f'x = {root} \nf(x) = {f(root)} \nn = {n}')     


main()
