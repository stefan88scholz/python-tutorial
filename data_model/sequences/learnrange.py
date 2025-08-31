# https://docs.python.org/3.13/library/stdtypes.html#typesseq-range
# https://docs.python.org/3.13/library/stdtypes.html#typesseq
from collections.abc import Collection, Iterable, Iterator

from functions.learndecorators import exec_func_info

@exec_func_info
def class_range() -> None:
    my_range: range = range(10)
    print(f'{type(my_range) = }')
    print(f'{my_range.__sizeof__() = }')
    print(f'{len(my_range) = }')
    print(f'{my_range = }')
    print(f'{my_range.__repr__() = }')
    print(f'{my_range.__str__() = }')
    print(f'{my_range.__iter__() = }')

    print(f'{isinstance(my_range,Collection) = }')
    print(f'{isinstance(my_range,Iterable) = }')
    print(f'{isinstance(my_range,Iterator) = }')
    print(f'{isinstance(my_range.__iter__(),Iterator) = }')

    print(f'{my_range.count(4) = }')
    print(f'{my_range.index(4) = }')
    print(f'{my_range.start = }')
    print(f'{my_range.stop = }')
    print(f'{my_range.step = }')

    print('Content: [',end='')
    for content in my_range:
        print(content,end=',')
    print(']')

    for idx,content in enumerate(my_range):
        print(f'my_range[{idx}] = {content}')

@exec_func_info
def list_of_methods() -> None:
    i: int = 0
    for method in dir(range):
        if '__' not in method:
            i += 1
            print(i, method, sep=': ')

def main() -> None:
    list_of_methods()
    class_range()

if __name__ == '__main__':
    main()
