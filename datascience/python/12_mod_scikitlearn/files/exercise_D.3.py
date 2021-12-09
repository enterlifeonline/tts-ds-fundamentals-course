# exercise_D.3

import pandas as pd
from sklearn.model_selection import train_test_split  
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

iris = pd.read_csv("iris.csv")
#Drop id column
iris = iris.drop('Id',axis=1)
X = iris.iloc[:, :-1].values
y = iris.iloc[:, 4].values

#Split arrays or matrices into train and test subsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20) 

model = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial').fit(X, y)
model.fit(X_train,y_train)
prediction=model.predict(X_test)
print('The accuracy of the Logistic Regression is', metrics.accuracy_score(prediction,y_test))