import pandas as pd
from collections import defaultdict
df=pd.read_csv("/content/drive/MyDrive/Big Data Assignment 1 Data/bristol-air-quality-data.csv",sep=';')
df['Date Time'] = pd.to_datetime(df['Date Time'], errors='coerce')
df['Dates'] = pd.to_datetime(df['Date Time']).dt.date
df['Time'] = pd.to_datetime(df['Date Time']).dt.time
def task2_a():
  max=0
  i=0
  for index,x in enumerate(df['CO']):
    if(x!='NaN'):
      if(max<x):
        max=x
        i=index
  print(df.iloc[i,[0,4,17]])
task2_a()