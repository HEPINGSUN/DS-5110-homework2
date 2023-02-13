import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/jennybc/gapminder/main/inst/extdata/gapminder.tsv', sep='\t')

g = sns.FacetGrid(df, col="continent", height=5, sharex=False)
g.map(plt.scatter, "gdpPercap", "lifeExp")
g.set(xlim=(0, 60000))

# Create a copy of the data frame for the log-scale plot
df_log = df.copy()
df_log["gdpPercap"] = np.log(df_log["gdpPercap"])

g_log = sns.FacetGrid(df_log, col="continent", height=5, sharex=False)
g_log.map(plt.scatter, "gdpPercap", "lifeExp")

plt.show()



