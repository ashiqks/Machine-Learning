# -*- coding: utf-8 -*-
"""RandomForestRegressor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cfpJ03fk-1TKJlzIA0FiJvjoMA3J2iwQ
"""

from google.colab import drive
drive.mount('/content/drive/')

import os
os.chdir('/content/drive/My Drive/colab')

#import necessary modules
import numpy as np
from sklearn.model_selection import train_test_split #import the function to partition the dataset to train and test sets
from sklearn.ensemble import RandomForestRegressor # import the random forest regresssion model 
from sklearn.model_selection import GridSearchCV #import the GridSearchCV class for hypertuning the model
import pandas as pd

csv = pd.read_csv('kc_house_data.csv') # read the dataset using pandas package 
csv = csv.dropna(axis=0) # drop all the rows of the dataset where atleast  one value in a row contains 'NaN' value
y = csv.price.values # price column is the target and convert it into numpy ndarrays
x_list = ['bedrooms', 'sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement', 'bathrooms', 'floors', 'waterfront', 'grade', 'condition', 'yr_built', ] #Taking only necessary columns for regression
x = csv[x_list].values # Extracting the required columns and converting it into numpy ndarrays

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0) # splitting the dataset using the train_test_split where the test data contains 20% of the original dataset

regressor = RandomForestRegressor() # creating an object of the RandomForestRegressor with default settings
regressor.fit(x_train, y_train) # training the model using the train dataset

R2_value= regressor.score(x_test, y_test) # returns the R^2 value of the prediction
print(acc)

params = {'n_estimators': np.arange(10, 500, 10)} # setting up the parameters for hypertuning, here the 'n_estimator' parameter is being tuned for a value between 10 & 500 with a multiple of 10
hypertuning = GridSearchCV(regressor, params) # Instantiating the GridSearchCV class with the two necessary parameters, the estimator model being tuned and the params search space
hypertuning.fit(x_train, y_train) # fitting the GridSearchCV object to the training dataset to get an optimal value for the 'n_estimator' parameter
print(hypertuning.score(x_test, y_test)) # returns the R^2 value of the prediction of the hyperparameter result
print(hypertuning.best_params_) # prints the best fit hyperparameter for the model within the search space we specified