import numpy as np
import pandas as pd
import matplotlib.pyplot as  plt

plt.rcParams['figure.figsize'] = (20.0,10.0)

#reading data
data=pd.read_csv('C:/Users/kiit1/Documents/headbrain.csv')
print(data.shape)
print(data.head())
#collecting X and Y

X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values


#Finding Mean value

mean_X=np.mean(X)
mean_Y=np.mean(Y)

#total no of values

k=len(X)

#calculate m and c

numerator=0
denomirator=0

for i in range(k):
    numerator+=(X[i]-mean_X)*(Y[i]-mean_Y)
    denomirator=denomirator+(X[i]-mean_X)*(X[i]-mean_X)

m=numerator/denomirator
c=mean_Y-(m*mean_X)

print(m,c)

#Plot graph

max_x=np.max(X)+100
min_x=np.min(X)-100

#calculate line value of X and Y

x=np.linspace(min_x,max_x,1000)
y=c+m*x

#plotting line

plt.plot(x,y,color='#58b970',label='regression line')
plt.scatter(X,Y,c='#ef5423',label='scatter plot')

plt.xlabel('headsize')
plt.ylabel('brainweight')
plt.legend()
plt.show()

# Check using R^2 method

ss_t=0
ss_r=0

for i in  range (k):
    y_pred=m*X[i]+c
    ss_r+=(Y[i]-mean_Y)**2
    ss_t+=(y_pred-Y[i])**2
r2=1-(ss_t/ss_r)
print(r2)