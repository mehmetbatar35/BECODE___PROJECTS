import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import pickle



def preprocess_data(file_path):

    df = pd.read_csv(file_path)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    df.drop(['monthlycharges', 'typeofsale', 'country', 'floodingzone', 'locality', 'district'], axis=1, inplace=True)

    df['subtypeofproperty'] = df['subtypeofproperty'].apply(lambda x: 'apartment' if x in 
        ['apartment', 'ground_floor', 'apartment_block', 'flat_studio', 'service_flat', 'kot'] 
        else ('house' if x in ['country_cottage','pavilion', 'mansion', 'manor_house', 'castle', 
        'chalet','triplex', 'farmhouse', 'town_house', 'house', 'villa', 'duplex', 'penthouse'] 
        else 'other'))
    one_hot_sub = pd.get_dummies(df['subtypeofproperty']).astype('int64')
    one_hot_df = pd.get_dummies(df['region']).astype('int64')
    df = pd.concat([df, one_hot_sub, one_hot_df], axis=1)
    df.drop(['subtypeofproperty', 'region'], axis=1, inplace=True)


    region_dict = {'Hainaut': 1, 'Namur': 2, 'Liège': 3, 'Luxembourg': 4, 'Limburg': 5, 
                'East Flanders': 6, 'West Flanders': 7, 'Antwerp': 8, 'Brussels': 9, 
                'Walloon Brabant': 10, 'Flemish Brabant': 11}
    df['province'] = df['province'].map(region_dict)

    rating_dict = {'A++': 1, 'A+': 2, 'A': 3, 'A_A+': 4, 'E_C': 5, 'G_C': 6, 'B': 7, 'B_A': 8, 
                'C': 9, 'D': 10, 'E': 11, 'F_C': 12, 'F': 13, 'F_D': 14, 'E_D': 15, 
                'F_E': 16, 'G': 17}
    df['peb'] = df['peb'].map(rating_dict)

    X = df.drop('price', axis=1)
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    with open('scaler.pkl', 'wb') as scaler_file:
        pickle.dump(scaler, scaler_file)

    X_train_scaled_df = pd.DataFrame(X_train_scaled, columns=X.columns)
    X_test_scaled_df = pd.DataFrame(X_test_scaled, columns=X.columns)    

    return X_train_scaled_df, X_test_scaled_df, y_train, y_test



def train_and_save_model(X_train, y_train, model, model_name):
    model.fit(X_train, y_train) 
    model_filename = f"{model_name}.pkl"
    with open(model_filename, 'wb') as model_file:
        pickle.dump(model, model_file)

    print(f"{model_name} model saved as {model_filename}")

def load_and_evaluation_model(model_name, X_test, y_test):
    with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    model_filename = f"{model_name}.pkl"
    with open(model_filename, 'rb') as model_file:
        model = pickle.load(model_file)
    X_test_scaled = scaler.transform(X_test)
    y_pred = model.predict(X_test_scaled)
    test_score = model.score(X_test_scaled, y_test)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"{model_name} Model Evaluation: ")
    print(f"Test Score: {test_score}")
    print(f"Mean Absolute Error: {mae}")

    mean_price = y_test.mean()
    relative_error = mae / mean_price
    print(f"Relative Error: {relative_error}")    

# EXAMPLE USAGE

X_train, X_test, y_train, y_test = preprocess_data('01.IMMOELIZA/03.Machine_Learning/cleaned_dataset.csv')  

xgb_model = XGBRegressor(n_estimators=100, random_state=42)
train_and_save_model(X_train, y_train, xgb_model, 'xgboost')

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
train_and_save_model(X_train, y_train, rf_model, 'random_forest')

lr_model = LinearRegression()
train_and_save_model(X_train, y_train, lr_model, 'linear_regression')



load_and_evaluation_model('xgboost', X_test, y_test)
load_and_evaluation_model('random_forest', X_test, y_test)
load_and_evaluation_model('linear_regression', X_test, y_test)    