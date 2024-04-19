import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")

df['species']=df['species'].map({'setosa':1,
                                 'versicolor':2,
                                 'virginica':3})

correction=df.corr() #getting corraction matrix
#creating a plot of corraction matrix as heatmap
sns.heatmap(correction,cbar=True,
            annot=True,linewidths=0.5,
            cmap='Blues')
plt.show()
#positive corraction is represented as light
#negative corractfion is represented as dask