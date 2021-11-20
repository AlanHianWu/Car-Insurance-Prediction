from datetime import time
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['agg.path.chunksize'] = 10000

mergedFile = pd.read_csv("created_files/merged.csv", encoding="utf-8", low_memory=False)

column = [
    "Accident_Index", "Location_Easting_OSGR", "Location_Northing_OSGR", "Longitude","Latitude", 
     "Police_Force", "Accident_Severity", "Number_of_Vehicles", "Number_of_Casualties", "Date", "Day_of_Week", 
     "Time", "Local_Authority_(District)", "Local_Authority_(Highway)", "1st_Road_Class", "1st_Road_Number", 
     "Road_Type", "Speed_limit", "Junction_Detail", "Junction_Control", "2nd_Road_Class", "2nd_Road_Number",
     "Pedestrian_Crossing-Human_Control", "Pedestrian_Crossing-Physical_Facilities", "Light_Conditions", 
     "Weather_Conditions", "Road_Surface_Conditions", "Special_Conditions_at_Site", "Carriageway_Hazards", 
     "Urban_or_Rural_Area", "Did_Police_Officer_Attend_Scene_of_Accident", "LSOA_of_Accident_Location", 
     "Vehicle_Reference_x","Casualty_Reference", "Casualty_Class","Sex_of_Casualty", "Age_of_Casualty", 
     "Age_Band_of_Casualty", "Casualty_Severity", "Pedestrian_Location","Pedestrian_Movement", "Car_Passenger",
     "Bus_or_Coach_Passenger", "Pedestrian_Road_Maintenance_Worker", "Casualty_Type", "Casualty_Home_Area_Type",
     "temp", "Vehicle_Reference_y", "Vehicle_Type", "Towing_and_Articulation", "Vehicle_Manoeuvre",
     "Vehicle_Location-Restricted_Lane", "Junction_Location", "Skidding_and_Overturning", 
     "Hit_Object_in_Carriageway", "Vehicle_Leaving_Carriageway","Hit_Object_off_Carriageway", 
     "1st_Point_of_Impact", "Was_Vehicle_Left_Hand_Drive?", "Journey_Purpose_of_Driver", "Sex_of_Driver", 
     "Age_of_Driver", "Age_Band_of_Driver", "Engine_Capacity_(CC)", "Propulsion_Code", "Age_of_Vehicle", 
     "Driver_IMD_Decile", "Driver_Home_Area_Type"
     ]

merge_df = pd.DataFrame(mergedFile)

print("output")
print("="*300)

output = merge_df["Time"].value_counts()

print(output)

results = output.to_list()
times = output.index.to_list()


# bars = pd.DataFrame({'Vehicle Type':[], 'frequency':output.tolist()})

# times = pd.to_datetime(merge_df["Time"], format='%H:%M').dt.hour

# print(times)


scatter = pd.DataFrame({'Time':times,'results': results})
scatter.plot.scatter(x='Time', y='results')

# bars.plot.bar(x='Vehicle Type', y='frequency', ylim=(0, 3000000)) #rot=0) #ylim=(0, 3000000))


# plt.ticklabel_format(useOffset=False, style='plain', axis='y')


plt.show()