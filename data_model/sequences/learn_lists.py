# list is one of the basic sequence types in python.
# The list type is a mutuable sequence type
# https://docs.python.org/3/library/stdtypes.html#list
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# https://docs.python.org/3.13/reference/datamodel.html#mutable-sequences
from typing import Callable
from functools import wraps
from learntypes import learnclass

def function_name(func: Callable) -> Callable:
    @wraps(func)
    def print_name() -> None:
        print(f'{'':-<100}')
        print(f'You are in function {func.__name__}:')
        func()

    return print_name

my_list_int: list[int] = [0, 1, 2, 3, 4, 5,]
my_list_str: list[str] = ['apple', 'pear', 'cherry', 'apricot', 'grape', 'banana']
my_list_cities: list[learnclass.City] = [learnclass.City('Munich', 'Germany'),
                                         learnclass.City('Rom', 'Italy')]

@function_name
def print_lists() -> None:
    print(f'{my_list_int = }')
    print(f'{my_list_str = }')
    print(f'{my_list_cities = }')

@function_name
def list_slicing() -> None:
    """
    Syntax:      [x:y::z]
                  | |  |
    Start Index --- |  |
    Stop Index ------  |
    Step Interval ------
    :return:
    """
    print('Manipulate my_list_str')
    print(f'First Index: {my_list_str[0] = }')
    print(f'Last Index: {my_list_str[-1] = }')
    print(f'Index 1,2: {my_list_str[1:3] =}')
    print(f'Step size 2: {my_list_str[::2] =}')

    my_slice = slice(2,6)
    print(f'Using slice object: {my_list_str[my_slice] =}')

    print('Manipulate my_list_int:')
    my_list_int[1:3] = [6,7]
    print(my_list_int)
    my_list_int[::2] = [0 , 0, 0]
    print(my_list_int)

@function_name
def common_sequence_ops() -> None:
    rom : learnclass = learnclass.City('Rom','Italy')
    madrid : learnclass = learnclass.City('Madrid', 'Spain')

    print(f'Is Rom part of list of cities? ({rom in my_list_cities = })')
    print(f'Is Madrid NOT part of list of cities? ({madrid not in my_list_cities = })')
    print(f'Is number 6 part of my_list_int? ({6 in my_list_int = })')

@function_name
def add_remove_elements() -> None:
    #tmp_list_cities: list[City] = my_list_cities
    madrid = learnclass.City('Madrid', 'Spain')
    london = learnclass.City('London', 'England')
    my_list_cities.append(madrid)
    my_list_cities.append(london)
    print(f'New cities {my_list_cities[-2]} and {my_list_cities[-1]} added:')
    print(my_list_cities)
    print('Remove city Munich')
    my_list_cities.remove(learnclass.City('Munich', 'Germany'))
    print(my_list_cities)
    # Restore list
    #my_list_cities = tmp_list_cities

def main() -> None:
    print_lists()
    list_slicing()
    common_sequence_ops()
    add_remove_elements()

if __name__ == '__main__':
    main()