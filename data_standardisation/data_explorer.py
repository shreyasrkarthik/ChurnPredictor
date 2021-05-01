import pandas as pd

def get_column_counts(file_path):
    df = pd.read_csv(file_path)
    return dict(df.count())

def get_column_types(file_path):
    df = pd.read_csv(file_path)
    return dict(df.dtypes)



