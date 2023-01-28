from math import floor


def cut(n: float, k: int) -> float:
    """Отбрасывает все цифры после запятой, начиная с (k+1)-ой"""
    s = pow(10, k)
    return floor(n * s) / s


def main() -> None:
    print(cut(12, 3))


if __name__ == '__main__':
    main()
