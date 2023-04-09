from math import cos, e, log, sin


def f(x: float) -> float:
    """Исходная ф-ия"""
    return 1 + sin(x) - 1.2 / (e ** x)


def fp(x: float) -> float:
    """Первая производная ф-ии f"""
    return cos(x) + 1.2 / (e ** x)


def fpp(x: float) -> float:
    """Вторая производная ф-ии f"""
    return -sin(x) - 1.2 / (e ** x)


def fi(x: float) -> float:
    """Ф-ия фи для метода простой итерации"""
    return log(1.2 / (1 + sin(x)))


def fip(x: float) -> float:
    """Первая производная ф-ии fi"""
    return -cos(x) / (1 + sin(x))
