from auxiliary_funcs import cut


def method_gauss(ext_A: list[list[float]], k: int) -> list[float]:
    """Метод Гаусса с выбором главного элемента"""

    # Размерность матрицы A
    n = len(ext_A)

    for i in range(n):
        # Ищем максимальный элемент в i-ом столбце
        t = max(
                [(j, abs(ext_A[j][i])) for j in range(i, n)],
                key=lambda z: z[-1]
                )

        # Переставляем i-ую и t[0]-ую строки местами
        tmp = ext_A[t[0]]
        ext_A[t[0]] = ext_A[i]
        ext_A[i] = tmp

        # ???
        ext_A[i] = list(map(lambda z: cut(z / t[1], k), ext_A[i]))
        for j in range(i + 1, n):
            a_next = ext_A[j][i]
            for x in range(n + 1):
                ext_A[j][x] = cut(
                        ext_A[j][x] - cut(ext_A[i][x] * a_next, k),
                        k)

    X = [0.0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        X[i] = ext_A[i][n]
        for j in range(n - 1, i, -1):
            X[i] = cut(X[i] - cut(ext_A[i][j] * X[j], k), k)
    return X
