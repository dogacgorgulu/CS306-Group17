from connect import connectionCreator
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

mydb = connectionCreator()

first_query = "SELECT I.the_year, I.from_landslides FROM countries C, injuries I WHERE C.country_name = 'Indonesia' AND C.iso_code = I.iso_code"

first_df = pd.read_sql(first_query, mydb)

first_keys = [] #years
first_values = [] #injuries

for row in first_df.index:
    first_keys.append(first_df['the_year'][row])
    first_values.append(first_df['from_landslides'][row])

plt.title("Injuries by landslides in Indonesia")

plt.xlabel("Decades")
plt.ylabel("Injuries")

plt.plot(first_keys, first_values)

plt.savefig("figures/Injuries by landslides in Indonesia.png")

plt.close()

#############################################################################################

second_query = "SELECT I.the_year, I.from_earthquakes FROM countries C, injuries I WHERE C.country_name = 'Indonesia' AND C.iso_code = I.iso_code"

second_df = pd.read_sql(second_query, mydb)

second_keys = [] #years
second_values = [] #injuries

for row in second_df.index:
    second_keys.append(second_df['the_year'][row])
    second_values.append(second_df['from_earthquakes'][row])

plt.title("Injuries by earthquakes in Indonesia")

plt.xlabel("Decades")
plt.ylabel("Injuries")

plt.plot(second_keys, second_values)

plt.savefig("figures/Injuries by earthquakes in Indonesia.png")

plt.close()

#############################################################################################

third_query = "SELECT I.the_year, I.from_earthquakes FROM countries C, injuries I WHERE C.country_name = 'Turkey' AND C.iso_code = I.iso_code"

third_df = pd.read_sql(third_query, mydb)

third_keys = [] #years
third_values = [] #injuries

for row in third_df.index:
    third_keys.append(third_df['the_year'][row])
    third_values.append(third_df['from_earthquakes'][row])

plt.title("Injuries by earthquakes in Turkey")

plt.xlabel("Decades")
plt.ylabel("Injuries")

plt.plot(third_keys, third_values)

plt.savefig("figures/Injuries by earthquakes in Turkey.png")

plt.close()

#############################################################################################

fourth_query = "SELECT I.the_year, I.from_landslides FROM countries C, injuries I WHERE C.country_name = 'Turkey' AND C.iso_code = I.iso_code"

fourth_df = pd.read_sql(fourth_query, mydb)

fourth_keys = [] #years
fourth_values = [] #injuries

for row in fourth_df.index:
    fourth_keys.append(fourth_df['the_year'][row])
    fourth_values.append(fourth_df['from_landslides'][row])

plt.title("Injuries by landslides in Turkey")

plt.xlabel("Decades")
plt.ylabel("Injuries")

plt.plot(fourth_keys, fourth_values)

plt.savefig("figures/Injuries by landslides in Turkey.png")

plt.close()

#############################################################################################

mydb.close() 

