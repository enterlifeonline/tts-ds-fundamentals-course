# exercise_B.2

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris = pd.read_csv("iris.csv")
ax=plt.subplots(1,1,figsize=(10,8))
sns.countplot('Species',data=iris)
plt.title("Iris Species Count")
plt.show()