# -*- coding: utf-8 -*-
"""logistic-regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/Navan0/tot/blob/master/logistic_regression.ipynb
"""

!curl http://www.codeheroku.com/static/workshop/datasets/student_scores.csv -o student_scores.csv

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("house_price.csv")
df

x = df["Id"]
y = df["SalePrice"]
df.plot.scatter(x="Id",y="SalePrice",c="SalePrice",colormap='bwr')
plt.show()

def sigmoid(z):

    return 1 / (1+ np.exp(-z))

def logistic_regression(all_x,all_y,m,b):
    for x,y_actual in zip(all_x,all_y):
        y_pred = sigmoid(m*x+b)
        error = y_pred - y_actual

        delta_m = -1 * (error * x) * 0.05
        delta_b = -1 * (error) * 0.05

        m = m + delta_m
        b = b + delta_b

    return m,b

m = 0
b = 0
for i in range(0,100):
    m,b = logistic_regression(x,y,m,b)
m,b

### Helper function use when needed
def get_sigmoid(X,m,b):
    sig = []
    for x in X.values:
        y = sigmoid(m*x + b)
        sig.append(y)

    return sig

plt.plot(x,y,'o')
plt.xlabel("Id")
plt.ylabel("SalePrice")

sig = get_sigmoid(x,m,b)
plt.plot(x,sig,'ro')
plt.show()

def predict(x,m,b):
    y = sigmoid(m*x + b)

    if y > 0.5:
        return 1
    else:
        return 0

df["Predictions"] = df.apply(lambda row: predict(row["Id"],m,b),axis=1)
df
