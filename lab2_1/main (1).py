# This is a sample Python script.
import math
import numpy as np
import matplotlib.pyplot as plt

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def lab_1task():
    # Use a breakpoint in the code line below to debug your script.
    xArray = [0.033765, 0.169395, 0.38069, 0.61931, 0.830605, 0.966235]
    h1 = 0.1
    h2 = 0.05
    print(trapeze(h1,function))
    print(trapeze(h2,function))
    print((1 / 3) * (trapeze(h2,function) - trapeze(h1,function)))
    print()
    print(rectangles(h1,function))
    print(rectangles(h2,function))
    print((1 / 3) * (rectangles(h2,function) - rectangles(h1,function)))
    print()
    print(Simpson(h1,function))
    print(Simpson(h2,function))
    print((1 / 15) * (Simpson(h2,function) - Simpson(h1,function)))
    print()
    print(Gauss(xArray,function))


def trapeze(h,functionL):
    partitionMore = [x / 100000 for x in range(0, 100001, int(h * 100000))]
    return sum([(h / 2) * (functionL(x) + functionL(y)) for x, y in zip(partitionMore[:-1], partitionMore[1:])])


def rectangles(h,functionL):
    partitionMore = [x / 100000 for x in range(0, 100001, int(h * 100000))]
    return sum([functionL((x + y) / 2) * h for x, y in zip(partitionMore[:-1], partitionMore[1:])])


def Simpson(h,functionL):
    partitionMore = [x / 100000 for x in range(0, 100001, int(h * 100000))]
    return sum([(h / 6) * (functionL(x) + 4 * functionL(x + h / 2) + functionL(y)) for x, y in
                zip(partitionMore[:-1], partitionMore[1:])])


def Gauss(xAr,functionL):
    zipped = zip([0.085662, 0.180381, 0.233957, 0.233957, 0.180381, 0.085662], xAr)
    return sum([x * functionL(y) for x, y in zipped])


def function(x):
    return math.sqrt(math.log10(x + 1) + 1)


def secondFunction(x):
    return 1 / (x * x + 1)

# Press the green button in the gutter to run the script.
def lab_2task():
    exact = math.pi / 4
    deltaTrapeze=[]
    deltaRectangle=[]
    deltaSimpson=[]
    for i in range(1,100):
        deltaSimpson.append(abs(exact-Simpson(1 / i, secondFunction)))
        deltaTrapeze.append(abs(exact-trapeze(1 / i, secondFunction)))
        deltaRectangle.append(abs(exact-rectangles(1 / i, secondFunction)))
    plt.plot([i for i in range(1,100)], deltaRectangle, label="Прямоугольники")
    plt.plot([i for i in range(1, 100)], deltaTrapeze, label="Трапеция")
    plt.plot([i for i in range(1, 100)], deltaSimpson, label="Симпсон")
    plt.xlabel('n')
    plt.ylabel('δ(n)')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # lab_1task()
    lab_2task()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
