from connect import connectionCreator
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

mydb = connectionCreator()

#############################################################################################

first_query = "SELECT * FROM economic_damage"

first_df = pd.read_sql(first_query, mydb)

grouped_df = first_df.groupby(['the_year', 'iso_code']).sum().reset_index()

plt.figure(figsize=(10,7)) 

for i, iso_code in enumerate(grouped_df['iso_code'].unique()):
    data = grouped_df[grouped_df['iso_code'] == iso_code]
    plt.scatter(data['the_year'], data['total_economic_damages'])

plt.title('Total Economic Damages by Year')
plt.xlabel('Year')
plt.ylabel('Economic Damages')

plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plt.legend()
plt.savefig("figures/Total Economic Damages by Year.png")

#############################################################################################

grouped_df2 = first_df.groupby(['the_year', 'iso_code']).sum().reset_index()

plt.figure(figsize=(10,7)) 

for i, iso_code in enumerate(grouped_df2['iso_code'].unique()):
    data2 = grouped_df2[grouped_df2['iso_code'] == iso_code]
    plt.scatter(data2['the_year'], data2['total_insured_damages'])

plt.title('Total Insured Damages by Year')
plt.xlabel('Year')
plt.ylabel('Insured Damages')

plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plt.legend()
plt.savefig("figures/Total Insured Damages by Year.png")

#############################################################################################

grouped_df3 = first_df.groupby(['the_year', 'iso_code']).sum().reset_index()

plt.figure(figsize=(10,7)) 

for i, iso_code in enumerate(grouped_df3['iso_code'].unique()):
    data3 = grouped_df3[grouped_df3['iso_code'] == iso_code]
    plt.scatter(data3['the_year'], data3['total_reconstruction_costs'])

plt.title('Total Reconstruction Costs by Year')
plt.xlabel('Year')
plt.ylabel('Reconstruction Costs')

plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plt.legend()
plt.savefig("figures/Total Reconstruction Costs by Year.png")

#############################################################################################

mydb.close() 
