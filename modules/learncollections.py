import collections.abc
from functions.learndecorators import exec_func_info

@exec_func_info
def list_of_methods() -> None:
    i: int = 0
    for method in dir(collections.abc):
        if '__' not in method:
            i += 1
            print(i, method, sep=': ')

def main() -> None:
    list_of_methods()

if __name__ == '__main__':
    main()
