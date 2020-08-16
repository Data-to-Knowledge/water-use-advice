# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:25:41 2019

@author: michaelek
"""
import os
import pandas as pd
from pdsql import mssql
from matplotlib.pyplot import show

pd.options.display.max_columns = 10

date_col = 'Date_Time_Readings'

output_path = r'C:\ecan\git\water-use-advice\2020-08-17'

csv1 = 'L37-0812-m1.csv'
csv2 = 'L37-0812-m2.csv'

csv1_out = 'L37-0812-m1_fix.csv'
csv2_out = 'L37-0812-m2_fix.csv'


########################################
### Read and plot data

## Wap 1
df1 = pd.read_csv(os.path.join(output_path, csv1))

df1[date_col] = pd.to_datetime(df1['Date'] + ' ' + df1['Time'], dayfirst=True)

df2 = df1.drop(['Date', 'Time', 'GLOBAL.Flow1', 'GLOBAL.waterlevel'], axis=1)
df2 = df2.drop_duplicates(date_col).sort_values(date_col)

df2.rename(columns={'GLOBAL.Volume1': 'Acc'}, inplace=True)

df3 = df2.copy()
df3['sec_diff'] = df3[date_col].diff().dt.seconds
df3['vol_diff'] = df3['Acc'].diff()

print(any(df3['vol_diff'] < 0))

df2.set_index(date_col, inplace=True)
df2.plot()
show()

df2.to_csv(os.path.join(output_path, csv1_out))


## Wap 2
df1 = pd.read_csv(os.path.join(output_path, csv2))

df1[date_col] = pd.to_datetime(df1['Date'] + ' ' + df1['Time'], dayfirst=True)

df2 = df1.drop(['Date', 'Time', 'GLOBAL.Flow2', 'GLOBAL.waterlevel'], axis=1)
df2 = df2.drop_duplicates(date_col).sort_values(date_col)

df2.rename(columns={'GLOBAL.Volume2': 'Acc'}, inplace=True)

df3 = df2.copy()
df3['sec_diff'] = df3[date_col].diff().dt.seconds
df3['vol_diff'] = df3['Acc'].diff()

print(any(df3['vol_diff'] < 0))

df2.set_index(date_col, inplace=True)
df2.plot()
show()

df2.to_csv(os.path.join(output_path, csv2_out))











