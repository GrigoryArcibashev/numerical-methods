from funcs import fip, fp, fpp


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
