from auxiliary_funcs import cut


def method_gauss(ext_A: list[list[float]], k: int) -> list[float]:
    """Метод Гаусса с выбором главного элемента"""

    # Размерность матрицы A
    n = len(ext_A)

    for i in range(n):
        # Ищем главный элемент в i-ом столбце
        line_num, main_it = max(
                [(line, abs(ext_A[line][i])) for line in range(i, n)],
                key=lambda z: z[-1]
                )

        # Переставляем i-ую и line_num-ую строки местами
        tmp = ext_A[line_num]
        ext_A[line_num] = ext_A[i]
        ext_A[i] = tmp

        # Нормировка
        ext_A[i] = list(map(lambda z: cut(z / main_it, k), ext_A[i]))
        # Исключение элементов i-го столбца
        for j in range(i + 1, n):
            a_ji = ext_A[j][i]
            for u in range(n + 1):
                ext_A[j][u] = cut(
                        ext_A[j][u] - cut(ext_A[i][u] * a_ji, k),
                        k)

    # Вычисление матрицы-столбца X
    X = [0.0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        X[i] = ext_A[i][n]
        for j in range(n - 1, i, -1):
            X[i] = cut(X[i] - cut(ext_A[i][j] * X[j], k), k)
    return X
