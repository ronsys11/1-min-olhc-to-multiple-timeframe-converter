import pandas as pd
import numpy as np

df = pd.read_csv("D:\Historical data\BANK_NIFTY_data\BNF_2010.csv")
df['Time'] = df['Time'].apply(lambda x: x.replace(':', ''))
df['Date']= df['Date'].map(str)
df['time'] = df['Date'] + df['Time'] 
df.time = pd.to_datetime(df.time, format="%Y%m%d%H%M")
df = df.set_index("time")
t = df.groupby(pd.Grouper(freq='15min')).agg({"Open": "first", 
                                             "Close": "last", 
                                             "Low": "min", 
                                             "High": "max"})
t.columns = ["open", "close", "low", "high"]
print(t)
t.to_csv('D:\\Historical data\\BANK_NIFTY_data\\BNF_2010_15mins.csv')