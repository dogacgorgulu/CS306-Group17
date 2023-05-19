import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="2Dnsn2II2",
  database="natural_disasters"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM natural_disasters.population")

data = cursor.fetchall()

cursor.close()
conn.close()

df = pd.DataFrame(data, columns=["iso_code", "population", "the_year"])

# Get user input for the year
year = int(input("Enter the year: "))

# Filter the data for the specified year
df_year = df[df["the_year"] == year]

# Group data by country code and calculate the total population for each country in the specified year
population_by_country = df_year.groupby("iso_code")["population"].sum().reset_index()

# Sort the data in descending order based on the population
sorted_populations = population_by_country.sort_values(by="population", ascending=False)

# Select the top 10 countries
top_10_countries = sorted_populations.head(10)

# Create a pie chart using Matplotlib
plt.pie(top_10_countries["population"], labels=top_10_countries["iso_code"], autopct='%1.1f%%')
plt.title(f"Top 10 Countries with Highest Population in {year}")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
filename = str('C:/Users/egeoz/OneDrive/Masaüstü/CS306 Step 4/top_10_countries_' + str(year))
#plt.savefig(filename)
plt.show()

conn.close()
