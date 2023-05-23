import numpy as np

from config import a, counts, p, q
from progon_method.progon_maker import tridiagonal_solve
from progon_method.progon import Progon

left_progon = {
    'O(h^1)': (lambda h: (-1, 1), lambda h: -a * h),
    'O(h^2)': (
        lambda h: (-2, 2 - h * h),
        lambda h: - 2 * h * a + h * h * q(h)
        )
    }

right_progon = {
    'O(h^1)': (
        lambda h: (1, -1),
        lambda h: - h * (np.e - 1 / np.e + a)
        ),
    'O(h^2)': (
        lambda h: (- 2 + h * h, 2),
        lambda h: 2 * h * (np.e - 1 / np.e + a) - h * h * q(1 - h)
        )
    }


def progon():
    res = {
        'O(h^1)': {},
        'O(h^2)': {}
        }
    for acc in ('O(h^1)', 'O(h^2)'):
        left = left_progon[acc]
        right = right_progon[acc]
        for count in counts:
            pr = Progon(p, q, tridiagonal_solve, count)
            y_s = pr.make(left, right)
            res[acc][count] = y_s

    return res
