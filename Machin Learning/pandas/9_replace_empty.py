import pandas as pd

df = pd.read_csv('data.csv') # loading data into dataframe

print(df.columns[df.isna().any()]) # checking nan before replacing

calorie_mean = df['Calories'].mean()  # getting calories colunm mean value
print(calorie_mean)

# replacing nan value with mean value
df["Calories"].fillna(calorie_mean,inplace=True)
print(df.columns[df.isna().any()])  # checking nan after replacing
