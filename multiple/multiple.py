import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import  train_test_split
import math
from sklearn import linear_model
import seaborn as sns
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder

dataset=pd.read_csv('C:/Users/kiit1/Desktop/Downloads/zip/housing.csv')




dataset.hist()

#correlation plot

names=['longitude','latitude','housing_median_age','total_rooms','total_bedrooms',  'population','households','median_income'
       ,'median_house_value','ocean_proximity']
correlations=dataset.corr()
fig=plt.figure()
ax=fig.add_subplot(111)
cax=ax.matshow(correlations,vmin=-1,vmax=1)
fig.colorbar(cax)
ticks=np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.show()

le=LabelEncoder()
dataset.ocean_proximity=pd.to_numeric(dataset.ocean_proximity)

X=dataset[['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_house_value','ocean_proximity']]
Y=dataset['median_income']



X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=1/3,random_state=0)

reg=linear_model.LinearRegression()


reg.fit(X_train, Y_train)

Y_Pred=reg.predict(X_test)


