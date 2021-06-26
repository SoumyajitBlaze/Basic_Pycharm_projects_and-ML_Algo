from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas  as pd
import matplotlib.pyplot as plt
from sklearn import metrics

dataset=pd.read_csv('C:/Users/kiit1/Documents/headbrain.csv')
print(dataset)


X = dataset[['Head Size(cm^3)']]
Y = dataset['Brain Weight(grams)']


print(X)
X_Train,X_Test,Y_Train,Y_Test=train_test_split(X,Y,test_size=1/3,random_state=0)

regressor=LinearRegression()
regressor.fit(X_Train,Y_Train)

#Predict
Y_Pred=regressor.predict(X_Test)

#plot graph

plt.scatter(X_Train,Y_Train,color='red')
plt.plot(X_Train,regressor.predict(X_Train))
plt.xlabel('headsize')
plt.ylabel('brainweight')
plt.legend()
plt.show()

print(metrics.mean_absolute_error(Y_Test,Y_Pred))