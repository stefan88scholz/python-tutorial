from functions.learndecorators import exec_func_info

@exec_func_info
def method_ord_chr() -> None:
    """
    https://docs.python.org/3.13/library/functions.html#ord
    ord(c): Given a string representing one Unicode character,
    return an integer representing the Unicode code point of that character.
    https://docs.python.org/3.13/library/functions.html#chr
    chr(i): Return the string representing a character whose Unicode code point is the integer i

    https://symbl.cc/de/unicode-table/
    :return:
    """
    print(f'{ord('&') = }')
    print(f'{chr(38)} = ')
    print(f'{ord('%') = }')
    print(f'{chr(37)} = ')
    print(f'{ord('§') = }')
    print(f'{chr(167) = }')
    print(f'{chr(2439) = }')
    print(f'{chr(2510) = }')

@exec_func_info
def method_iter_next_any_all() -> None:
    my_list = iter(('Thomas','Bob','Emma','Olivia'))
    element = next(my_list)
    print(f'{element = }')
    element = next(my_list)
    print(f'{element = }')
    element = next(my_list)
    print(f'{element = }')
    print(f'{any(my_list) = }')
    empty_string = ''
    print(f'{any(empty_string) = }')
    zero_list = [0, 0, 0, 0]
    print(f'{any(zero_list) = }')
    zero_one_list = [0, 0, 0, 1]
    print(f'{any(zero_one_list) = }')
    non_zero_list = [1, 5, 1, 100]
    print(f'{all(my_list) = }')
    print(f'{all(zero_one_list) = }')
    print(f'{all(non_zero_list) = }')

def main() -> None:
    method_ord_chr()
    method_iter_next_any_all()

if __name__ == '__main__':
    main()
