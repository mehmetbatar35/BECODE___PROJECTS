import pandas as pd

csv_file = 'csv_to_database/merged_file_common_columns.csv'

df = pd.read_csv(csv_file)

print(df.columns)