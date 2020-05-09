import pandas as pd
import helper

print ("HELLO!")

df = pd.DataFrame({'A':[1,2,3], 'B':['05-08-2020', '07-04-1776', '08-30-1945']})
print('SplitDate\n---Before---\n', df)
df2 = helper.SplitDate(df, 'B')
print('---After---\n', df2, '\n')

a_list = ['8','4','H']
print('ListToSeries\n---Before---\n', df2)
print('The List:', a_list, '\n')
df3 = helper.ListToSeries(df2, a_list)
print('---After---\n', df3, '\n')