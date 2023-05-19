from connect import connectionCreator
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

mydb = connectionCreator()

first_query = "SELECT * FROM affected"

data = pd.read_sql(first_query, mydb)

data = data.drop("the_year", axis=1)

numerical_data = data.select_dtypes(include=['int64', 'float64'])

corr = numerical_data.corr()

mask = np.triu(np.ones_like(corr, dtype=bool))

f, ax = plt.subplots(figsize=(12, 13))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
plt.title("Affected People Heatmap")

sns.heatmap(corr, mask=mask, cmap="BuPu", vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})

plt.savefig("figures/Affected People Heatmap.png")

mydb.close() 
