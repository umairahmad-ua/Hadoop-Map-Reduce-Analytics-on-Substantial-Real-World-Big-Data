#!/usr/bin/python
import sys

dict1 ={"188" :"AURN Bristol Centre","203":"Brislington Depot",
'206' : 'Rupert Street',
'209' : 'IKEA M32',
'213' : 'Old Market',
'215' : 'Parson Street School',
'228' : 'Temple Meads Station',
'270' : 'Wells Road',
'271' : 'Trailer Portway P&R',
'375' : 'Newfoundland Road Police Station',
'395' : "Shiner's Garage",
'452' : 'AURN St Pauls',
'447' : 'Bath Road',
'459' : 'Cheltenham Road \ Station Road',
'463' : 'Fishponds Road',
'481' : 'CREATE Centre Roof',
'500' : 'Temple Way',
'501' : 'Colston Avenue'
}
lst=[]
for line in sys.stdin:
    line = line.strip()
    lst.append(line)
count=0
str1=[]
for index,x in enumerate(lst):
  if(index>0):
    temp=x.split(';')
    if(temp[4]!="" and temp[17!=""]):
      if(temp[4] in dict1):
        if(dict1[temp[4]]!=temp[17]):
          print(temp)