import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
titanic_data=pd.read_csv('C:/Users/kiit1/Documents/titanic.csv')
print(titanic_data.head(10))
print("no of passanger"+str(len(titanic_data.index)))

#CLEANING
print(titanic_data.isnull())
print(titanic_data.isnull().sum())
print(titanic_data.drop("Cabin",axis=1,inplace=True))
print(titanic_data)
titanic_data.dropna(inplace=True)
sns.heatmap(titanic_data.isnull(),yticklabels=False,cbar=False)
plt.show()

#CATEGORICAL BY DUMMIES

sex=pd.get_dummies(titanic_data['Sex'],drop_first=True)
print(sex.head(5))
embark=pd.get_dummies(titanic_data['Embarked'],drop_first=True)
print(embark.head(5))
pcl=pd.get_dummies(titanic_data['Pclass'],drop_first=True)
print(pcl.head(5))
titanic_data=pd.concat([titanic_data,sex,embark,pcl],axis=1)
print(titanic_data.head(8))
titanic_data.drop(['Sex','Embarked','PassengerId','Name','Ticket','Pclass'],axis=1,inplace=True)
print(titanic_data.head(10))