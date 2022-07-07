import pandas as pd
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt 
plt.style.use('seaborn')
df=pd.read_csv("/content/drive/MyDrive/Big Data Assignment 1 Data/bristol-air-quality-data.csv",sep=';')
df['Date Time'] = pd.to_datetime(df['Date Time'], errors='coerce')
df['Dates'] = pd.to_datetime(df['Date Time']).dt.date
df['Time'] = pd.to_datetime(df['Date Time']).dt.time
def task3_b():
  table = pd.pivot_table(data=df,index='Location',values='NO2',aggfunc=np.sum)
  #bar graph
  fig, ax = plt.subplots()
  plt.rcParams["figure.figsize"] = (15,6)
  plt.bar(table.index,table['NO2'])

  #xticks 
  plt.xticks(rotation=70) 

  #x-axis labels 
  plt.xlabel('States') 

  #y-axis labels 
  plt.ylabel('CO2 Level') 

  #plot title 
  plt.title('CO2 Level Region Wise') 

  #save plot 
  plt.show()
  image_format = 'svg'
  image_name = 'Visualization2.svg'

  fig.savefig(image_name, format=image_format, dpi=3000)
task3_b()