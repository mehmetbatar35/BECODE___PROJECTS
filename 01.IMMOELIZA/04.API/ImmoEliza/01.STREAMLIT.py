import pandas as pd
import pickle
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


# LOAD MODELS based on USER SELECTION
model_paths = {
    'gbr_model': r"03.Machine_Learning/gbr_model.pkl",
    'xgb_model': r"03.Machine_Learning/xgb_model.pkl",
    'scaler': r"03.Machine_Learning/scaler.pkl"
}


with open(model_paths['gbr_model'], 'rb') as f:
    gbr_model = pickle.load(f)
with open(model_paths['xgb_model'], 'rb') as f:
    xgb_model = pickle.load(f)
with open(model_paths['scaler'], 'rb') as f:
    scaler = pickle.load(f)

absolute_path = r"03.Machine_Learning/ready_for_modeling"
with open(absolute_path, 'rb') as f:
    df = pickle.load(f)


st.write(df.columns)
# st.write(df.garden.value_counts())

X = df.drop(columns = ['price'])
y = df['price']

st.title("Real Estate Price Prediction")


col1, col2, col3 = st.columns(3)


with col1:
    Brussels = st.checkbox("Brussels", value = False)
with col2:
    Flanders = st.checkbox("Flanders", value = False)
with col3:
    Wallonie = st.checkbox("Wallonie", value = False)

st.write("")

provinces_by_region = {
    'Brussels': ['Brussels'],
    'Flanders': ['West Flanders', 'Flemish Brabant', 'East Flanders', 'Limburg', 'Antwerp'],
    'Wallonie': ['Walloon Brabant', 'Luxembourg', 'Liège', 'Hainaut', 'Namur']             
}

selected_provinces = []
if Brussels:
    selected_provinces.extend(provinces_by_region['Brussels'])
if Flanders:
    selected_provinces.extend(provinces_by_region['Flanders'])
if Wallonie:
    selected_provinces.extend(provinces_by_region['Wallonie'])

# to ensure there are no duplicated
selected_provinces = list(set(selected_provinces))
province = st.selectbox('Province', selected_provinces)

if Brussels:
    df= df[df['Brussels'] == 1]
if Flanders:
    df= df[df['Flanders'] == 1]
if Wallonie:
    df= df[df['Wallonie'] == 1]


def user_input_features():
    constructionyear = st.number_input('Construction Year', min_value = 1895, max_value = 2024, value= 2000)
    if constructionyear < 1895 or constructionyear > 2024:
        st.warning('Please choose a year between 1895 and 2024.')
    livingarea = st.number_input('Living Area', 12, 446, 100)
    bathroom_count = st.slider('Bathroom Count', 0, 3, 0)
    bedroomcount = st.slider('Bedroom Count', 0, 8, 0)
    state_mapping = {'New': 5, 'Like New': 4, 'Good': 3, 'Fair': 2, 'Needs Renovation': 1}
    stateofbuilding = st.radio('State of Building', options= list(state_mapping.keys()), index = 2)
    stateofbuilding_value = state_mapping[stateofbuilding]


    kitchen_mapping = {'No_kitchen': 0, 'Basic Kitchen': 1, 'Modern Kitchen': 2, 'Luxury Kitchen': 3}
    sorted_kitchen_options = sorted(kitchen_mapping.keys(), key = lambda x: kitchen_mapping[x], reverse = True)
    kitchen = st.radio("Kitchen", options= sorted_kitchen_options, index = 3)
    kitchen_value = kitchen_mapping[kitchen]    

    rating_dict = {'G': 1, 'F': 2, 'E': 3, 'D': 4, 'C': 5, 'B': 6, 'A': 7, 'A+': 8, 'A++': 9}
    sorted_peb_options = sorted(rating_dict.keys(), key = lambda x: rating_dict[x], reverse = True)
    peb = st.selectbox("PEB", options = sorted_peb_options, index = 0)
    peb_value =rating_dict[peb]

    garden = st.checkbox("Garden", value=False)
    garden_value = 1 if garden else 0
    

    default_values = {col: 0 for col in X.columns}
    default_values.update({
        'bathroomcount': bathroom_count,
        'bedroomcount': bedroomcount,
        'constructionyear': constructionyear,
        'kitchen': kitchen_value,
        'livingarea': livingarea,
        'stateofbuilding': stateofbuilding_value,
        'peb': peb_value,
        'garden': garden_value
    })

    features = pd.DataFrame(default_values, index = [0])
    return features

input_df = user_input_features()

st.sidebar.header("Select Models")
gbr_selected = st.sidebar.checkbox("Gradient Boosting", value= False)
xgb_selected = st.sidebar.checkbox("XGBoost", value= False)

models = {}
if gbr_selected:
    models['Gradient Boosting'] = gbr_model
if xgb_selected:
    models['XGBoost'] = xgb_model    

def round_to_nearest(value, multiple):
    return round(value / multiple) * multiple


def evaluate_model(model, X, y):
    X_scaled = scaler.transform(X)
    y_pred = model.predict(X_scaled)
    test_score = model.score(X_scaled, y)
    mae = mean_absolute_error(y, y_pred)
    return test_score, mae


if st.button("Calculate Price"):
    if not models:
        st.error("Please select at least one model.")
    else:
        for model_name, model in models.items():
            input_scaled = scaler.transform(input_df)
            predicted_price = model.predict(input_scaled)

            rounded_price = round_to_nearest(predicted_price[0], 100)

            st.subheader("Predict Price: ")
            st.write(input_df)
            st.write('Predicted Price:', rounded_price)
            # st.balloons()

            # EVALUATE MODEL 
            test_score, mae = evaluate_model(model, X, y)
            with st.sidebar.expander(f"{model_name} Model Evaluation", expanded = True):
                st.sidebar.write(f"Test Score: {test_score:.4f}")
                st.sidebar.write(f"Mean Absolute Error: {mae:.2f}")






















# with st.sidebar.expander('Model Evaluation', expanded= True):
#     st.sidebar.write("Test Score:", test_score)
#     st.sidebar.write("Mean Absolute Error:", mae)

#     mean_price = y_test.mean()
#     relative_error = mae / mean_price
#     st.sidebar.write("Relative Error:", relative_error)




