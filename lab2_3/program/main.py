import numpy as np
from matplotlib import pyplot as plt

from config import a, colors, counts
from lab3_progon import progon
from lab3_shoot import shoot, shoot_methods

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

        for name, met in shoot_methods.items():
            ax.plot(
                    np.linspace(0, 1, count),
                    res_shoot[name][count],
                    label=f'{name}',
                    color=colors[color_count]
                    )
            color_count += 1

        for acc in ('O(h^1)', 'O(h^2)'):
            ax.plot(
                    np.linspace(0, 1, count + 1),
                    res_progon[acc][count],
                    label=f'Разностная прогонка ({acc})',
                    color=colors[color_count]
                    )
            color_count += 1
        ax.legend()
    plt.show()
