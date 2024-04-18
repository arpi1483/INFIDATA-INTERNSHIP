#assuming a dataframe/datset is alredy present
#this is how we read/load it

import pandas as pd
#for creating and handling datframe
#loading id.csv into pandas datframe

data=pd.read_csv("diabetes.csv")
print(data)
#displaying the dataframe

print("display speciific columns")
print(data['Glucose'])  #displaying single column
print(data[["Glucose","BMI"]])  #displaying multiple column

print(data.shape)  #displaying shape of dataset
print(data.size)  #displaying size of data

#Indexing
print(data.head())  #print first 5 rows of data
print(data.tail())  #print last 5 row of data

print(data.head(3))  
print(data.tail(10))
