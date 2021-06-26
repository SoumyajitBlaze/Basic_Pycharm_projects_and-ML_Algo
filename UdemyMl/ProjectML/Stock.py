import pandas as pd

with open('D:/Udemy ML/Stock-Sentiment-Analysis-master/Data.csv') as f:
    print(f)

df = pd.read_csv('D:/Udemy ML/Stock-Sentiment-Analysis-master/Data.csv', encoding='cp1252')
print(df)

train = df[df['Date'] < '20150101']
test = df[df['Date'] > '20141231']

print(train)
print(test)
import re

data = train.iloc[:, 2:27]

data.replace("[^a-zA-Z]", " ", regex=True, inplace=True)

# Renaming column name

list1 = [i for i in range(25)]
new_index = [str(i) for i in list1]
data.columns = new_index

# converting into lower cases

for index in new_index:
    data[index] = data[index].str.lower()

headlines = []
for row in range(0, len(data.index)):
    headlines.append(' '.join(str(x) for x in data.iloc[row, 0:25]))

print(headlines[0])  # makes paragraph....for all in 0 index same goes for headline[1...n]

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

countvector = CountVectorizer(ngram_range=(1, 3))
traindataset = countvector.fit_transform(headlines)

from sklearn.naive_bayes import MultinomialNB

classifier = MultinomialNB().fit(traindataset, train['Label'])

test_transform = []
for row in range(0, len(test.index)):
    test_transform.append(' '.join(str(x) for x in test.iloc[row, 2:27]))
    test_dataset = countvector.transform(test_transform)
    predictions = classifier.predict(test_dataset)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

score = accuracy_score(test['Label'], predictions)

print(score)