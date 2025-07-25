from typing import Iterable, TypeVar

# Function with parameters
def function_with_parameters(a: int, b: int) -> None:
    """
    
    :param a: integer number a
    :param b: integer numb b
    :return: None
    """
    print(function_with_parameters.__name__)
    print(f'{a = }; {b = }; {a + b = }')

# Function with default parameters
def function_with_default_parameters(a: int =10, b: int =340) -> None:
    """

    :param a: integer number a
    :param b: integer numb b
    :return: None
    """
    print(function_with_default_parameters.__name__)
    print(f'a + b = {a} + {b} = {sum([a,b])}')

T = TypeVar('T')
def function_optional_parameters(elements: Iterable[T], target: list[T].__or__(None) = None) -> list[T]:
    if target is None:
        target = []
    target.extend(elements)
    return target

def main():
    function_with_parameters(5,6)
    function_with_default_parameters()
    function_with_default_parameters(100)
    function_with_default_parameters(100,100)
    # Function expects two int as parameters but does not throw an error.
    # If type check is necessary than buildin function isInstance needs to be used
    function_with_default_parameters(5.5,6.7)

    print(function_optional_parameters([1,2]))

if __name__ == '__main__':
    main()

