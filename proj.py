__author__ = 'vikram'
# Import libraries necessary for this project
import numpy as np
import pandas as pd
from time import time
# from IPython.display import display # Allows the use of display() for DataFrames

# Import supplementary visualization code visuals.py
# import visuals as vs

# Load the Census dataset
data = pd.read_csv("census.csv")

# Success - Display the first record
print data.head(n=10)
print len(data)
n_greater_50k = 0
for _, oneSample in data.iterrows():
    if (oneSample['income'] == '>50K'):
        n_greater_50k+=1
print n_greater_50k

# data.loc[data['income'] == '<=50K', 'income'] = 0
# print data.head(n=10)

income_raw = data['income']
for x in range(0, len(income_raw)):
    if income_raw[x] == "<=50K":
        income_raw[x] = 0
    else:
        income_raw[x] = 1
print(income_raw)