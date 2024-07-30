import pandas as pd
import pickle
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler



absolute_path = r"C:\Users\mehme\becode---\BECODE___PROJECTS\01.IMMOELIZA\02.Data_Analysis\df.pkl"

with open(absolute_path, 'rb') as f:
    df = pickle.load(f)

st.title("Real Estate Price Prediction")

st.subheader("Dataset")
st.write(df.head())