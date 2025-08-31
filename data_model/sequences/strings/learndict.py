# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# https://www.w3schools.com/python/python_dictionaries.asp

from functions.learndecorators import exec_func_info
from typing import TypedDict

@exec_func_info
def content_of_dict() -> None:
    i: int = 0
    for content in dir(dict):
        if '_' not in content:
            i += 1
            print(i, content, sep=': ')

@exec_func_info
def init_dict_object() -> None:
    dict1: dict[str, int|str] = dict()
    dict2: dict[str,int] = {'0': 1, '1': 2, '2': 4, '3': 8}
    print(f'{dict1 = }')
    print(f'{dict2 = }')
    dict1['name'] = 'Bob'
    dict1['age'] = 30
    print(f'{dict1 = }')
    del(dict1['age'])
    print(f'{dict1 = }')

def main() -> None:
    pass

if __name__ == '__main__':
    content_of_dict()
    init_dict_object()
