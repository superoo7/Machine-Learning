# Use preprocessed template

# Data Preprocessing Template

# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, 0].values		# Independant variable
Y = dataset.iloc[:, -1].values		# Dependant variable

# Machine learning prep with spliting dataset for Training set and Test set
from sklearn.cross_validation import train_test_split
# normally test_size is .2-.3 (train_size+test_size = 1)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 1/3, random_state = 0)

# Feature Scaling
'''
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train.reshape(-1,1),Y_train.reshape(-1,1)) # formatting issue, reshape resolved

# Predicting the Test set results
y_pred = regressor.predict(X_test.reshape(-1,1))

# 





















