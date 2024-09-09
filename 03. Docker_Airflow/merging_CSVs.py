import pandas as pd
import os

csv_directory = 'csv_files'

csv_files = [i for i in os.listdir(csv_directory)]

dataframes = [pd.read_csv(os.path.join(csv_directory, file)) for file in csv_files]


first_df_columns = dataframes[0].columns.tolist()

common_columns = [col for col in first_df_columns if all(col in df.columns for df in dataframes)]

filtered_dataframes = [df[common_columns] for df in dataframes]

merged_df = pd.concat(filtered_dataframes, ignore_index=True)

print(merged_df.shape)
print(len(merged_df[merged_df.isnull().all(axis=1)]))

merged_df = merged_df.dropna(how='all')
print(merged_df.shape)
print(len(merged_df[merged_df.isnull().all(axis=1)]))


merged_df.to_csv('csv_to_database/Merged_file_common_columns.csv', index=False)

























# for index, i in enumerate(dataframes):
#     print(f"Dataframe {index + 1} shape: {i.shape}", end = " ")
#     nul_rows = len(i[i.isnull().all(axis = 1)])
#     print(f"Null rows: {nul_rows}")
#     if nul_rows > 0 :
#         dataframes[index] = i.dropna(how = 'all')
    
# common_columns = set(dataframes[0].columns)
# for df in dataframes[1:]:
#     common_columns.intersection_update(df.columns)

# common_columns = list(common_columns)

# filtered_dataframes = [df[common_columns] for df in dataframes]

# merged_df = pd.concat(filtered_dataframes, ignore_index= True)

# merged_df.to_csv('merged_file_common_columns.csv', index=False)


# print(merged_df.shape)

