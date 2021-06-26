import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('D:/Udemy ML/ML_Complete/Part 1 - Data Preprocessing/Data_Preprocessing/data.csv')


x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values

from  sklearn.model_selection import  train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
print(x_train)

#Feature Scaling..................................................................................
'''
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)

'''