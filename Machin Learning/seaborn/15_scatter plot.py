import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")

sns.scatterplot(x='sepal_length',y='petal_length',data=df,
                hue='species',size='species')

plt.show()