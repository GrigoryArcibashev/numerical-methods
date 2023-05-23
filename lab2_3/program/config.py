from decimal import Decimal

a = 2.1


# СТРЕЛЬБА
def f(x, y, dy):
    return y + Decimal('2') * Decimal(str(a)) + Decimal('2') + Decimal(
            str(a)) * x * (Decimal('1') - x)


g = lambda x, r, dr: r

# ПРОГОНКА
p = lambda x: 1

q = lambda x: 2.0 + 2.0 * a + a * x * (1 - x)

counts = [
    10,
    20,
    50,
    100
    ]

colors = ['m', 'g', 'orange', 'c', 'b']
