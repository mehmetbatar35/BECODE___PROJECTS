import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle

absolute_path = r"04.API/ImmoEliza/after_outlier_df.pkl"

preprocessor = pickle.load(open('04.API/ImmoEliza/after_outlier_df.pkl', 'rb'))

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

one_hot_sub = pd.get_dummies(df['subtypeofproperty']).astype('int64')
one_hot_df = pd.get_dummies(df['region']).astype('int64')
df = pd.concat([df, one_hot_sub, one_hot_df], axis=1)
df.drop(['subtypeofproperty', 'region'], axis=1, inplace=True)

df.groupby('province')['price'].mean()

order_mapping = {'West Flanders': 1, 'Walloon Brabant': 2, 'Luxembourg': 3, 'Liège': 4, 'Limburg': 5, 'Hainaut': 6, 'Flemish Brabant': 7, 'East Flanders': 8, 'Namur': 9, 'Brussels': 10, 'Antwerp': 11}
rating_dict = {'G': 1, 'F_E': 2, 'F_D': 3, 'F': 4, 'F_C': 5, 'E_D': 6, 'E': 7, 'D': 8, 'C': 9, 'B_A': 10, 'B': 11, 'G_C': 12, 'E_C': 13, 'A_A+': 14, 'A': 15, 'A+': 16, 'A++': 17}

df['province'] = df['province'].map(order_mapping)
df['peb'] = df['peb'].map(rating_dict)