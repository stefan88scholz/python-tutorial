# https://pandas.pydata.org/docs/user_guide/dsintro.html#series
# https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series

import pandas as pd
import numpy as np

# Series is a one-dimensional labeled array capable of holding any data type (integers, strings, python objects, etc.)
# The axis labels are collectively referred to as the index.

def print_different_series() -> None:
    pd_series : pd.Series = pd.Series(5,name='scalar_value')
    print(pd_series)
    print(type(pd_series))
    print(f'{'-':-<100}')
    pd_series: pd.Series = pd.Series(['Jan', 'Feb', 'March', 'April'], index=['First','Second','Third','Fourth'])
    print(pd_series)

def main() -> None:
    print_different_series()

if __name__ == '__main__':
    main()