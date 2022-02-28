import pandas as pd
import numpy as np
import csv

#this block of code will return a the data into Py in a workable format
filename = '2021_pittsburgh_fish_fry_locations.csv'

fields = []
rows = []

#The below data is the entire data set
with open (filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next (csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d"%(csvreader.line_num))
    
print(type(rows))
    
'''
print('Field names are:' + ', '.join(field for field in fields)) #testing 
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%30s"%col,end=" "),
    print('\n')
'''
rows1= pd.DataFrame(rows, columns=('validated', 'venue_name', 'venue_type', 'venue_address', 
                                   'website', 'events', 'etc', 'menu_url', 'menu_text', 
                                   'venue_notes', 'phone', 'email', 'homemade_pierogies', 
                                   'take_out', 'alcohol', 'lunch', 'handicap', 'publish',
                                   'id', 'latitude', 'longitude'))
rawfishData = rows1.fillna("Not Available") #Replace NaNs with something to tell user the data is missing
print(rawfishData.describe()) #testing that NaNs are indeed gone

#rawfishData is a DF with NaNs replaced with "Not Available"
#fields and rows are lists without the NaNs filled in


#The below block of data will be used to get the data of interest for our application
print(fields)
rawData = []
    
for line in rows:
    line1 = line[:-1]
    line2 = str(line1)
    line_new = line2.split(',')
    rawData.append(line_new[1]) #name of venue
    rawData.append(line_new[2]) #venue type
    rawData.append(line_new[3]) #venue address
    rawData.append(line_new[4]) #venue website
    rawData.append(line_new[5]) # events is col 5 but the strs are so long you can't print with anyother information
    rawData.append(line_new[7]) #menu website
    rawData.append(line_new[14]) #if there is alcohol 
    rawData.append(line_new[19]) #latitude
    rawData.append(line_new[20]) #longitude
    print('{:<50s} {:<10s} {:<10s} {:<20s}'.format(line_new[1], line_new[2], line_new[3], line_new[4])) #snapshot of rawData

#print(rawData) #makeing sure rawData has all the selcted infromation

#The below code will convert rawData and our data of intrest to a data frame and remove NaNs

rawData_DF = pd.DataFrame(rawData)
rawData_clean = rawData_DF.fillna ("Not Available")
## Mary comment: This is only printing one column, not 21 columns 
#print(rawData_clean) #testing to see if it workedy

## Return open date and time

TimeDate = rawfishData['events'] 
print(TimeDate)
##print(TimeDate[1].split(","))

def DateTime(i):
    i in rawfishData['venue_name'].values
    if True:
        Sched=rawfishData.loc[rawfishData['venue_name'] == i, 'events']
        Sched_str = Sched.to_string() 
        print(i, 'is serving fish at:\n', Sched_str.split(","))
    if False: 
        print('Bad format!')
    
    
i = input('Enter the venue name:')
DateTime(i) 



##Map stuff 

import geopandas as gpd
from geopandas import GeoDataFrame 
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon 
import descartes 

neighborhoods = gpd.read_file('/Users/kubin/MedPyth/pittsburghpaneighborhoods-/')

fig,ax = plt.subplots(figsize = (15,15))
neighborhoods.plot(ax = ax) 

df = pd.read_csv('2021_pittsburgh_fish_fry_locations.csv')

geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = GeoDataFrame(df, geometry= geometry)
print(gdf.head()) 

fig,ax = plt.subplots(figsize = (15,15))
neighborhoods.plot(ax = ax, alpha = 0.4, color = 'grey')
gdf.plot(column = 'venue_type', ax = ax, alpha = .5, legend = True, markersize = 50)
plt.xlim(-80.10, -79.90)
plt.ylim(40.36, 40.50)
plt.title('Pittsburgh Fish Fry Spots', fontsize = 16, fontweight = 'bold')
plt.show() 





