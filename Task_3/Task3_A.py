import pandas as pd
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt 
plt.style.use('seaborn')
df=pd.read_csv("/content/drive/MyDrive/Big Data Assignment 1 Data/bristol-air-quality-data.csv",sep=';')
df['Date Time'] = pd.to_datetime(df['Date Time'], errors='coerce')
df['Dates'] = pd.to_datetime(df['Date Time']).dt.date
df['Time'] = pd.to_datetime(df['Date Time']).dt.time
def task3_a():
  fig = plt.figure(figsize = (20,30))
  ax = fig.gca()
  df.hist(ax=ax,layout=(9,3))
  plt.show()
  image_format = 'svg'
  image_name = 'Visualization1.svg'
  fig.savefig(image_name, format=image_format, dpi=3000)
task3_a()