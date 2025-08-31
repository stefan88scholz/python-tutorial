from functions.learndecorators import exec_func_info

text1: str = 'Germany, officially the Federal Republic of Germany, is a country in Central Europe.'
text2: str = 'HP, ACER, ASUS, APPLE, DELL'
text_fruits1: str = 'apple, banana, pear, strawberry'
text_fruits2: str = 'orange, pineapple, mango, kiwi, blueberry, apple, banana, pear, strawberry'
text_apples: str = 'red apple, green apple, rotten apple, unripe apple, toffee apple, apple turnover'

@exec_func_info
def method_capitalize_casefold() -> None:

    print(f'{text1 = }')
    print(f'{text1.capitalize() = }')
    print(f'{text1.casefold() = }')

    print(f'{text2 = }')
    print(f'{text2.capitalize() = }')
    print(f'{text2.casefold() = }')

    print(f'{text_fruits1 = }')
    print(f'{text_fruits1.capitalize() = }')
    print(f'{text_fruits1.casefold() = }')

@exec_func_info
def method_center() -> None:
    print('Apple'.center(100))
    print(f' Apple '.center(100,'*'))
    print(str.center(text_fruits1,100,'$'))

@exec_func_info
def method_count() -> None:
    print(f'{text_fruits1 = }')
    print(f'{text_apples = }')
    print(f'{text_fruits1.count('apple') = }')
    print(f'{text_apples.count('apple') = }')
    print(f'{text_apples[6:40:] = }')
    print(f'{text_apples.count('apple',6, 40) = }')

@exec_func_info
def method_encode() -> None:
    # https://docs.python.org/3.13/library/stdtypes.html#str.encode
    # https://docs.python.org/3.13/library/codecs.html#standard-encodings
    print(f'{text_fruits2 = }')
    print(f'{text_fruits2.encode('utf_8') = }')
    print(f'{text_fruits2.encode('utf_16') = }')
    print(f'{text_fruits2.encode('utf_32') = }')
    print(f'{text_fruits2.encode('ascii') = }')
    print(f'{text_fruits2.encode('cp037') = }')
    any_text = r'aTHld_5847_&$)=§!"_\n_/t_#<>'
    print(f'{any_text = }')
    print(f'{any_text.encode('utf_8') = }')
    print(f'{any_text.encode('utf_16') = }')
    print(f'{any_text.encode('utf_32') = }')
    print(f'{any_text.encode('ascii',errors='replace') = }')
    print(f'{any_text.encode('ascii',errors='backslashreplace') = }')
    print(f'{any_text.encode('ascii',errors='ignore') = }')
    try:
        print(f'{any_text.encode('ascii') = }')
    except Exception as e:
        print(f'ERROR: {e}')
    print(f'{any_text.encode('cp037') = }')

@exec_func_info
def method_endswith() -> None:
    print(f'{text2 = }')
    print(f'{text2.endswith('ll') = }')
    print(f'{text2.endswith('LL') = }')
    print(f'{text2[4:14] = }')
    print(f'{text2.endswith('ASUS',4, 14) = }')
    print(f'{text1[24:52] = }')
    print(f'{text1.endswith(('Europe.','Germany,'),24, 52) = }')
    print(f'{text1 = }')
    print(f'{text1.endswith(('Europe.','Germany')) = }')

@exec_func_info
def method_expandtabs() -> None:
    text_with_tab: str = 'This\tis\ta\ttext\twith\ttabs.'
    print(f'{text_with_tab = }')
    print(f'{text_with_tab.expandtabs() = }')
    print(f'{text_with_tab.expandtabs(2) = }')

@exec_func_info
def method_find() -> None:
    """
    https://docs.python.org/3.13/library/stdtypes.html#str.find
    :return:
    """
    print(f'{text_apples = }')
    print(f'{text_apples.find('apple')}')
    print(f'{text_apples[9:40] = }')
    print(f'{text_apples.find('apple',9,40)}')

@exec_func_info
def method_format() -> None:
    """
    https://docs.python.org/3.13/library/stdtypes.html#str.format
    :return:
    """
    print('His name is {} and birthplace is {}'.format('Bob','London'))
    print('His name is {name} and birthplace is {city}'.format(name='Bob', city='London'))
    print('{1} eats an {0}'.format('apple', 'Bob'))

