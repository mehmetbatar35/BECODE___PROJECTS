import pandas as pd

file = r"C:\Users\mehme\becode---\BECODE___PROJECTS\01.IMMOELIZA\02.Data_Analysis\final_dataset.csv"
df = pd.read_csv(file)

print(df.head())

df.columns = df.columns.str.lower()
print(df.columns)

print(df)

# df = df.drop(['url'])



