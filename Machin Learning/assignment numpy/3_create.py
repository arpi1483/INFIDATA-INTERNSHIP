import pandas as pd
#how to dictionary to datframe

data=pd.DataFrame({
    "name":["Alice","Bob","Charlie"],
    "age":[25,30,35],
    "city":['New York','Los Angeles','Chicago']
})

print(data)

data.to_csv('person_info.csv',index=False)

print(data.shape)

print("statistical info :\n",data.describe())

print("basic info:\n",data.info())

print(data.size)