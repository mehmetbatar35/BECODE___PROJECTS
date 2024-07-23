import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor

from sklearn.preprocessing import StandardScaler

def model_func():
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
    df = pd.read_csv('01.IMMOELIZA/03.Machine_Learning/cleaned_dataset.csv')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # Drop unnecessary columns
    df.drop(['monthlycharges', 'typeofsale', 'country', 'floodingzone', 'locality', 'district'], axis=1, inplace=True)

    # Apply one-hot encoding to 'subtypeofproperty' and 'region' columns
    df['subtypeofproperty'] = df['subtypeofproperty'].apply(lambda x: 'apartment' if x in 
        ['apartment', 'ground_floor', 'apartment_block', 'flat_studio', 'service_flat', 'kot'] 
        else ('house' if x in ['country_cottage','pavilion', 'mansion', 'manor_house', 'castle', 
        'chalet','triplex', 'farmhouse', 'town_house', 'house', 'villa', 'duplex', 'penthouse'] 
        else 'other'))
    one_hot_sub = pd.get_dummies(df['subtypeofproperty']).astype('int64')
    one_hot_df = pd.get_dummies(df['region']).astype('int64')
    df = pd.concat([df, one_hot_sub, one_hot_df], axis=1)
    df.drop(['subtypeofproperty', 'region'], axis=1, inplace=True)

    # Map ordinal features to numerical values
    region_dict = {'Hainaut': 1, 'Namur': 2, 'Liège': 3, 'Luxembourg': 4, 'Limburg': 5, 
                'East Flanders': 6, 'West Flanders': 7, 'Antwerp': 8, 'Brussels': 9, 
                'Walloon Brabant': 10, 'Flemish Brabant': 11}
    df['province'] = df['province'].map(region_dict)

    rating_dict = {'A++': 1, 'A+': 2, 'A': 3, 'A_A+': 4, 'E_C': 5, 'G_C': 6, 'B': 7, 'B_A': 8, 
                'C': 9, 'D': 10, 'E': 11, 'F_C': 12, 'F': 13, 'F_D': 14, 'E_D': 15, 
                'F_E': 16, 'G': 17}
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

# Run the model function
model_func()
