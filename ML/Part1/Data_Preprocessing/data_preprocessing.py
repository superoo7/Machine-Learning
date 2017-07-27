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
                
# show full array
np.set_printoptions(threshold=np.nan)
                
# Dealing with missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0) # use mean value to replace the NaN data
imputer.fit(X[:,1:3])
X[:, 1:3] = imputer.transform(X[:,1:3])

# Encode data (Country and Purchased)
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder() # Country
X[:,0] = labelencoder_X.fit_transform(X[:, 0]) # transform names into numbers
# Encounter problem that a country are higher value than another
# Use dummy variable (create France, Germany, Spain column)

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0]) # chosen 0 index
X = onehotencoder.fit_transform(X).toarray()
# France, Germany, Spain (alphabet order)

# Purchased (Yes, No)
labelencoder_Y = LabelEncoder() 
Y = labelencoder_Y.fit_transform(Y) # transform purchased into numbers

