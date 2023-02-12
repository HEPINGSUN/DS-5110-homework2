import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/jennybc/gapminder/main/inst/extdata/gapminder.tsv', sep='\t')

g = sns.FacetGrid(df, col="continent", height=5)
g.map(plt.scatter, "gdpPercap", "lifeExp")
plt.show()
# In general, the higher the GDP, the longer the average life expectancy.
# However, there are some exceptions in that some low-income countries also have high life expectancy.





