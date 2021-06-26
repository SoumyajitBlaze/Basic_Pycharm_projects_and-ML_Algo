import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('D:/Udemy ML/ML_Complete/Part 2 - Regression/Section 5 - Multiple Linear Regression/50_Startups.csv')
print(dataset)


x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,4].values
y=y.astype('int')

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_x=LabelEncoder()
x[:,3]=labelencoder_x.fit_transform(x[:,3])

#one hot encoding for dummy variables...........................................................

onehotencoder=OneHotEncoder(categorical_features=[3])
x=onehotencoder.fit_transform(x).toarray()
x=x[:,1:]
print(x)

from  sklearn.model_selection import  train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
y_pred=regressor.predict(x_test)
print(y_test)
print(y_pred)



#Feature Scaling..................................................................................
'''
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)

'''

import  statsmodels.api as sm
x=np.append(arr=np.ones((50,1)).astype(int),values=x,axis=1)
x_opt=x[:,[0,1,2,3,4,5]]
regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
print(regressor_OLS.summary())

x_opt=x[:,[0,1,3,4,5]]
regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
print(regressor_OLS.summary())

x_opt=x[:,[0,3,4,5]]
regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
print(regressor_OLS.summary())

x_opt=x[:,[0,3,5]]
regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
print(regressor_OLS.summary())

