# exercise_B.8

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris = pd.read_csv("iris.csv")
fig=sns.jointplot(x='SepalLengthCm', y='SepalWidthCm', kind="hex", color="red", data=iris)
plt.show()