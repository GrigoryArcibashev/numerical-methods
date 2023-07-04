import numpy as np
from matplotlib import pyplot as plt
from decimal import Decimal
from config import a, colors, counts
from progon_method.main_progon import progon
from shoot_method.main_shoot import shoot, shoot_methods

if __name__ == '__main__':
    res_shoot = shoot()
    res_progon = progon()
    for count in counts:
        fig, ax = plt.subplots()
        ax.set_xlabel('x')
        ax.set_ylabel('y')

        color_count = 0

        xs = np.linspace(0, 1, 100)
        ys = np.exp(xs) + np.exp(-xs) + a * xs * xs - a * xs - 2

        ax.plot(xs, ys, color='red', label='Аналитическое решение')

        t = float(res_shoot['Рунге-Кутт'][count][0] - Decimal(ys[0]))
        tt = lambda x: float(x) - t

        for name, met in shoot_methods.items():
            yyy = list(map(tt, res_shoot[name][count]))
            ax.plot(
                    np.linspace(0, 1, count),
                    yyy,
                    label=f'{name}',
                    color=colors[color_count]
                    )
            color_count += 1


        t = res_progon['O(h^1)'][count][0] - ys[0]
        tt = lambda x: float(x) - t
        for acc in ('O(h^1)', 'O(h^2)'):
            if acc == 'O(h^1)':
                yyy = list(map(tt, res_progon[acc][count]))
            else:
                yyy = res_progon[acc][count]
            ax.plot(
                    np.linspace(0, 1, count + 1),
                    yyy,
                    label=f'Разностная прогонка ({acc})',
                    color=colors[color_count]
                    )
            color_count += 1
        ax.legend()
    plt.show()
