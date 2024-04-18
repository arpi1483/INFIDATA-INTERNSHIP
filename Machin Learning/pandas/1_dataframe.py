#creating a dataframe/dataset

import pandas as pd
#how to dictionary to datframe

data=pd.DataFrame({
    "name":["ali","khan","mahesh","vinit"],
    "age":[20,25,30,25],
    "branch":["cse","me","ise","ece"],
    "place":["banglore","delhi","mysore","porbandar"]
})
print(data)

#saving the dataframe created as csv file
data.to_csv('id.csv',index=False)