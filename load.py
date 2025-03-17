import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print(df.head())

    print('-----data.info-----')
    print(df.info())

   

    return df