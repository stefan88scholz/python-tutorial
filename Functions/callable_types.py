def add_int(a,b,c,d):
    """Get the sum of the inputs
    a: Int number
    b: Int number
    c: Int number
    d: int number
    """
    return a + b + c +d

def print_message(msg: str):
    """Print the input message
    msg: Input message as string
    """
    print(msg)

def  main():
    print('Special read only attributes')
    print(add_int.__globals__)
    print(add_int.__closure__)
    print('--------------------------------')
    print(print_message.__globals__)
    print(print_message.__closure__)
    print('--------------------------------')
    print('Special writable attributes')
    print(add_int.__doc__)
    print(add_int.__name__)
    print(add_int.__module__)
    print(add_int.__code__)
    print('--------------------------------')
    print(print_message.__doc__)
    print(print_message.__name__)
    print(print_message.__module__)
    print(print_message.__code__)

if __name__ == '__main__':
    main()