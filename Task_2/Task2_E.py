import pandas as pd
from collections import defaultdict
df=pd.read_csv("/content/drive/MyDrive/Big Data Assignment 1 Data/bristol-air-quality-data.csv",sep=';')
df['Date Time'] = pd.to_datetime(df['Date Time'], errors='coerce')
def task2_e():
  df.query('Location in ["Old Market", "AURN St Pauls"]')
task2_e()