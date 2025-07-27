import pandas as pd
from datetime import datetime


def main() -> None:
    my_df: pd.DataFrame = pd.DataFrame(
        data= {'name': ['Stefan','Thomas','Matthias','Jochen'],
               'hometown': ['Berlin', 'Munich', 'Munich', 'Hamburg'],
               'birthplace': ['Munich', 'Munich','Munich', 'Munich'],
               'birthdate': [datetime(1980,5,17), datetime(1979,12,12),
                            datetime(1980,5,1), datetime(1980,7,30)]
               }
    )
    print(f'{my_df = }')
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

if __name__ == '__main__':
    main()

