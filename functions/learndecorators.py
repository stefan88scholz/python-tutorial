# https://book.pythontips.com/en/latest/decorators.html
from collections.abc import Callable
from functools import wraps


def exec_func_info(func: Callable, data = None) -> Callable:
    @wraps(func)
    def print_name(*args) -> None:
        print(f'{'':-<100}')
        print(f'{'Start of function '.upper()}{func.__name__}:')
        if not len(args):
            func()
        else:
            func(*args)

        print(f'{'End of function '.upper()}{func.__name__}')
        print(f'{'':-<100}')

    return print_name


def main() -> None:
    pass


if __name__ == '__main__':
    main()
