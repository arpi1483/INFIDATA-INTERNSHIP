import matplotlib.pyplot as plt #basic visualization
import seaborn as sns #adavance visualization

#loading dataset
df=sns.load_dataset("iris")#loading dataset
print(df)

#draw lineplot
sns.lineplot(x="sepal_length",y="sepal_width",data=df)
#setting the title using matplotlib
plt.title("Lineplot on IRIS dataset")
plt.show()