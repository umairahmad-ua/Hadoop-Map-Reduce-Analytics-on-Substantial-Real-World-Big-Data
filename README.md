# Hadoop-Map-Reduce-Analytics-on-Substantial-Real-World-Big-Data
1.8 GB of Big data from 18 monitoring stations in Bristol where I have modeled the problem and applied the cleanse, normalize, shard, map, and query on big data. understand the data cleansing processes by writing python scripts to process and convert the data to the first (cleansed) JSON data objects. Visualize the data to translate information into a visual context. Used NoSQL, Hadoop, and Pandas to apply analytics on air quality data.

The Input Data

The following ZIP file provides data ranging from 2004 to 03 February 2020 taken from 18 monitoring stations in and around Bristol.
Monitors come and go and may suffer downtimes, so the data isn't complete for all stations at all times.

Download & save the data file [bristol-air-quality-data.zip](https://fetstudy.uwe.ac.uk/~p-chatterjee/2020-21/modules/dmf/assignment/bristol-air-quality-data.zip):

Note the following:

There are 18 stations (monitors):

- 188 => 'AURN Bristol Centre', 203 => 'Brislington Depot', 206 => 'Rupert Street',
- 209 => 'IKEA M32',
- 213 => 'Old Market',
- 215 => 'Parson Street School', 228 => 'Temple Meads Station', 270 => 'Wells Road',
- 271 => 'Trailer Portway P&R',
- 375 => 'Newfoundland Road Police Station', 395 => "Shiner's Garage",
- 452 => 'AURN St Pauls',
- 447 => 'Bath Road',
- 459 => 'Cheltenham Road \ Station Road', 463 => 'Fishponds Road',
- 481 => 'CREATE Centre Roof', 500 => 'Temple Way',
- 501 => 'Colston Avenue'

Each line represents one reading from a specific detector. Detectors take one reading every hour. If you examine the file using a programming editor, Notepad++ can handle the job, you can see that the first row gives headers and


there are another 1408379 (1.4 million+) rows (lines). There are 23 data items (columns) per line.
The schema is given below:

- measure	Desc	unit
- Date Time	Date and time of measurement	datetime
- NOx	Concentration of oxides of nitrogen	μg/m3
- NO2	Concentration of nitrogen dioxide	μg/m3
- NO	Concentration of nitric oxide	μg/m3
- SiteID	Site ID for the station	integer
- PM10	Concentration of particulate matter <10 micron diameter	μg/m3
- NVPM10	Concentration of non - volatile particulate matter <10 micron diameter	μg/m3
- VPM10	Concentration of volatile particulate matter
- <10 micron diameter	μg/m3
- NVPM2.5	Concentration of non volatile particulate matter <2.5 micron diameter	μg/m3
- PM2.5	Concentration of particulate matter <2.5 micron diameter	μg/m3
- VPM2.5	Concentration of volatile particulate matter
- <2.5 micron diameter	μg/m3
- CO	Concentration of carbon monoxide	mg/m3
- O3	Concentration of ozone	μg/m3
- SO2	Concentration of sulphur dioxide	μg/m3
- Temperature	Air temperature	°C
- RH	Relative Humidity	%
- Air Pressure	Air Pressure	mbar
- Location	Text description of location	text
- geo_point_2d	Latitude and longitude	geo point
- DateStart	The date monitoring started	datetime
- DateEnd	The date monitoring ended	datetime
- Current	Is the monitor currently operating	text
- Instrument Type	Classification of the instrument	text

## Task1 scripts to carry out the following.
- a.	Crop the file to delete any records before 00:00 01 Jan 2010.
- b.	Filter for and remove any dud records where there is no value for SiteID or there is a mismatch between SiteID and Location.
(This script should print the lines number and mismatch field values for each dud record.)
- c.	Process the file and replace any empty fields with the value: NaN

This processing is implemented on Hadoop. I have writed Mapper and Reducer. (for Hadoop version)

## Task 2 script carry out the following.
- a.	Return the station number, station name, and date/time of the highest recorded value of carbon monoxide (CO) found in the dataset.
 
- b.	Return the mean values of NO2 & NO by each station for the year 2019 for readings taken on or near 08:00 hours (peak traffic intensity).
- c.	Extend the previous query to show these values for all stations in the years 2010 to 2019.
- d.	Write two more queries according to your aspects that can be more informative for us.

