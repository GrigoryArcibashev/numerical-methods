from math import e, pi, sin, cos, sqrt, log


def f(x: float) -> float:
    """Исходная ф-ия"""
    return 1 + sin(x) - 1.2 / (e**x)


def fp(x: float) -> float:
    """Первая производная ф-ии f"""
    return cos(x) + 1.2 / (e**x)


def fpp(x: float) -> float:
    """Вторая производная ф-ии f"""
    return -sin(x) - 1.2 / (e**x)


def fi(x: float) -> float:
    """Ф-ия фи для метода простой итерации"""
    return log(1.2 / (1 + sin(x)))


def fip(x: float) -> float:
    """Первая производная ф-ии fi"""
    return -cos(x) / (1 + sin(x))


def get_m(a: float, b: float, eps: float) -> float:
    """Возвращает число m = min(|f`(x)|)"""
    rng = [a + eps * i for i in range(int((b - a) / eps))]
    if rng[-1] < b:
        rng.append(b)
    return min(filter(lambda s: s > 0, map(abs, map(fp, rng))))


def get_M(a: float, b: float, eps: float) -> float:
    """Возвращает число M = max(|f``(x)|)"""
    rng = [a + eps * i for i in range(int((b - a) / eps))]
    if rng[-1] < b:
        rng.append(b)
    return max(map(abs, map(fpp, rng)))


def get_q(a: float, b: float, eps: float) -> float:
    """Возвращает число q = max(fi`(x))"""
    rng = [a + eps * i for i in range(int((b - a) / eps))]
    if rng[-1] < b:
        rng.append(b)
    return max(map(abs, map(fip, rng)))


def dichotomy(a: float, b: float, eps: float) -> tuple[float, int]:
    """Метод дихотомии"""
    n = 1
    while True:
        root = (a + b) / 2
        if (b - a) / pow(2, n) <= eps :
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
        if M * pow(root - xn, 2) / (2*m) <= eps:
            return root, n
        xn = root
        n += 1


def calc_delta_xn(xn: float, d:int, M: float) -> float:
    """Возвращает △xn"""
    return (-fp(xn) + d * sqrt(pow(fp(xn), 2) + 2 * M * f(xn))) / (-M) 


def parabols(x0: float, x1: float, eps: float) \
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
    root, n = parabols(a, b, eps)
    print(f'ПАРАБОЛЫ\nx = {root} \nn = {n}\n')   
    root, n = simple_iteration(a, b, eps)
    print(f'ИТЕРАЦИЯ\nx = {root} \nn = {n}\n')

    print(f'm = {get_m(a, b, eps)}')
    print(f'M = {get_M(a, b, eps)}')
    print(f'q = {get_q(a, b, eps)}')


main()
