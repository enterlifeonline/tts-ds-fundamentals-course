# exercise_B.11

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris = pd.read_csv("iris.csv")
sns.jointplot("SepalLengthCm", "SepalWidthCm", data=iris, color="b").plot_joint(sns.kdeplot, zorder=0, n_levels=6) 
plt.show()