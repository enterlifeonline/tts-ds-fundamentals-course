# exercise_B.18

import pandas as pd
import seaborn as sns 
iris = pd.read_csv("iris.csv")
#Drop id column
iris = iris.drop('Id',axis=1)
box_data = iris #variable representing the data array
box_target = iris.Species #variable representing the labels array
sns.boxplot(data = box_data,width=0.5,fliersize=5)
sns.set(rc={'figure.figsize':(2,15)})

