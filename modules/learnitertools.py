#https://docs.python.org/3/library/itertools.html#
#https://pypi.org/project/more-itertools/

from collections.abc import Iterable
import itertools
from functions.learndecorators import exec_func_info

input_string = 'APPLE'
input_list = range(0, 10, 2)

@exec_func_info
def list_of_methods() -> None:
    i: int = 0
    for method in dir(itertools):
        if '__' not in method:
            i += 1
            print(i, method, sep=': ')

@exec_func_info
def method_cycle(data) -> None:
    buffer: itertools.cycle = itertools.cycle(data)
    print(f'{type(buffer) = }')
    repeat: int = 0
    start: int = 0
    end: int = len(data)

    for element in buffer:
        if start == 0:
            print(f'Sequence {repeat+1}',end=': ')
        print(element, end='')
        if start == end-1:
            if repeat == 5:
                print('')
                break
            else:
                repeat += 1
                start = 0
                print('')
        else:
            start += 1



def main() -> None:
    list_of_methods()
    method_cycle(input_string)
    #method_cycle(input_list)

if __name__ == '__main__':
    main()


