import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
df = pd.read_csv('exam_marks.csv')

# Display the first few rows of the dataset
print(df.head())

# Visualize the relationship between study hours and exam scores
plt.figure(figsize=(10, 6))
sns.lineplot(x='hours', y='marks', data=df)
plt.title('Study Hours vs Exam Scores')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.show()

example1_data=pd.DataFrame({'x':[['hours']],
                            'y':[['marks']]})
x=example1_data['x'].values.reshape(-1,1) #choosing input values
y=example1_data['y'].values.reshape(-1,1)

from sklearn.linear_model import LinearRegression #importing algo
linear_regressor=LinearRegression() #initalising algorithm
linear_regressor.fit(x,y)