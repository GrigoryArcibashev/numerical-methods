from auxiliary_funcs import cut, get_extended_A


def calc_b_ij(
        A: list[list[float]],
        B: list[list[float]],
        C: list[list[float]],
        ij: tuple[int, int],
        k: int) \
        -> float:
    i, j = ij
    res = A[i][j]
    for t in range(j):
        res = cut(res - cut(B[i][t] * C[t][j], k), k)
    return cut(res, k)


def calc_c_ij(
        A: list[list[float]],
        B: list[list[float]],
        C: list[list[float]],
        ij: tuple[int, int],
        k: int) \
        -> float:
    i, j = ij
    res = A[i][j]
    for t in range(i):
        res = cut(res - cut(B[i][t] * C[t][j], k), k)
    if B[i][i] == 0:
        return cut(res / 2.27622519233e-05, k)
    return cut(res / B[i][i], k)


def calc_x(
        Y: list[float],
        C: list[list[float]],
        X: list[float],
        i: int,
        n: int,
        k: int) \
        -> float:
    res = Y[i]
    for t in range(i, n - 1):
        res = cut(res - cut(C[i][t + 1] * X[t + 1], k), k)
    return cut(res, k)


def compact_scheme_gauss(extended_A: list[list[float]], k: int) -> list[float]:
    """Компактная схема Гаусса"""
    # Размерность матрицы A
    n = len(extended_A)

    # Вычисление матриц B и C
    B = [[0.0] * n for _ in range(n)]
    C = [[0.0] * i + [1.0] + [0.0] * (n - i - 1) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i >= j:
                B[i][j] = calc_b_ij(extended_A, B, C, (i, j), k)
            else:
                C[i][j] = calc_c_ij(extended_A, B, C, (i, j), k)

    # Вычисление матрицы-столбца Y
    raw_Y = [[0.0] * (n + 1) for _ in range(n)]
    for i in range(n):
        raw_Y[i][n] = calc_c_ij(extended_A, B, raw_Y, (i, n), k)
    Y = list(map(lambda y: y[n], raw_Y))

    # Вычисление матрицы-столбца X
    X = [0.0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        X[i] = calc_x(Y, C, X, i, n, k)
    return X
