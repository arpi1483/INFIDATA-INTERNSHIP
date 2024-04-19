import matplotlib.pyplot as plt
import seaborn as sns

#violin plot
#loading dataset
df=sns.load_dataset("iris")
#creating a violin plot
sns.violinplot(x='species',y='sepal_width',data=df,palette='Blues')
#displying the violin
plt.show()