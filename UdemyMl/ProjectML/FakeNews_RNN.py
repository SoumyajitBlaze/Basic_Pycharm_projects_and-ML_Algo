import pandas as pd
df=pd.read_csv('D:/Udemy ML/ML_Complete/Dataset_Fake_news/train.csv')

print(df.shape)
null_columns=df.columns[df.isnull().any()]

df=df.dropna()
print(df.isnull().sum())
X=df.drop('label',axis=1)
y=df['label']
messages=X.copy()

messages.reset_index(inplace=True)
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer,HashingVectorizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
corpus=[]
import re
for i in range (len(messages)):
    review=re.sub('[^a-zA-Z]',' ',messages['title'][i])
    review=review.lower()
    review=review.split()
    review=[ps.stem(word) for word in review if not word in stopwords.words('english')]
    review=' '.join(review)
    corpus.append(review)

import tensorflow as tf
from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Bidirectional
from tensorflow.keras.layers import Dropout

voc_size=5000
onehot_repr=[one_hot(words,voc_size) for words in corpus]
sent_length=20
embedded_docs=pad_sequences(onehot_repr,padding='pre',maxlen=sent_length)


embedding_vector_features=40
model=Sequential()
model.add(Embedding(voc_size,embedding_vector_features,input_length=sent_length))
model.add(LSTM(100))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

import numpy as np
X_final=np.array(embedded_docs)
y_final=np.array(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X_final,y_final,test_size=0.33,random_state=0)

model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=10,batch_size=64)

y_pred=model.predict_classes(X_test)

from sklearn import metrics
from sklearn.metrics import confusion_matrix
import numpy as np
import itertools
score=metrics.accuracy_score(y_test,y_pred)
print("Accuracy:  %0.3f" %score)
cm=metrics.confusion_matrix(y_test,y_pred)
