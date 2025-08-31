import pandas as pd

def method_read_csv()-> None:
    df_sp500 = pd.read_csv('data/sp500_constituents.csv')
    df_nasdaq_screener_nasdaq: pd.DataFrame = pd.read_csv('data/nasdaq_screener_nasdaq_med_to_mega.csv')
    df_nasdaq_screener_nyse: pd.DataFrame = pd.read_csv('data/nasdaq_screener_nyse_med_to_mega.csv')

    list_nyse_sp500: list[str] = list()
    list_nasdaq_sp500: list[str] = list()
    list_no_match: list[str] = list()

    for symbol in df_sp500['Symbol']:
        nasdaq_check: pd.DataFrame = df_nasdaq_screener_nasdaq[df_nasdaq_screener_nasdaq['Symbol'] == symbol]
        nyse_check: pd.DataFrame = df_nasdaq_screener_nyse[df_nasdaq_screener_nyse['Symbol'] == symbol]
        if not nasdaq_check.empty:
            list_nasdaq_sp500.append(symbol)
        elif not nyse_check.empty:
            list_nyse_sp500.append(symbol)
        else:
            list_no_match.append(symbol)

    print(list_nasdaq_sp500)
    print(list_nyse_sp500)
    print(list_no_match)

    df_underlying: pd.DataFrame = pd.concat([df_nasdaq_screener_nasdaq, df_nasdaq_screener_nyse])
    df_underlying.columns = df_underlying.columns.str.replace(' ','')
    print(df_underlying)


    list_nasdaq_sp500.clear()
    list_nyse_sp500.clear()
    list_no_match.clear()
    print(df_underlying.columns)
    for row in df_underlying.itertuples():
        nasdaq_check: pd.DataFrame = df_nasdaq_screener_nasdaq[df_nasdaq_screener_nasdaq['Symbol'] == row.Symbol]
        nyse_check: pd.DataFrame = df_nasdaq_screener_nyse[df_nasdaq_screener_nyse['Symbol'] == row.Symbol]
        if not nasdaq_check.empty:
            list_nasdaq_sp500.append(row.Symbol)
        elif not nyse_check.empty:
            list_nyse_sp500.append(row.Symbol)
        else:
            list_no_match.append(row.Symbol)
        print(f'Market Cap: {(round((row.MarketCap / 1_000_000),2)):.2f}')

    print(list_nasdaq_sp500)
    print(list_nyse_sp500)
    print(list_no_match)

def main() -> None:
    method_read_csv()

if __name__ == '__main__':
    main()
