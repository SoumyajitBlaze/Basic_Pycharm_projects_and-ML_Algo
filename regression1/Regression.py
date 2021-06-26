import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0,10.0)

#reading data
data=pd.read_csv('C:/Users/kiit1/Documents/headbrain.csv')

#collecting X and Y

X=data['Head Size(cm^3)'].values
Y=data['Brain weight(grams)'].values

#Finding Mean value

mean_X=np.mean(X)
mean_Y=np.mean(Y)

#total no of values

k=len(X)

#calculate m and c

numerator=0
denomirator=0

for i in range(k):
    numerator=numerator+(X-mean_X)*(Y-mean_Y)
    denomirator=denomirator+(X-mean_X)**2

m=numerator/denomirator
c=mean_Y-(m*mean_X)

print(m,c)

