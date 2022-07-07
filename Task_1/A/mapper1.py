#!/usr/bin/python
import sys
import os

lst=[]
for line in sys.stdin:
    line = line.strip()
    lst.append(line)

  
for index,x in enumerate(lst):
  if(index>0):
    temp=x.split(';')
    temp2=temp[0].split('-')
    temp2[0]=temp2[0].replace('"',"")
    if(temp2[0]!=""):
        if(int(temp2[0])>2010):
            print(index,x)