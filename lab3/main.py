from auxiliary_funcs import get_extended_A
from csg import compact_scheme_gauss


def print_csg() -> None:
    print('Компактная схема Гаусса')
    for k in (2, 4, 6):
        X = compact_scheme_gauss(get_extended_A(), k)
        print(f'При k = {k}:')
        print(f'\tx1 = {X[0]}\n\tx2 = {X[1]}\n\tx3 = {X[2]}')


def main() -> None:
    print_csg()


if __name__ == '__main__':
    main()
