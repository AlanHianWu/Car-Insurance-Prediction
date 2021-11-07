import pandas as pd
import datetime
import sys

print('Reading data from {} to {}...'.format(sys.argv[1], sys.argv[2]))

accidents = pd.read_csv("Accidents0515.csv", error_bad_lines=False)

accidents = accidents[(pd.to_datetime(accidents['Date']).dt.date >= datetime.date(int(sys.argv[1]), 1, 1)) &
                      (pd.to_datetime(accidents['Date']).dt.date < datetime.date(int(sys.argv[2]), 1, 1))]

casualties = pd.read_csv("Casualties0515.csv", error_bad_lines=False)

vehicles = pd.read_csv("Vehicles0515.csv", error_bad_lines=False)

print('Merging Accidents, Casualties and Vehicles...')

data = pd.merge(accidents, casualties, on=['Accident_Index'], copy=False).merge(vehicles, on=['Accident_Index'], copy=False)

data = data.drop(columns=['Propulsion_Code', 'Pedestrian_Road_Maintenance_Worker', 'Police_Force', 'Number_of_Casualties', 'Local_Authority_(District)', 'Local_Authority_(Highway)', 'Carriageway_Hazards', 'Special_Conditions_at_Site', 'Did_Police_Officer_Attend_Scene_of_Accident', 'Age_of_Casualty', 'Age_Band_of_Casualty', 'Pedestrian_Movement'])


import math

def closest_city(latitude, longitude, lat_long_lst):
   closest = lat_long_lst[0]
   for row in lat_long_lst:
      if (math.dist((latitude, longitude), (row[1], row[2])) < 
          math.dist((latitude, longitude), (closest[1], closest[2]))):
         closest = row
   return closest[0]

print('Converting Location coordinates (Latitude & Longitude) to city...')

data_long_lat = data[['Accident_Index', 'Latitude', 'Longitude']].drop_duplicates().values.tolist()

cities_df = pd.read_csv('worldcities.csv')

cities_df = cities_df[cities_df['country'] == 'United Kingdom'][['city', 'lat', 'lng']].values.tolist()

new_data = pd.DataFrame(list(map(lambda x: [x[0], closest_city(x[1], x[2], cities_df)], data_long_lat)),
                        columns = ['Accident_Index', 'City_of_Accident'])


out = pd.merge(data, new_data, on=['Accident_Index']).drop(columns=['Latitude', 'Longitude', 'Location_Easting_OSGR', 'Location_Northing_OSGR'])

print('Writing to merged.csv ...')

out[out['Sex_of_Driver'] != 3].to_csv('merged.csv', index=False)