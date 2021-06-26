import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('D:/Udemy ML/ML_Complete/Part 2 - Regression/Section 4 - Simple Linear Regression/Salary_Data.csv')
print(dataset)

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values

from  sklearn.model_selection import  train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)
print(x_train)

#Feature Scaling..................................................................................
'''
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)

'''

print(str(len(dataset.Salary)))
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
y_pred=regressor.predict(x_test)
print(y_test)
print(y_pred)

#Scatter Plot

plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title('Exp vs sal')
plt.xlabel('Exp')
plt.ylabel('Sal')
plt.show()
plt.scatter(x_test,y_test,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title('Exp vs sal')
plt.xlabel('Exp')
plt.ylabel('Sal')
plt.show()
