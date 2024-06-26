import numpy as np #for array operatiin
import pandas as pd #for creating and handling dataset

example2_data=pd.DataFrame({'x':[0,1,2,3,4],
                            'y':[1.5,2,3.5,5,4.5]})

print(example2_data) #displaying exmaple1 dataframe

x=example2_data['x'].values.reshape(-1,1) #choosing input values
y=example2_data['y'].values.reshape(-1,1) #choosing output values

from sklearn.linear_model import LinearRegression #importing algo
linear_regressor=LinearRegression() #initalising algorithm
linear_regressor.fit(x,y)  #traing the algo on our data
print('[info] linear regression model training complete...')

m=linear_regressor.coef_[0][0]
c=linear_regressor.intercept_[0]

print(f"m values is :{m}")
print(f"c values is :{c}")
print(f"eqation of line is :y={m}x+{c}")

new_user_input=float(input("enter the value of x:"))
new_user_input=[[new_user_input]]
new_output=linear_regressor.predict(new_user_input)[0]
print(f"when x={new_user_input},y={new_output}")

