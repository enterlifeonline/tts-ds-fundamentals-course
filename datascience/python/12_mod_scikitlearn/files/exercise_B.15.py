# exercise_B.15

# Import necessary modules 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
iris = pd.read_csv("iris.csv")
#Drop id column
iris = iris.drop('Id',axis=1)
sns.kdeplot(data=sub[['PetalLengthCm','PetalWidthCm']],cmap="plasma", shade=True, shade_lowest=False)
plt.title('Iris-setosa')
plt.xlabel('Petal Length Cm')
plt.ylabel('Petal Width Cm')
plt.show()