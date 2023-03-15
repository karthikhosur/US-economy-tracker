import pandas as pd


df = pd.read_csv('data.csv')


def get_data(query):
    if query == "fed_rate_basic":

        df_fed_rate_basic = df[['Date', 'Type', 'Rate']]
        df_all = df[['Date', 'Type', 'Rate',
                    'open', 'low', 'high', 'close', 'volume']]
        return df_fed_rate_basic, df_all
