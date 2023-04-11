import math
import matplotlib.pyplot as plt


def task1():
    x_nodes = [0.033765, 0.169395, 0.38069, 0.61931, 0.830605, 0.966235]
    A = [0.085662, 0.180381, 0.233957, 0.233957, 0.180381, 0.085662]
    h1 = 0.1
    h2 = 0.05

    print('Трапеции')
    print('h1:', end=' ')
    print(trapeze(h1, function))
    print('h2:', end=' ')
    print(trapeze(h2, function))
    print('Погрешность:', end=' ')
    print(trapeze_inaccuracy_by_Runge(function, h1, h2))
    print()

    print('Прямоугольники')
    print('h1:', end=' ')
    print(rectangles(h1, function))
    print('h2:', end=' ')
    print(rectangles(h2, function))
    print('Погрешность:', end=' ')
    print(rectangles_inaccuracy_by_Runge(function, h1, h2))
    print()

    print('Симпсон')
    print('h1:', end=' ')
    print(Simpson(h1, function))
    print('h2:', end=' ')
    print(Simpson(h2, function))
    print('Погрешность:', end=' ')
    print(Simpson_inaccuracy_by_Runge(function, h1, h2))
    print()

    print('Гаусс')
    print(Gauss(x_nodes, A, function))


def trapeze_inaccuracy_by_Runge(func, h1, h2):
    return 1 / 3 * (trapeze(h2, func) - trapeze(h1, func))


def rectangles_inaccuracy_by_Runge(func, h1, h2):
    return 1 / 3 * (rectangles(h2, func) - rectangles(h1, func))


def Simpson_inaccuracy_by_Runge(func, h1, h2):
    return 1 / 15 * (Simpson(h2, func) - Simpson(h1, func))


def trapeze(h, func):
    m = int(1 / h) + 1
    x_nodes = [h * x for x in range(m)]
    f = [(func(x) + func(x_next))
         for x, x_next in zip(x_nodes[:-1], x_nodes[1:])]
    return h / 2 * sum(f)


def rectangles(h, func):
    m = int(1 / h) + 1
    x_nodes = [h * x for x in range(m)]
    f = [func((x + x_next) / 2)
         for x, x_next in zip(x_nodes[:-1], x_nodes[1:])]
    return h * sum(f)


def Simpson(h, func):
    m = int(1 / h) + 1
    x_nodes = [h * x for x in range(m)]
    f = [(func(x) + 4 * func((x + x_next) / 2) + func(x_next))
         for x, x_next in zip(x_nodes[:-1], x_nodes[1:])]
    return h / 6 * sum(f)


def Gauss(x_nodes, A, func):
    return sum([i * func(j) for i, j in zip(A, x_nodes)])


def function(x):
    return math.sqrt(math.log10(x + 1) + 1)


def function2(x):
    return 1 / (x * x + 1)


def task2():
    exact = math.pi / 4
    deltaTrapeze = []
    deltaRectangle = []
    deltaSimpson = []
    vals = [x for x in range(1, 101)]
    for x in vals:
        deltaSimpson.append(abs(exact - Simpson(1 / x, function2)))
        deltaTrapeze.append(abs(exact - trapeze(1 / x, function2)))
        deltaRectangle.append(abs(exact - rectangles(1 / x, function2)))
    plt.plot(vals, deltaRectangle, label="Прямоугольники")
    plt.plot(vals, deltaTrapeze, label="Трапеция")
    plt.plot(vals, deltaSimpson, label="Симпсон")
    plt.xlabel('n')
    plt.ylabel('δ(n)')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # task1()
    task2()
