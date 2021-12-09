# exercise_C.5

# Import necessary modules 
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split  
iris = pd.read_csv("iris.csv")
#Drop id column
iris = iris.drop('Id',axis=1)
X = iris.iloc[:, :-1].values
y = iris.iloc[:, 4].values
#Split arrays or matrices into train and test subsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20) 
knn = KNeighborsClassifier(n_neighbors=7)  
knn.fit(X_train, y_train)   
# Calculate the accuracy of the model 
print("Accuracy of the model:")
print(knn.score(X_test, y_test))