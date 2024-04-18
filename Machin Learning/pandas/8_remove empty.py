import pandas as pd

df=pd.read_csv('data.csv')  #loading the dataset
print('[info] data loaded successfully...')

print('[info] checking for nan values...')
print(df.columns[df.isna().any()])

print('[info] removing nan values...')
df=df.dropna()  #this line removes entire row which has nan value

print('[info] checking nan values again...')
print(df.columns[df.isna().any()])