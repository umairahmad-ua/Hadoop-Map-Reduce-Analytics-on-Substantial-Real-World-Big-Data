#!/usr/bin/python
import sys
import os
lst=[]
output=[]
for line in sys.stdin:
    line = line.strip()
    line=line.replace("'","")
    line=line.replace("[","")
    line=line.replace("]","")
    lst.append(line)
for index_x,x in enumerate(lst):
  temp=x.split(",")
  for index_y,y in enumerate(temp):
    if(str(y)==" "):
      output.append('NAN')
    else:
      output.append(y)

print(output)
