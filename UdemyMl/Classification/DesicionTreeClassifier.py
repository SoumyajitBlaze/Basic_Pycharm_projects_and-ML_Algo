import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_csv('D:/Udemy ML/ML_Complete/Dataset 3/kyphosis.csv')
'''
k=sns.pairplot(dataset,hue='Kyphosis')
plt.show(k)
'''

x=dataset.iloc[:,1:4]
y=dataset.iloc[:,0:1]
from sklearn.model_selection import train_test_split

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30, random_state = 0)
from  sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier(criterion='entropy')

dtree.fit(x_train, y_train)

y_pred=dtree.predict(x_test)

from  sklearn.metrics import confusion_matrix
conf_matrix=confusion_matrix(y_test,y_pred)
print(conf_matrix)

#TREE VISUALIZATION

from IPython.display import Image
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
import pydot

features = list(dataset.columns[1:])
features

dot_data = StringIO()
export_graphviz(dtree, out_file=dot_data,feature_names=features,filled=True,rounded=True)

graph = pydot.graph_from_dot_data(dot_data.getvalue())

Image(graph[0].create_png())



# Create PNG
graph[0].write_png("DTC.png")