@exec_func_info
def method_format_options() -> None:
    """
    https://docs.python.org/3.13/library/string.html#format-specification-mini-language

    :return:
    """
    print('{:,<100}'.format('GOLDEN GATE BRIDGE'))
    print('{:$^100}'.format('GOLDEN GATE BRIDGE'))
    print('{:=>100}'.format('GOLDEN GATE BRIDGE'))

    print('{:+100}'.format(20))
    print('{:0=+100}'.format(20))
    print('{:100,}'.format(1230045647939183138))
    print('{:100_}'.format(1230045647939183138))
    print('{:>100_b}'.format(1230045647939183138))
    print('{:100_x}'.format(1230045647939183138))
    print('{:100_X}'.format(1230045647939183138))
    print('{:100_o}'.format(1230045647939183138))
    print('{:100n}'.format(1230045647939183138))

    print('{:+100%}'.format(0.15))
    print('{: 100.2%}'.format(0.15))
    print('{: 100.2%}'.format(-0.15))

    print('{: 100e}'.format(1230045647939183138))
    print('{: 100E}'.format(1230045647939183138))
    print('{: 100f}'.format(1230045647939183138))
    print('{: 100g}'.format(1230045647939183138))

@exec_func_info
def method_format_map() -> None:
    pass

@exec_func_info
def method_index() -> None:
    print(f'{text_fruits2[12:17] = }')
    print(f'{text_fruits2.index('apple') = }')
    try:
        print(f'{text_fruits2.index('durian') = }')
    except ValueError as e:
        print(f'ValueError: {e}')

def method_isalnum_isalpha_isascii_isdecimal_isdigit_isidentifier() -> None:
    print(f'{'ABCdefg4'.isalnum() = }')
    print(f'{'ABCdefg45678§'.isalnum() = }')
    print(f'{'45678.123'.isalnum() = }')

    print(f'{'ABCdefg'.isalpha() = }')
    print(f'{'ABCdefg%'.isalpha() = }')
    print(f'{'ABCdefg4'.isalpha() = }')

    print(f'{'ABCdefg45678'.isascii() = }')
    print(f'{'ABCdefg45678§'.isascii() = }')

    print(f'{'45678'.isdecimal() = }')
    print(f'{'45678.123'.isdecimal() = }')

    print(f'{'0'.isdigit() = }')
    print(f'{'01'.isdigit() = }')
    print(f'{'01.2'.isdigit() = }')
    print(f'{'01f'.isdigit() = }')

    print(f'{'ABCdefg45678'.isidentifier() = }')
    print(f'{'ABCdefg45678§'.isidentifier() = }')

@exec_func_info
def string_iterable() -> None:
    for letter in text1:
        print(letter,end='')
    print('')
    for idx,letter in enumerate(text1,start=0):
        print(f'[{idx}:{letter}]',end=',')
    print('')
    print(f'{next(text1.__iter__()) = }')
    print(f'{next(text1.__iter__()) = }')
    my_iter = iter(text1)
    print(f'{next(my_iter) = }')
    print(f'{next(my_iter) =}')
    print(f'{next(my_iter) =}')

@exec_func_info
def string_operators() -> None:
    """
    Implemented operators of class str:
    +
    ==
    !=
    """

    text_a = 'Hello '
    text_b = 'Sir!'
    text_c = 'Hello '
    numb_a = '5'
    numb_b = '40'

    try:
        print(f'{text_a + text_b = }')
        print(f'{numb_a + numb_b = }')
        print(f'{text_a == text_b = }')
        print(f'{text_a != text_b = }')
        print(f'{text_a == text_c = }')
        print(f'{text_a > text_b = }')
        print(f'{numb_a > numb_b = }')

        for idx,letter in enumerate(text_a):
            print(f'text_a[{idx}]: {ord(letter) = }')
        for idx,letter in enumerate(text_b):
            print(f'text_b[{idx}]: {ord(letter) = }')
        for idx,letter in enumerate(numb_a):
            print(f'numb_a[{idx}]: {ord(letter) = }')
        for idx,letter in enumerate(numb_b):
            print(f'numb_b[{idx}]: {ord(letter) = }')

        # Unsupported operators
        print(f'{numb_a - numb_b = }')
        print(f'{numb_a * numb_b = }')
        print(f'{numb_a / numb_b = }')
    except Exception as e:
        print(f'ERROR: {e}')

@exec_func_info
def content_of_str() -> None:
    i: int = 0
    for method in dir(str):
        if '__' not in method:
            i += 1
            print(i, method, sep=': ')

def main() -> None:
    content_of_str()
    #method_capitalize_casefold()
    #method_center()
    #method_count()
    #method_encode()
    #method_endswith()
    #method_expandtabs()
    #method_find()
    #method_format()
    #method_format_options()
    #method_index()
    #method_isalnum_isalpha_isascii_isdecimal_isdigit_isidentifier()
    #string_operators()
    #string_iterable()


if __name__ == '__main__':
    main()