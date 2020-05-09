import pandas as pd

def SplitDate(df, column):
    X = df.copy()
    X[column] = pd.to_datetime(X[column])
    X['Year'] = X[column].dt.year
    X['Month'] = X[column].dt.month
    X['Day'] = X[column].dt.day
    X = X.drop(columns=column)
    return X

def ListToSeries(df, a_list):
    X = df.copy()
    X['newlist'] = pd.Series(a_list)
    return X