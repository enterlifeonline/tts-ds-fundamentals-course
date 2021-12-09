# exercise_B.17

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
iris = pd.read_csv("iris.csv")
#Drop id column
iris = iris.drop('Id',axis=1)
X = iris.iloc[:, 0:4]
f, ax = plt.subplots(figsize=(10, 8))
corr = X.corr()
print(corr)
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), 
          cmap=sns.diverging_palette(220, 10, as_cmap=True),square=True, ax=ax, linewidths=.5)
plt.show() 
