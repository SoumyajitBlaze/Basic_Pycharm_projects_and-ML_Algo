import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('D:/Udemy ML/ML_Complete/Part 2 - Regression/Section 6 - Polynomial Regression/Position_Salaries.csv')
print(dataset)


x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values

'''
from  sklearn.model_selection import  train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
print(x_train)
'''
#Feature Scaling..................................................................................
'''
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)

'''

from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(x,y)

#FITTING POLYNOMIAL REGRESSION................................................................
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=4)
x_poly=poly_reg.fit_transform(x)
#Fitting it to Multiple Regression
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)
y_pred=lin_reg2.predict(x_poly)
print(y_pred)

#VISUALISING Linear Regression Result.........................................................................
plt.scatter(x,y,color='red')
plt.plot(x,lin_reg.predict(x),color='blue')
plt.title('Truth or Bluff(Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#VISUALIZING Polynomial Regression Result.............................................

x_grid=np.arange(min(x),max(x),0.1)
x_grid=x_grid.reshape((len(x_grid),1))

plt.scatter(x,y,color='red')
plt.plot(x_grid,lin_reg2.predict(poly_reg.fit_transform(x_grid)),color='blue')
plt.title('Truth or Bluff(Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
#Predicting New Result with Linear Regression
print(lin_reg.predict([[6.5]]))
#Predicting New Result with Polynomial Refression
print(lin_reg2.predict(poly_reg.fit_transform([[6.5]])))