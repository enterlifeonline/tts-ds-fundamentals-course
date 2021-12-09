# exercise_C.1

import pandas as pd
iris = pd.read_csv("iris.csv")
#Drop id column
iris = iris.drop('Id',axis=1)
X = iris.iloc[:, :-1].values
y = iris.iloc[:, 4].values
print("Attributes:")
print(X)
print("\nLabels:")
print(y)
