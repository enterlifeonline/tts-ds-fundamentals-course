# exercise_A.8

import pandas as pd
data = pd.read_csv("iris.csv")
print("Original Data:")
print(data.head())
new_data = data.drop('Id',axis=1)
print("After removing id column:")
print(new_data.head())
x = data.iloc[:, [1, 2, 3, 4]].values
print(x) 