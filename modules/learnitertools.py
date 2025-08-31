#https://docs.python.org/3/library/itertools.html#
#https://pypi.org/project/more-itertools/

from collections.abc import Iterable
import itertools
from itertools import cycle
from functions.learndecorators import exec_func_info

input_string = 'APPLE'
input_range: range = range(0, 10, 2)
input_list: list[str] = ['Bob', 'James', 'Sandra']
input_tuple: tuple[str,int,str] = ('Bob', 32, 'London')
input_dict: dict[str,str | int]= {'Name': 'Bob', 'Age': 32, 'City': 'London'}

@exec_func_info
def content_of_itertools() -> None:
    i: int = 0
    for method in dir(itertools):
        if '__' not in method:
            i += 1
            print(i, method, sep=': ')

@exec_func_info
def class_cycle(data: Iterable, len_iter: int, nr_of_seq: int) -> None:
    buffer: cycle = cycle(data)
    print(f'{type(buffer) = }')
    repeat: int = 1
    start: int = 0
    end: int = len_iter

    for element in buffer:
        if start == 0:
            print(f'[{element}',end=',')
        elif start < end-1:
            print(element, end=',')
        else:
            print(element, end='')

        if start == end-1:
            if repeat == nr_of_seq:
                print(']')
                break
            else:
                repeat += 1
                start = 0
                print('],',end='')
        else:
            start += 1

def main() -> None:
    content_of_itertools()
    class_cycle(input_string, len(input_string), 3)
    class_cycle(input_range, len (input_range), 3)
    class_cycle(input_list, len(input_list), 3)
    class_cycle(input_tuple, len(input_tuple), 3)
    class_cycle(input_dict, len(input_dict), 3)

if __name__ == '__main__':
    main()


