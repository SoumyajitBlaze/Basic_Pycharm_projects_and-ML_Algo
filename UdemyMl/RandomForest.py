# Regression Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('D:/Udemy ML/ML_Complete/Part 2 - Regression/Section 6 - Polynomial Regression/Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""


# Feature Scaling
'''
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import FunctionTransformer
sc_X = StandardScaler()
sc_y = StandardScaler()
x=sc_X.fit_transform(x)
y = np.squeeze(sc_y.fit_transform(y.reshape(-1, 1)))
'''
# Fitting the Regression Model to the dataset
# Create your regressor here
from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=300,random_state=0)
regressor.fit(x,y)

regressor.fit(x,y)
# Predicting a new result

y_pred=regressor.predict([[6.5]])
print(y_pred)
# Visualising the Regression results
x_grid = np.arange(min(x), max(x), 0.01)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regressor.predict(x_grid), color = 'blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()