import pandas as pd


def load_collection(filename):
    store = pd.HDFStore(filename, mode="r")
    df = store['df']
    store.close()
    return df


def store_collection(filename, df):
    store = pd.HDFStore(filename, mode="w")
    store['df'] = df
    store.close()
