import pandas as pd
import pickle

absolute_path = r"04.API/ImmoEliza/after_outlier_df.pkl"

with open(absolute_path, 'rb') as f:
    df = pickle.load(f)



pd.set_option('display.max_columns', None)

# print(df.head())

one_hot_sub = pd.get_dummies(df['subtypeofproperty']).astype('int64')
one_hot_df = pd.get_dummies(df['region']).astype('int64')
df = pd.concat([df, one_hot_sub, one_hot_df], axis=1)
df.drop(['subtypeofproperty', 'region'], axis=1, inplace=True)

df.groupby('province')['price'].mean()

order_mapping = {'West Flanders': 1, 'Walloon Brabant': 2, 'Luxembourg': 3, 'Liège': 4, 'Limburg': 5, 'Hainaut': 6, 'Flemish Brabant': 7, 'East Flanders': 8, 'Namur': 9, 'Brussels': 10, 'Antwerp': 11}
df['province'] = df['province'].map(order_mapping)

rating_dict = {'G': 1, 'F_E': 2, 'F_D': 3, 'F': 4, 'F_C': 5, 'E_D': 6, 'E': 7, 'D': 8, 'C': 9, 'B_A': 10, 'B': 11, 'G_C': 12, 'E_C': 13, 'A_A+': 14, 'A': 15, 'A+': 16, 'A++': 17}
df['peb'] = df['peb'].map(rating_dict)

# print(df.head())

with open("ready_for_modeling", "wb") as f:
    pickle.dump(df, f )