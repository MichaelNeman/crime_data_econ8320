# -*- coding: utf-8 -*-
"""
@author: mneman
"""
import pandas as pd
import numpy as np

#Changes to directory or file format will require adjustments to the pd.read functions. 

#-----read strata files into dataframes-------

incident_file = pd.read_stata(r"C:\Users\mnema\Documents\School\ECON_8320\Project\data_files\incident.dta", convert_categoricals=False)
household_file = pd.read_stata(r"C:\Users\mnema\Documents\School\ECON_8320\Project\data_files\household.dta", convert_categoricals=False)
person_file = pd.read_stata(r"C:\Users\mnema\Documents\School\ECON_8320\Project\data_files\person.dta", convert_categoricals=False)

#-----select columns of interest for each dataframe--------

incident_file = incident_file[["IDHH", "IDPER", "YEAR", "V4014", "V4015", "V4049", "V4050", 
                               "V4051", "V4052","V4053", "V4054", "V4055", "V4056", "V4060", "V4061", "V4069", "V4070",
                               "V4078", "V4079", "V4081", "V4094", "V4095", "V4096", "V4097", "V4098", "V4100", "V4102", 
                               "V4105","V4106", "V4482A", "V4482B", "V4483","V4484", "V4485", "V4528", "V4529"]]

person_file1 = person_file[["IDHH", "YEAR", "V2120", "V3013", "V3015", "V3017", "V3020", "V3022", "V3023A", "V3074",
                            "V3075", "V3076", "V3078", "V3083", "V3084", "V3085", "V3086"]]

household_file = household_file[["IDHH", "YEAR", "V2026"]]

#-----convert missing data to NaN, household_file-----

household_file.loc[household_file["V2026"] == 98, "V2026"] = np.nan
household_file.loc[household_file["V2026"] == 99, "V2026"] = np.nan
household_file.replace(r'^\s*$', np.nan, regex = True) #use regex to convert empty value to Nan

#-----convert missing data to NaN, person_file1-----

person_file1.replace(r'^\s*$', np.nan, regex = True)

#column_list1 contains columns that use 98,99,-1 as missing data codes in person_file1
#loop through these columns to replace missing data codes with NaN

column_list1 = ["V3013", "V3020", "V3023A", "V3074"] 
for col in column_list1:
    person_file1.loc[person_file1[col] == 98, col] = np.nan
        
for col in column_list1:
    person_file1.loc[person_file1[col] == 99, col] = np.nan

for col in column_list1:
    person_file1.loc[person_file1[col] == -1, col] = np.nan

#column_list2 contains columns that use 8,9,-2,-1 as missing data codes in person_file1
#loop through these columns to replace missing data codes with NaN

column_list2 = ["V2120", "V3015", "V3017", "V3022", "V3075", "V3076", "V3078", "V3083", "V3084", "V3085", "V3086"]

for col in column_list2:
    person_file1.loc[person_file1[col] == 8, col] = np.nan
        
for col in column_list2:
    person_file1.loc[person_file1[col] == 9, col] = np.nan

for col in column_list2:
    person_file1.loc[person_file1[col] == -1, col] = np.nan

for col in column_list2:
    person_file1.loc[person_file1[col] == -2, col] = np.nan
    
#only column V2120 in person_file1 uses '7' as a missing data code
person_file1.loc[person_file1["V2120"] == 7, "V2120"] = np.nan

#-----convert missing data to NaN, incident_file-----

incident_file.replace(r'^\s*$', np.nan, regex = True)

#column list3 contains columns that use 8,9,-1,-2 as missing data codes in incident_file
column_list3 = ["V4049", "V4050", "V4051", "V4052","V4053", "V4054", "V4055", 
                "V4056", "V4060", "V4061", "V4069", "V4070", "V4078", "V4079", "V4081", "V4094",
                "V4095", "V4096", "V4097", "V4098", "V4100", "V4102", "V4105","V4106", "V4483", 
                "V4484", "V4485" ]

for col in column_list3:
    incident_file.loc[incident_file[col] == 8, col] = np.nan
        
for col in column_list3:
    incident_file.loc[incident_file[col] == 9, col] = np.nan

for col in column_list3:
    incident_file.loc[incident_file[col] == -1, col] = np.nan

for col in column_list3:
    incident_file.loc[incident_file[col] == -2, col] = np.nan

#column_list4 contains columns that use 98,99,-1,-2 as missing data codes in incident file  

column_list4 = ["V4014", "V4482A", "V4482B", "V4528", "V4529"]

for col in column_list4:
    incident_file.loc[incident_file[col] == 98, col] = np.nan
        
for col in column_list4:
    incident_file.loc[incident_file[col] == 99, col] = np.nan

for col in column_list4:
    incident_file.loc[incident_file[col] == -1, col] = np.nan

for col in column_list4:
    incident_file.loc[incident_file[col] == -2, col] = np.nan

#column V4015 used 9998, 9999 as missing data codes

incident_file.loc[incident_file['V4015'] == 9998, 'V4015'] = np.nan

incident_file.loc[incident_file['V4015'] == 9999, 'V4015'] = np.nan


#-----rename columns for easier identification-----

incident_file = incident_file.rename({"IDHH":"IDHH", "IDPER":"IDPR", "YEAR":"YEAR", "V4014":"month_occured", "V4015":"year_occured", 
                                      "V4049":"had_weapon", "V4050":"weapon_type", "V4051":"hand_gun", "V4052":"other_gun","V4053":"knife",
                                      "V4054":"sharp_object", "V4055":"blunt_object", "V4056":"weapon_other", "V4060":"hit_attack",
                                      "V4061":"attack_attempt", "V4069":"sex_contact_force", "V4070":"sex_contact_no_force",
                                      "V4078":"threat_rape", "V4079":"threat_kill", "V4081":"threat_sex_assualt", "V4094":"raped",
                                      "V4095":"rape_attempt", "V4096":"sex_assault", "V4097":"shot", "V4098":"shot_missed",
                                      "V4100":"knife_attack", "V4102":"hit_object", "V4105":"hit_slapped","V4106":"grabbed",
                                      "V4482A":"industry_code", "V4482B":"occupation_code", "V4483":"job_location","V4484":"occured_at_work",
                                      "V4485":"work_days_nights", "V4528":"crime_code_old", "V4529":"crime_code_new"}, axis = 1)

person_file1 = person_file1.rename({"IDHH":"IDHH", "YEAR":"YEAR", "V2120":"public_housing", "V3013":"Age", "V3015":"marital_status",
                                    "V3017":"sex", "V3020":"ed_attain", "V3022":"race", "V3023A":"race_recode", "V3074":"job_desc",
                                    "V3075":"emp_sector", "V3076":"work_urban_sub_rural", "V3078":"university_employee", "V3083":"citizen_status",
                                    "V3084":"sexual_orientation", "V3085":"birth_gender_ident", "V3086":"current_gender_ident"}, axis = 1)

household_file = household_file.rename({"IDHH":"IDHH", "YEAR":"YEAR", "V2026":"household_income"}, axis = 1)

#-----merge data files-----

crime_data = household_file.merge(person_file1, left_on='IDHH', right_on='IDHH')
crime_data = crime_data.merge(incident_file, left_on='IDHH', right_on='IDHH')

#-----filter data set to only include incidents in the workplace-----

crime_data = crime_data[crime_data['occured_at_work'] == 1]

#-----export cleaned dataframe to csv-----

crime_data.to_csv(r"C:\Users\mnema\Documents\School\ECON_8320\Project\data_files\crime_data.csv", header = True, sep = ',')



