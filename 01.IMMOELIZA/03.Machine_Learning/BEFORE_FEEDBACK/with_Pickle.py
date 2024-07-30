from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


def print_score(y_test, y_pred, model_name):
    mae = mean_absolute_error(y_true = y_test, y_pred = y_pred)
    r_2 = r2_score(y_true = y_test, y_pred = y_pred)
    print(f"""
            Score for : {model_name}
            R² = {r_2} 
            MAE = {mae}    
        """)
    
absolute_path = "C:\Users\mehme\becode---\BECODE___PROJECTS\01.IMMOELIZA\02.Data_Analysis\df.pkl"

pickle.load(open(absolute_path, "rb"))