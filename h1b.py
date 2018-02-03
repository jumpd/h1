#Predict whether a person will be certified or denied
import pandas as pd
import matplotlib.pyplot as plt
import h1bfunctions 
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

#dataset path
data_set_path = 'h1b_kaggle.csv'

#split data into training and test set
chunks = 100 #number of data rows want to use
data_set = h1bfunctions.get_data(data_set_path, chunk = chunks)

#clean the data
new_data = h1bfunctions.format_clean(data_set)

xs = new_data.drop('CASE_STATUS', axis = 1)  
ys = new_data['CASE_STATUS']
X_train, X_test, y_train, y_test = train_test_split(xs,ys, test_size=0.30)

#summary statistics
print(xs.describe())
print(ys.describe())

#Visuallizations
#h1functions.visualize(xs)

#Transform and Scale Data
scaler = preprocessing.StandardScaler()
scaler.fit_transform(X_train)

#lasso regression
#Logistic Regression
#Deep Neural Net 
