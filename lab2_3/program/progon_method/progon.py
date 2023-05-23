import numpy as np


class Progon:
    def __init__(self, p, q, maker, count):
        self.q = q
        self.p = p
        self.maker = maker
        self.count = count
        self.h = 1 / count
        self.xs = np.linspace(0, 1, count + 1)

    def a(self, p_i):
        return 2 + self.h * self.h * p_i

    def b(self, q_i):
        return self.h * self.h * q_i

    def matrix_new(self, row_0_, row_n_):
        mx = np.zeros((self.count + 1, self.count + 1))
        row_0 = row_0_(self.h)
        row_n = row_n_(self.h)
        for i in range(len(row_0)):
            mx[0, i] = row_0[i]
        for i in range(1, self.count):
            mx[i, i - 1] = 1
            mx[i, i] = - self.a(self.p(self.xs[i]))
            mx[i, i + 1] = 1
        for i in range(len(row_n)):
            mx[self.count, self.count - len(row_n) + i + 1] = row_n[i]
        return mx

    def free_new(self, b_0_, b_n_):
        free = np.empty(self.count + 1)
        b_0 = b_0_(self.h)
        b_n = b_n_(self.h)
        free[0] = b_0
        for i in range(1, self.count):
            free[i] = self.b(self.q(self.xs[i]))
        free[self.count] = b_n
        return free

    def make(self, row_0, row_n):
        mx = self.matrix_new(row_0[0], row_n[0])
        v = self.free_new(row_0[1], row_n[1])
        ys = self.maker(mx, v)
        return ys
