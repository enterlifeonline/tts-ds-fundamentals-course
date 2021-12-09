# exercise_B.9

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
iris = pd.read_csv("iris.csv")
fig=sns.jointplot(x='SepalLengthCm', y='SepalWidthCm', kind="kde", color='cyan', data=iris)  
plt.show()