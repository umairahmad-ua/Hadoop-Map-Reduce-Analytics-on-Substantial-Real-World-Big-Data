import pandas as pd
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt 
plt.style.use('seaborn')
df=pd.read_csv("/content/drive/MyDrive/Big Data Assignment 1 Data/bristol-air-quality-data.csv",sep=';')
df['Date Time'] = pd.to_datetime(df['Date Time'], errors='coerce')
df['Dates'] = pd.to_datetime(df['Date Time']).dt.date
df['Time'] = pd.to_datetime(df['Date Time']).dt.time
def task3_c():
  dff = df[pd.notnull(df['Temperature'])]
  table=pd.pivot_table(dff,index='Dates',values='Temperature') 
  #bar graph
  fig, ax = plt.subplots()
  plt.rcParams["figure.figsize"] = (15,6)
  plt.bar(table.index,table['Temperature'])

  #xticks 
  plt.xticks(rotation=70) 

  #x-axis labels 
  plt.xlabel('Date Time') 

  #y-axis labels 
  plt.ylabel('Temprature') 

  #plot title 
  plt.title('Temprature Relation with DateTiem') 

  #display 
  plt.show()
  #Save Plot as svg
  image_format = 'svg'
  image_name = 'Visualization3.svg'

  fig.savefig(image_name, format=image_format, dpi=1200)
task3_c()