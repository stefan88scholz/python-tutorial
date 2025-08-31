from functions.learndecorators import exec_func_info
import pandas as pd
from datetime import datetime, date

@exec_func_info
def init_dataframe() -> None:
    my_df: pd.DataFrame = pd.DataFrame(
        data= {'name': ['Stefan','Thomas','Matthias','Jochen'],
               'hometown': ['Berlin', 'Munich', 'Munich', 'Hamburg'],
               'birthplace': ['Munich', 'Munich','Munich', 'Munich'],
               'birthdate': [datetime(1980,5,17), datetime(1979,12,12),
                            datetime(1980,5,1), datetime(1980,7,30)]
               }
    )
    print(my_df)
    print(f'{'':-<100}')
    print(f'{my_df.index = }')
    print(f'{'':-<100}')
    print(f'{my_df.columns = }')
    print(f'{'':-<100}')
    print(f'{my_df.keys() = }')
    print(f'{'':-<100}')
    print(f'{my_df.values = }')
    print(f'{'':-<100}')
    print(f'{my_df['name'] = }')

    tmp_dict: dict = {'name': 'Bob', 'age': 32, 'birthplace': 'London', 'birthday': date(1993,4,20)}
    df_from_dict: pd.DataFrame = pd.DataFrame.from_dict(tmp_dict, orient='index')
    print(df_from_dict)

def main() -> None:
    init_dataframe()

if __name__ == '__main__':
    main()

