import pandas as pd

# get iris data set
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

df.head()
df.describe()

df.groupby('species')['sepal_width'].mean()
print(df.groupby('species')['sepal_width'].nunique())
