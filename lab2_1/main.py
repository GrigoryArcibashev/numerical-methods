import math
import matplotlib.pyplot as plt


def lab_1task():
    x_nodes = [0.033765, 0.169395, 0.38069, 0.61931, 0.830605, 0.966235]
    A = [0.085662, 0.180381, 0.233957, 0.233957, 0.180381, 0.085662]
    h1 = 0.1
    h2 = 0.05

    print(trapeze(h1, function))
    print(trapeze(h2, function))
    print(1 / 3 * (trapeze(h2, function) - trapeze(h1, function)))
    print()

    print(rectangles(h1, function))
    print(rectangles(h2, function))
    print(1 / 3 * (rectangles(h2, function) - rectangles(h1, function)))
    print()

    print(Simpson(h1, function))
    print(Simpson(h2, function))
    print(1 / 15 * (Simpson(h2, function) - Simpson(h1, function)))
    print()

    print(Gauss(x_nodes, A, function))


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


def lab_2task():
    exact = math.pi / 4
    deltaTrapeze = []
    deltaRectangle = []
    deltaSimpson = []
    for i in range(1, 100):
        deltaSimpson.append(abs(exact - Simpson(1 / i, function2)))
        deltaTrapeze.append(abs(exact - trapeze(1 / i, function2)))
        deltaRectangle.append(abs(exact - rectangles(1 / i, function2)))
    print(deltaRectangle)
    plt.plot([i for i in range(1, 100)], deltaRectangle, label="Rectangle")
    plt.plot([i for i in range(1, 100)], deltaTrapeze, label="Trapeze")
    plt.plot([i for i in range(1, 100)], deltaSimpson, label="Simpson")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # lab_1task()
    lab_2task()
