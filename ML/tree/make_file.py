import pandas as pd


risk_files01 = pd.read_csv("../../created_files/riskCSVs/Age_Band_of_Driver_Risk.csv")
risk_files02 = pd.read_csv("../../created_files/riskCSVs/Sex_of_Driver_Risk.csv")
risk_files03 = pd.read_csv("../../created_files/riskCSVs/Urban_or_Rural_Area_Risk.csv")
risk_files04 = pd.read_csv("../../created_files/riskCSVs/Vehicle_Type_Risk.csv")

risks = [risk_files01, risk_files02, risk_files03, risk_files04]

merged = pd.read_csv("../../created_files/merged.csv", low_memory=False)
merged_df = pd.DataFrame(merged)

columns_to_drop = [
    "Accident_Index", "Location_Easting_OSGR", "Location_Northing_OSGR", "Longitude","Latitude", 
     "Police_Force", "Accident_Severity", "Number_of_Vehicles", "Number_of_Casualties", "Date", "Day_of_Week", 
     "Time", "Local_Authority_(District)", "Local_Authority_(Highway)", "1st_Road_Class", "1st_Road_Number", 
     "Road_Type", "Speed_limit", "Junction_Detail", "Junction_Control", "2nd_Road_Class", "2nd_Road_Number",
     "Pedestrian_Crossing-Human_Control", "Pedestrian_Crossing-Physical_Facilities", "Light_Conditions", 
     "Weather_Conditions", "Road_Surface_Conditions", "Special_Conditions_at_Site", "Carriageway_Hazards", 
     "Did_Police_Officer_Attend_Scene_of_Accident", "LSOA_of_Accident_Location", 
     "Vehicle_Reference_x","Casualty_Reference", "Casualty_Class","Sex_of_Casualty", "Age_of_Casualty", 
     "Age_Band_of_Casualty", "Casualty_Severity", "Pedestrian_Location","Pedestrian_Movement", "Car_Passenger",
     "Bus_or_Coach_Passenger", "Pedestrian_Road_Maintenance_Worker", "Casualty_Type", "Casualty_Home_Area_Type",
     "Vehicle_Reference_y", "Towing_and_Articulation", "Vehicle_Manoeuvre",
     "Vehicle_Location-Restricted_Lane", "Junction_Location", "Skidding_and_Overturning", 
     "Hit_Object_in_Carriageway", "Vehicle_Leaving_Carriageway","Hit_Object_off_Carriageway", 
     "1st_Point_of_Impact", "Was_Vehicle_Left_Hand_Drive?", "Journey_Purpose_of_Driver", 
     "Age_of_Driver", "Engine_Capacity_(CC)", "Propulsion_Code", "Age_of_Vehicle", 
     "Driver_IMD_Decile", "Driver_Home_Area_Type"
     ]

merged_df.drop(columns_to_drop, axis=1, inplace=True)


columns = []
rows = []

for file in risks:
    output = []
    
    columns.append(file.columns[0])
    
    c0 = file.values[:, 0]
    c1 = file.values[:, 1]

    maps = dict(zip(c0, c1))

    for risk in merged[file.columns[0]]:
        try:
            output.append(maps[risk])
        except:
            output.append("N/A")
    rows.append(output)

data = dict(zip(columns, rows))

ML_ready = pd.DataFrame(data)

# print(ML_ready)


risky = []

risky_math = {"high":1, "moderate":0.5, "low": -1, "N/A": 0}

for index, row in ML_ready.iterrows():
    risk = 0
    for r in row.values.tolist():
        risk += risky_math[r]
    
    if risk > 0:
        risk = 0
    else:
        risk = 1
    risky.append(risk)

merged_df.insert(0, "Risk", risky)


merged_df.to_csv('../../created_files/decision_tree_data.csv')
