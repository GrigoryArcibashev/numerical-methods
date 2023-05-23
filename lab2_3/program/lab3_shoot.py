from decimal import Decimal

from config import a, counts, f, g
from shoot_method.methods.euler import Euler
from shoot_method.methods.euler2 import Euler2
from shoot_method.methods.rk import RK4
from shoot_method.shoot import Shoot


def right(y, dy):
    return dy - Decimal('1').exp() + Decimal('1') / Decimal(
            '1').exp() - Decimal(str(a))


def dright(r, dr):
    return dr


left_shoot = (lambda mu: -Decimal(str(a)), lambda mu: Decimal('0'))
right_shoot = (right, dright)
shoot_methods = {
    'Эйлер': (Euler(lambda x, y, dy: dy, f), Euler(lambda x, r, dr: dr, g)),
    'Эйлер с пересчетом': (
        Euler2(lambda x, y, dy: dy, f), Euler2(lambda x, r, dr: dr, g)),
    'Рунге-Кутт': (RK4(lambda x, y, dy: dy, f), RK4(lambda x, r, dr: dr, g))
    }


def shoot():
    dy_a, dr_a = left_shoot
    phi_b, dphi_b = right_shoot
    res = {
        'Эйлер': {},
        'Эйлер с пересчетом': {},
        'Рунге-Кутт': {}
        }
    for count in counts:
        for name, met in shoot_methods.items():
            sh = Shoot(met[0], met[1], count)
            y_s = sh.make1(dy_a, dr_a, phi_b, dphi_b)
            res[name][count] = y_s
    print()

    return res
