import pandas as pd
from collections import defaultdict
df=pd.read_csv("/content/drive/MyDrive/Big Data Assignment 1 Data/bristol-air-quality-data.csv",sep=';')
df['Date Time'] = pd.to_datetime(df['Date Time'], errors='coerce')
df['Dates'] = pd.to_datetime(df['Date Time']).dt.date
df['Time'] = pd.to_datetime(df['Date Time']).dt.time
dict1_no2 = defaultdict(float)
dict1_no = defaultdict(float)
def task2_c():
  count_dict1_no2 = defaultdict(float)
  count_dict1_no = defaultdict(float)
  for index, row in df.iterrows():
    date=str(row['Dates']).split("-")
    time=str(row["Time"]).split(":")
    if(str(date[0])!="NaT"):
      if(2010<=int(date[0]) <=2019):
        if(int(time[0])>7 and int(time[0])<10):
          if(str(row["NO2"])!="nan" and str(row["Location"])!="nan"):
            dict1_no2[row["Location"]]+=float(row["NO2"])
            count_dict1_no2[row["Location"]]+=1
          if(str(row["NO"])!="nan" and str(row["Location"])!="nan"):
            dict1_no[row["Location"]]+=float(row["NO"])
            count_dict1_no[row["Location"]]+=1
  for key in dict1_no2:
    dict1_no2[key]=dict1_no2[key]/count_dict1_no2[key]
    dict1_no[key]=dict1_no[key]/count_dict1_no[key]
task2_c()
def task2_d():
  max=0
  min=dict1_no2['Brislington Depot']
  for key in dict1_no2:
    if(max<dict1_no2[key]):
      output=key
    if(min>dict1_no2[key]):
      output2=key
  print("Max NO2, Locations Vise=",output)
  print("Min NO2, Locations Vise=",output2)
task2_d()