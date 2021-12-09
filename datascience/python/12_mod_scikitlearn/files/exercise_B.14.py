# exercise_B.14

# Import necessary modules 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
iris = pd.read_csv("iris.csv")
#Drop id column
iris = iris.drop('Id',axis=1)
sub=iris[iris['Species']=='Iris-setosa']
sns.kdeplot(data=sub[['SepalLengthCm','SepalWidthCm']],cmap="plasma", shade=True, shade_lowest=False)
plt.title('Iris-setosa')
plt.xlabel('Sepal Length cm')
plt.ylabel('Sepal Width cm')
plt.show()