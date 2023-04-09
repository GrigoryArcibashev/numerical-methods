from auxiliary_funcs import get_exact_solution, get_extended_A
from csg import compact_scheme_gauss
from norm import calc_norm
from mg import method_gauss


def print_csg() -> None:
    print('Компактная схема Гаусса')
    for k in (2, 4, 6):
        X = compact_scheme_gauss(get_extended_A(), k)
        print(f'При k = {k}:')
        print(f'\tx1 = {X[0]}\n\tx2 = {X[1]}\n\tx3 = {X[2]}')
    print('\n')


def print_mg() -> None:
    print('Метод Гаусса с выбором главного элемента')
    for k in (2, 4, 6):
        X = method_gauss(get_extended_A(), k)
        print(f'При k = {k}:')
        print(f'\tx1 = {X[0]}\n\tx2 = {X[1]}\n\tx3 = {X[2]}')
    print('\n')


def print_norm_csg() -> None:
    print('НОРМА: компактная схема Гаусса')
    for k in (2, 4, 6):
        X = compact_scheme_gauss(get_extended_A(), k)
        exact_X = get_exact_solution()
        norm = calc_norm([X[i] - exact_X[i] for i in range(len(X))])
        print(f'При k = {k}:')
        print(f'\tnorm = {norm}')
    print('\n')


def print_norm_mg() -> None:
    print('НОРМА: метод Гаусса с выбором главного элемента')
    for k in (2, 4, 6):
        X = method_gauss(get_extended_A(), k)
        exact_X = get_exact_solution()
        norm = calc_norm([X[i] - exact_X[i] for i in range(len(X))])
        print(f'При k = {k}:')
        print(f'\tnorm = {norm}')
    print('\n')


def main() -> None:
    print_csg()
    print_mg()
    print_norm_csg()
    print_norm_mg()


if __name__ == '__main__':
    main()
