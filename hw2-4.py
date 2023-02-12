import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

url = "https://raw.githubusercontent.com/jennybc/gapminder/main/inst/extdata/gapminder.tsv"
data = pd.read_csv(url, sep='\t')
column = "lifeExp"
plt.hist(data[column], bins=80, density=True, alpha=0.7, color='blue')

# calculate KDE
mu, std = norm.fit(data[column])
x = np.linspace(data[column].min(), data[column].max(), 100)
pdf = norm.pdf(x, mu, std)
plt.plot(x, pdf, 'k', linewidth=2)

plt.title("Histogram with Overlaid Normal Distribution")
plt.xlabel(column)
plt.ylabel("Density")
plt.show()

