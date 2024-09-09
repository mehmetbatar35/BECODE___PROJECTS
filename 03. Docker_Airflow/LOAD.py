
import pandas as pd
import sqlite3


teams_df = pd.read_csv(r'C:\Users\mehme\becode---\BECODE___PROJECTS\03. Docker_Airflow\New_csv_files\teams.csv')
matches_df = pd.read_csv(r'C:\Users\mehme\becode---\BECODE___PROJECTS\03. Docker_Airflow\New_csv_files\matches.csv')
match_stats_df = pd.read_csv(r'C:\Users\mehme\becode---\BECODE___PROJECTS\03. Docker_Airflow\New_csv_files\match_statistics.csv')


conn = sqlite3.connect('football_prediction.db')

teams_df.to_sql('teams', conn, if_exists='append', index=False)
matches_df.to_sql('matches', conn, if_exists='append', index=False)
match_stats_df.to_sql('match_statistics', conn, if_exists='append', index=False)

conn.close()