import pandas as pd
import pickle
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor



absolute_path = r"04.API/ImmoEliza/ready_for_modeling"

with open(absolute_path, 'rb') as f:
    df = pickle.load(f)

pd.set_option('display.max_columns', None)

X = df.drop(columns = ['price'])
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#Train Linear Regression Model
lr_model = LinearRegression()
lr_model.fit(X_train_scaled, y_train)

# Train GradientBoostingRegressor Model
gbr_model = GradientBoostingRegressor(n_estimators = 100, random_state = 42)
gbr_model.fit(X_train_scaled, y_train)

# Train XGBRegressor Model
xgb_model = XGBRegressor(n_estimators = 100, random_state = 42)
xgb_model.fit(X_train_scaled, y_train)


# EVALUATE MODELS
def evaluate_model(model, X_test_scaled, y_test):
    y_pred = model.predict(X_test_scaled)
    test_score = model.score(X_test_scaled, y_test)
    mae = mean_absolute_error(y_test, y_pred)
    return test_score, mae

# Evaluate Linear Model
lr_test_score, lr_mae = evaluate_model(lr_model, X_test_scaled, y_test)
print(f"Linear Regression - Test Score: {lr_test_score:.4f}")
print(f"Linear Regression - Mean Absolute Error: {lr_mae:.4f}")

# Evaluate GradientBoostingRegressor Model
gbr_test_score, gbr_mae = evaluate_model(gbr_model, X_test_scaled, y_test)
print(f"GradientBoostingRegressor - Test Score: {gbr_test_score:.4f}")
print(f"GradientBoostingRegressor - Mean Absolute Error: {gbr_mae:.4f}")

# Evaluate XGBRegressor Model
xgb_test_score, xgb_mae = evaluate_model(xgb_model, X_test_scaled, y_test)
print(f"XGBRegressor - Test Score: {xgb_test_score:.4f}")
print(f"XGBRegressor - Mean Absolute Error: {xgb_mae:.4f}")


#Save the Models and Scaler
model_paths = {
    'lr_model': r"04.API/ImmoEliza/lr_model.pkl",
    'gbr_model': r"04.API/ImmoEliza/gbr_model.pkl",
    'xgb_model': r"04.API/ImmoEliza/xgb_model.pkl",
    'scaler': r"04.API/ImmoEliza/scaler.pkl"
}

# SAVE Linear Regression MODEL
with open(model_paths['lr_model'], 'wb') as f:
    pickle.dump(lr_model, f)

# SAVE GradientBoostingRegressor MODEL
with open(model_paths['gbr_model'], 'wb') as f:
    pickle.dump(gbr_model, f)

# SAVE XGBRegressor MODEL
with open(model_paths['xgb_model'], 'wb') as f:
    pickle.dump(xgb_model,f)

# SAVE SCALER
with open(model_paths['scaler'], 'wb') as f:
    pickle.dump(scaler, f)

print(f"Models and scaler saved to {model_paths['xgb_model']}, {model_paths['lr_model']}, {model_paths['scaler']}")    







