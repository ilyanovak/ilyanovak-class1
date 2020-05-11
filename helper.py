import pandas as pd
import numpy as np

def SplitDate(df, column):
    '''
    Splits a datetime column into Year, Month, and Day columns

    Params:
        df (pandas.DataFrame) which contains column param
        column (pandas.Series) with values in datetime type

    Returns:
        Copy of original dataframe with original column removed and new
        Year, Month, and Day columns
    '''
    X = df.copy()
    X[column] = pd.to_datetime(X[column])
    X['Year'] = X[column].dt.year
    X['Month'] = X[column].dt.month
    X['Day'] = X[column].dt.day
    X = X.drop(columns=column)
    return X
    
def ListToSeries(df, a_list):
    '''
    Converts a list variable into a pandas Series and adds it as a column
    to a pandas data frame

    Params:
        df (pandas.DataFrame) to which the new Series is added
        a_list (python list type) which is added to df

    Returns:
        Original df with added column with contents of a_list
    '''
    X = df.copy()
    X['newlist'] = pd.Series(a_list)
    return X

class SplitDateClass:
    def __init__(self, df, column):
        self.df = df
        self.column = column
        self.year=np.NaN,
        self.month=np.NaN,
        self.day=np.NaN,

    def Split(self):
        X = self.df
        X[self.column] = pd.to_datetime(X[self.column])
        self.year = X[self.column].dt.year
        self.month = X[self.column].dt.month
        self.day = X[self.column].dt.day