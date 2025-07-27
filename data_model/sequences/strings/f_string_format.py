#https://myshell.co.uk/blog/2018/11/python-f-string-formatting-cheatsheet/
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings

# Format specification:
# [[fill]align][sign][#][0][width][grouping_option][.precision][type]

from datetime import  datetime
from learntypes import learnclass

def conversion() -> None:
    rom : learnclass.City = learnclass.City('Rom','Italy')
    print(f'{rom}') #returns City.__str__
    print(f'{rom!s}')  # returns City.__str__
    print(f'{rom!r}') #returns City.__repr__
    print(f'{rom!a}') #returns ascii(City.__repr__)
    numb_a : int = 5
    print(f'{numb_a}')
    print(f'{numb_a!s}')
    print(f'{numb_a!r}')
    print(f'{numb_a!a}')
    text: str = 'This is a string object'
    print(f'{text}')
    print(f'{text!s}')
    print(f'{text!r}')
    print(f'{text!a}')


def equal_sign() -> None:
    breakf: str = 'Breakfast starts at 6am and ends at 10am'
    print(f'{breakf = }')
    print(f'{5 + 5 = }')
    print(f'{range(5) = }')
    print(f'{learnclass.City('Berlin','Germany') = }')
    print(f'{[x for x in range(10) if x % 2 == 0] = }')

def main() -> None:
    conversion()
    equal_sign()

if __name__ == '__main__':
    main()
