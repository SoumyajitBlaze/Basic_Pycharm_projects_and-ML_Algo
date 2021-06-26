import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('D:/Udemy ML/ML_Complete/Part 1 - Data Preprocessing/Data_Preprocessing/data.csv')
print(dataset)

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values

#taking care of missing data.................................................................

from  sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean' ,axis=0,)
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])
print(x)

#Encoding....................................................................................

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_x=LabelEncoder()
x[:,0]=labelencoder_x.fit_transform(x[:,0])

#one hot encoding for dummy variables...........................................................

onehotencoder=OneHotEncoder(categorical_features=[0])
x=onehotencoder.fit_transform(x).toarray()

print(x)

labelencoder_y=LabelEncoder()
y=labelencoder_x.fit_transform(y)
print(y)

from  sklearn.model_selection import  train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
print(x_train)

#Feature Scaling..................................................................................
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)

print(x_train)



