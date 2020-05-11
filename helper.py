import pandas as pd

def SplitDate(df, column):  # LR: - I liked how you passed a column param. This way regardles of the name of the column
                            #you can pass it to your helper function and it will do the work. 
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
    X[column] = pd.to_datetime(X[column])  # LR: I suggest you add the "infer_datetime_format=True", I think this help to speed up or it is consider good practice 
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
