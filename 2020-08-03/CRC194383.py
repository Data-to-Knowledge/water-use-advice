# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:25:41 2019

@author: michaelek
"""
import os
from allotools import AlloUsage
import pandas as pd
from pdsql import mssql
from gistools import vector
from matplotlib.pyplot import show

pd.options.display.max_columns = 10

from_date = '1970-07-01'
to_date = '2020-06-30'

output_path = r'C:\ecan\git\water-use-advice\2020-08-03'

csv1 = 'K37-3109.csv'
csv2 = 'K37-3110.csv'

cant_summ_no_hydro = 'cant_summ_no_hydro_2020-07-30.csv'
cant_summ_with_hydro = 'cant_summ_with_hydro_2020-07-30.csv'

cant_allo_no_hydro = 'cant_allo_no_hydro_2020-07-30.csv'
cant_allo_with_hydro = 'cant_allo_with_hydro_2020-07-30.csv'


#cwms = 'Selwyn - Waihora'

# gwaz = ['Rakaia-Selwyn', 'Selwyn-Waimakariri', 'Little Rakaia']


########################################
### Read and plot data

df1 = pd.read_csv(os.path.join(output_path, csv1))

df1['date_time'] = pd.to_datetime(df1['Date'] + ' ' + df1['Time'], dayfirst=True)

df2 = df1.drop(['Date', 'Time'], axis=1)
df2 = df2.drop_duplicates('date_time').sort_values('date_time')


# df2['sec_diff'] = df1['date_time'].diff().dt.seconds
# df2['vol_diff'] = df1['Volume_CuM'].diff()


ts2.to_csv(os.path.join(output_path, cant_summ_with_hydro))
allo1.to_csv(os.path.join(output_path, cant_allo_with_hydro))



df1 = pd.read_csv(os.path.join(output_path, csv2))

df1['date_time'] = pd.to_datetime(df1['Date'] + ' ' + df1['Time'], dayfirst=True)

df2 = df1.drop(['Date', 'Time'], axis=1)
df2 = df2.drop_duplicates('date_time').sort_values('date_time')














