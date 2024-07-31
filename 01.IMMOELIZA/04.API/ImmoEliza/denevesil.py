
import pandas as pd
import pickle
import streamlit as st
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler

# LOAD MODELS based on USER SELECTION
model_paths = {
    'gbr_model': r"04.API/ImmoEliza/gbr_model.pkl",
    'xgb_model': r"04.API/ImmoEliza/xgb_model.pkl",
    'scaler': r"04.API/ImmoEliza/scaler.pkl"
}

with open(model_paths['gbr_model'], 'rb') as f:
    gbr_model = pickle.load(f)
with open(model_paths['xgb_model'], 'rb') as f:
    xgb_model = pickle.load(f)
with open(model_paths['scaler'], 'rb') as f:
    scaler = pickle.load(f)

absolute_path = r"04.API/ImmoEliza/ready_for_modeling"
with open(absolute_path, 'rb') as f:
    df = pickle.load(f)

X = df.drop(columns=['price'])
y = df['price']

st.title("Real Estate Price Prediction")

st.header("User Input Parameters")

def user_input_features():
    province = st.selectbox('Province', [
        'West Flanders', 'Walloon Brabant', 'Luxembourg', 'Liège',
        'Limburg', 'Hainaut', 'Flemish Brabant', 'East Flanders',
        'Namur', 'Brussels', 'Antwerp'
    ])
    constructionyear = st.number_input('Construction Year', min_value=1895, max_value=2024, value=2000)
    if constructionyear < 1895 or constructionyear > 2024:
        st.warning('Please choose a year between 1895 and 2033.')
    stateofbuilding = st.slider('State of Building', 0, 5, 0)
    livingarea = st.number_input('Living Area', 12, 446, 12)
    bathroom_count = st.slider('Bathroom Count', 0, 3, 0)
    bedroomcount = st.slider('Bedroom Count', 0, 8, 0)
    kitchen = st.slider('Kitchen', 0, 3, 0)
    swimmingpool = st.slider('Swimming Pool', 0, 1, 0)
    
    order_mapping = {'West Flanders': 1, 'Walloon Brabant': 2, 'Luxembourg': 3, 'Liège': 4, 'Limburg': 5, 'Hainaut': 6, 'Flemish Brabant': 7, 'East Flanders': 8, 'Namur': 9, 'Brussels': 10, 'Antwerp': 11}
    province_mapped = order_mapping[province]

    default_values = {col: 0 for col in X.columns}
    default_values.update({
        'province': province_mapped,
        'bathroomcount': bathroom_count,
        'bedroomcount': bedroomcount,
        'constructionyear': constructionyear,
        'kitchen': kitchen,
        'livingarea': livingarea,
        'stateofbuilding': stateofbuilding,
        'swimmingpool': swimmingpool,
    })

    features = pd.DataFrame(default_values, index=[0])
    return features

input_df = user_input_features()

model_choice = st.sidebar.selectbox("Which model do you want to use to predict the price?", ['gbr_model', 'xgb_model'])

def round_to_nearest(value, multiple):
    return round(value / multiple) * multiple

def evaluate_model(model, X, y):
    X_scaled = scaler.transform(X)
    y_pred = model.predict(X_scaled)
    test_score = model.score(X_scaled, y)
    mae = mean_absolute_error(y, y_pred)
    return test_score, mae

if model_choice == 'gbr_model':
    model = gbr_model
elif model_choice == 'xgb_model':
    model = xgb_model

if st.button("Calculate Price"):
    input_scaled = scaler.transform(input_df)
    predicted_price = model.predict(input_scaled)

    rounded_price = round_to_nearest(predicted_price[0], 5000)

    st.subheader("Predict Price for New Input")
    st.write(input_df)
    st.write('Predicted Price:', rounded_price)

    # EVALUATE MODEL 
    test_score, mae = evaluate_model(model, X, y)
    with st.sidebar.expander(f"{model_choice} Model Evaluation", expanded=True):
        st.sidebar.write(f"Test Score: {test_score:.4f}")
        st.sidebar.write(f"Mean Absolute Error: {mae:.2f}")

# Optionally, you could also add the feature importance if needed
# if hasattr(model, 'feature_importances_'):
#     st.subheader("Feature Importance")
#     importance = model.feature_importances_
#     features = X.columns
#     importance_df = pd.DataFrame({'Feature': features, 'Importance': importance})
#     importance_df = importance_df.sort_values(by="Importance", ascending=False)
#     st.bar_chart(importance_df.set_index("Feature"))
