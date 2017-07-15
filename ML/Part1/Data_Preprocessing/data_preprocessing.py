# Data Preprocessing 

# Library needed
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')

# Create Matrix
# iloc[row,col] : -> all
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,3].values
                
np.set_printoptions(threshold=numpy.nan)
                
# Dealing with missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer.fit(X[:,1:3])
X[:, 1:3] = imputer.transform(X[:,1:3])

