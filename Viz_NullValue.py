%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('data.csv')
df.head()

plt.figure(figsize=(15,8))

sns.heatmap(df.isnull(),yticklabels=False,
            cbar=False, cmap='viridis') #creating heatmap with nullvalues 
