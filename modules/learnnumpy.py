# https://github.com/numpy/numpy
# https://www.w3schools.com/python/numpy/numpy_intro.asp
# https://numpy.org/doc/stable/user/index.html

import numpy as np
from functions.learndecorators import exec_func_info

a0D = np.array(42)
a1D = np.array([1,2,4,8])
a2D = np.array([[1,2,4,8], [8,16,32,64]])
a3D = np.array([[1,2,4,8], [8,16,32,64], [64,128,256,512]])

@exec_func_info
def content_of_numpy() -> None:
    print(f' {np.__all__ = }')
    print(f' {len(np.__all__) = }')
    i: int = 0
    for content in dir(np):
        if '_' not in content:
            i += 1
            print(i, content, sep=': ')

def numpy_version() -> None:
    print(f' {np.__version__ = }')
    print(f' {np.__NUMPY_SETUP__ = }')

@exec_func_info
def numpy_array() -> None:
    print(f'{type(a1D) = }')
    print(f'{a1D.__str__() = }')
    print(f'{a1D.__repr__() = }')
    print(f'{a1D = }')

@exec_func_info
def numpy_append() -> None:
    print(f'{id(a1D) = :X}h')
    print(f'{a1D = }')
    a1D_new = np.append(a1D,32)
    print(f'{id(a1D_new) = :X}h')
    print(f'{a1D_new = }')


def main() -> None:
    #content_of_numpy()
    #numpy_version()
    numpy_array()
    numpy_append()

if __name__ == '__main__':
    main()

