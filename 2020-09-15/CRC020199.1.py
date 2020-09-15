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

output_path = r'C:\ecan\git\water-use-advice\2020-09-15'

csv1 = 'L35_0916_original.csv'

csv1_out = 'L35_0916_fix.csv'


########################################
### Read and plot data

## Wap 1
df1 = pd.read_csv(os.path.join(output_path, csv1))

df1['DateTime'] = pd.to_datetime(df1['DateTime'], dayfirst=True)

df2 = df1.rename(columns={'DateTime': date_col, 'Flow': 'Flow (l/s)'})

df2 = df2.dropna().drop_duplicates(date_col).sort_values(date_col)

df2.loc[df2['Flow (l/s)'] < 0, 'Flow (l/s)'] = 0

df2.set_index(date_col, inplace=True)
df2.plot()
show()

df2.to_csv(os.path.join(output_path, csv1_out))









