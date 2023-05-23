from decimal import Decimal
import numpy as np


class RK4:
    def __init__(self, f, g):
        self.f = f
        self.g = g

    def make(self, y0, dy0, count: int):
        h = Decimal('1.0') / Decimal(str(count))
        res1 = [0] * count
        res2 = [0] * count
        lp = np.linspace(0, 1, count)
        res1[0] = y0
        res2[0] = dy0
        for i in range(count - 1):
            y, dy = self.step(Decimal(str(lp[i + 1])), y0, dy0, h)
            res1[i + 1] = y
            res2[i + 1] = dy
            y0, dy0 = y, dy
        return res1, res2

    def k1(self, x, y0, dy0, h):
        return h * self.f(x, y0, dy0)

    def k2(self, x, y0, dy0, k1, l1, h):
        return h * self.f(x, y0 + k1 / Decimal('2'), dy0 + l1 / Decimal('2'))

    def k3(self, x, y0, dy0, k2, l2, h):
        return h * self.f(x, y0 + k2 / Decimal('2'), dy0 + l2 / Decimal('2'))

    def k4(self, x, y0, dy0, k3, l3, h):
        return h * self.f(x, y0 + k3, dy0 + l3)

    def l1(self, x, y0, dy0, h):
        return h * self.g(x, y0, dy0)

    def l2(self, x, y0, dy0, k1, l1, h):
        return h * self.g(x, y0 + k1 / Decimal('2'), dy0 + l1 / Decimal('2'))

    def l3(self, x, y0, dy0, k2, l2, h):
        return h * self.g(x, y0 + k2 / Decimal('2'), dy0 + l2 / Decimal('2'))

    def l4(self, x, y0, dy0, k3, l3, h):
        return h * self.g(x, y0 + k3, dy0 + l3)

    def step(self, x, y, dy, h):
        k1_ = self.k1(x, y, dy, h)
        l1_ = self.l1(x, y, dy, h)
        k2_ = self.k2(x, y, dy, k1_, l1_, h)
        l2_ = self.l2(x, y, dy, k1_, l1_, h)
        k3_ = self.k3(x, y, dy, k2_, l2_, h)
        l3_ = self.l3(x, y, dy, k2_, l2_, h)
        k4_ = self.k4(x, y, dy, k3_, l3_, h)
        l4_ = self.l4(x, y, dy, k3_, l3_, h)

        return (
            y + (k1_ + Decimal('2') * k2_ + Decimal(
                    '2') * k3_ + k4_) / Decimal('6'),
            dy + (l1_ + Decimal('2') * l2_ + Decimal(
                    '2') * l3_ + l4_) / Decimal('6'))
