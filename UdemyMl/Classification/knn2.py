import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Importing the dataset
dataset = pd.read_csv('D:/Udemy ML/ML_Complete/Part 3 - Classification/Dataset2/Classified Data.csv')
print(dataset.shape)
count=pd.value_counts(dataset['TARGET CLASS'])
print(count)



x=dataset.iloc[:,0:11]
y=dataset.iloc[:,11]

'''
k=sns.pairplot(dataset)
plt.show(k)
'''
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.transform(x_test)
print(x_train)

# Fitting the knn Regression Model to the dataset
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=23,metric='minkowski',p=2)
classifier.fit(x_train,y_train)



y_pred=classifier.predict(x_test)
print(y_pred)

#Making confution matrix
from sklearn.metrics import confusion_matrix,classification_report
cm=confusion_matrix(y_test,y_pred)
print(cm)
print(classification_report(y_test,y_pred))

#choosing k value

error_rate=[]
for i in range(1,40):
    classifier=KNeighborsClassifier(n_neighbors=i)
    classifier.fit(x_train,y_train)
    y_pred=classifier.predict(x_test)
    error_rate.append(np.mean(y_pred!=y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue',linestyle='dashed',marker='o',markerfacecolor='red',markersize=10)
plt.title('Error Rate vs K value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()
