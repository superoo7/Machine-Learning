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
