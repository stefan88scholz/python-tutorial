#https://myshell.co.uk/blog/2018/11/python-f-string-formatting-cheatsheet/
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings

# Format specification:
# [[fill]align][sign][#][0][width][grouping_option][.precision][type]

from datetime import  datetime
from learntypes import learnclass

def conversion() -> None:
    rom : learnclass.City = learnclass.City('Rom','Italy')
    numb_a : int = 5
    print(f'{rom}') #returns City.__str__
    #print(f'{numb_a:!r}') format specifier not defined for int
    print(f'{rom:!r}') #returns City.__repr__
    print(f'{rom:!a}') #returns ascii(City.__repr__)

def main() -> None:
    conversion()

if __name__ == '__main__':
    main()
