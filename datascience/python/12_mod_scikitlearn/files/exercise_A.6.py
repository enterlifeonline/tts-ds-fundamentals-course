# exercise_A.6

import pandas as pd
data = pd.read_csv("iris.csv")
print("Observations of each species:")
print(data['Species'].value_counts()) 