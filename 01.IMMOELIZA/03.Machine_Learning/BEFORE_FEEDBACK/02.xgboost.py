import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor

from sklearn.preprocessing import StandardScaler


"""
Loads and preprocesses the dataset, trains an XGBoost regression model,
evaluates its performance, and prints the test score, mean absolute error, 
and relative error.

The function performs the following steps:
1. Loads the dataset from 'cleaned_dataset.csv'.
2. Drops unnecessary columns.
3. Applies one-hot encoding to categorical features.
4. Maps ordinal features to numerical values.
5. Splits the data into training and testing sets.
6. Scales the feature data.
7. Trains an XGBoost regression model.
8. Evaluates the model on the test set.
9. Prints the test score, mean absolute error, and relative error.

Parameters:
None

Returns:
None
"""
# Load dataset


import pickle

absolute_path = r"04.API/ImmoEliza/after_outlier_df.pkl"

with open(absolute_path, "rb") as f:
    df = pickle.load(f)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Apply one-hot encoding to 'subtypeofproperty' and 'region' columns

one_hot_sub = pd.get_dummies(df['subtypeofproperty']).astype('int64')
one_hot_df = pd.get_dummies(df['region']).astype('int64')
df = pd.concat([df, one_hot_sub, one_hot_df], axis=1)
df.drop(['subtypeofproperty', 'region'], axis=1, inplace=True)

# Map ordinal features to numerical values
order_mapping = {'West Flanders': 1, 'Walloon Brabant': 2, 'Luxembourg': 3, 'Liège': 4, 'Limburg': 5, 'Hainaut': 6, 'Flemish Brabant': 7, 'East Flanders': 8, 'Namur': 9, 'Brussels': 10, 'Antwerp': 11}
rating_dict = {'G': 1, 'F_E': 2, 'F_D': 3, 'F': 4, 'F_C': 5, 'E_D': 6, 'E': 7, 'D': 8, 'C': 9, 'B_A': 10, 'B': 11, 'G_C': 12, 'E_C': 13, 'A_A+': 14, 'A': 15, 'A+': 16, 'A++': 17}
df['province'] = df['province'].map(order_mapping)
df['peb'] = df['peb'].map(rating_dict)

# Split the data into features and target variable
X = df.drop('price', axis=1)
y = df['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the feature data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the XGBoost regression model
model = XGBRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Make predictions and evaluate the model
y_pred = model.predict(X_test_scaled)
test_score = model.score(X_test_scaled, y_test)
mae = mean_absolute_error(y_test, y_pred)

# Print evaluation metrics
print('Test Score:', test_score)
print('Mean Absolute Error:', mae)

# Calculate and print relative error
mean_price = y_test.mean()
relative_error = mae / mean_price
print('Relative Error:', relative_error)


