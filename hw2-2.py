import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/jennybc/gapminder/main/inst/extdata/gapminder.tsv', sep='\t')

g = sns.FacetGrid(df, col="continent", height=5)
g.map(plt.scatter, "gdpPercap", "lifeExp")
plt.show()





