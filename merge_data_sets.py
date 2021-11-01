import pandas as pd

accidents = pd.read_csv("Accidents0515.csv", error_bad_lines=False)

casualties = pd.read_csv("Casualties0515.csv", error_bad_lines=False)

vehicles = pd.read_csv("Vehicles0515.csv", error_bad_lines=False)

data = pd.merge(accidents, casualties, on=['Accident_Index'], copy=False).merge(vehicles, on=['Accident_Index'], copy=False)

data = data.drop(columns=['Propulsion_Code', 'Pedestrian_Road_Maintenance_Worker', 'Police_Force', 'Number_of_Casualties', 'Local_Authority_(District)', 'Local_Authority_(Highway)', 'Carriageway_Hazards', 'Special_Conditions_at_Site', 'Did_Police_Officer_Attend_Scene_of_Accident', 'Age_of_Casualty', 'Age_Band_of_Casualty', 'Pedestrian_Movement'])

data.to_csv("merged.csv", index=False)
