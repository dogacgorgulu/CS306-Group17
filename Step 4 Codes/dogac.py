from connect import connectionCreator
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from os.path import join
import matplotlib.ticker as ticker

mydb = connectionCreator()

################################################################################

first_query = "SELECT * FROM deaths"

first_df = pd.read_sql(first_query, mydb)

grouped_data = first_df.groupby('the_year')['from_earthquakes'].sum().reset_index()

years = ["1950", "1960", "1970", "1980", "1990", "2000", "2010", "2020"] #years
first_values = [] #deaths

for row in grouped_data.index:
    first_values.append(grouped_data['from_earthquakes'][row])

plt.title("Total Deaths from Earthquakes by Year")

plt.xlabel("Decades")
plt.ylabel("Deaths")

plt.bar(years, first_values)
plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
plt.savefig("figures/Total Deaths from Earthquakes by Year.png")
plt.close()

################################################################################

second_df = pd.read_sql(first_query, mydb)

grouped_data2 = second_df.groupby('the_year')['from_landslides'].sum().reset_index()

second_values = [] #deaths

for row in grouped_data2.index:
    second_values.append(grouped_data2['from_landslides'][row])

plt.title("Total Deaths from Landslides by Year")

plt.xlabel("Decades")
plt.ylabel("Deaths")

plt.bar(years, second_values)
plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
plt.savefig("figures/Total Deaths from Landslides by Year.png")
plt.close()

mydb.close() 
