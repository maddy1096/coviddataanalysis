##Checking no of people who have recovered##

#decision tree regression 
import pandas as pd
import numpy as np

#Selecting the required data
data = pd.read_csv('time_series_covid_19_recovered_1.csv')

df = data.groupby(['Country/Region']).sum().reset_index().sort_values('sum',ascending = False).reset_index(drop = True)

#Splitting the data for x and y
X = df.iloc[:,1:-2]

Y = df.iloc[:,-2]


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

#decision regression to predict values of next day based on previous count 
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, Y_train)

# Predicting a new result
y_pred = regressor.predict(X_test)

#RMSE calculation 
from sklearn.metrics import mean_squared_error 

mse = mean_squared_error(Y_test,y_pred) 

