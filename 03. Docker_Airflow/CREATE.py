import pandas as pd
import sqlite3

teams_df = pd.read_csv(r'C:\Users\mehme\becode---\BECODE___PROJECTS\03. Docker_Airflow\New_csv_files\teams.csv')
matches_df = pd.read_csv(r'C:\Users\mehme\becode---\BECODE___PROJECTS\03. Docker_Airflow\New_csv_files\matches.csv')
match_stats_df = pd.read_csv(r'C:\Users\mehme\becode---\BECODE___PROJECTS\03. Docker_Airflow\New_csv_files\match_statistics.csv')


conn = sqlite3.connect('football_prediction.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        TeamID INT PRIMARY KEY,
        TeamName VARCHAR(255)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS matches (
        MatchID INT PRIMARY KEY,
        Div VARCHAR(50),
        Date DATE,
        Time TIME,
        HomeTeamID INT,
        AwayTeamID INT,
        FTHG INT,
        FTAG INT,
        FTR VARCHAR(10),
        HTHG INT,
        HTAG INT,
        HTR VARCHAR(10),
        FOREIGN KEY (HomeTeamID) REFERENCES teams(TeamID),
        FOREIGN KEY (AwayTeamID) REFERENCES teams(TeamID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS match_statistics (
        MatchID INT PRIMARY KEY,
        HSCR INT,
        ASCR INT,
        HST INT,
        AST INT,
        HF INT,
        AF INT,
        HC INT,
        AC INT,
        HY INT,
        AY INT,
        HR INT,
        AR INT,
        FOREIGN KEY (MatchID) REFERENCES matches(MatchID)
    )
''')

conn.commit()

# Insert the CSV data into the tables
teams_df.to_sql('teams', conn, if_exists='append', index=False)
matches_df.to_sql('matches', conn, if_exists='append', index=False)
match_stats_df.to_sql('match_statistics', conn, if_exists='append', index=False)

# Close the connection
conn.close()