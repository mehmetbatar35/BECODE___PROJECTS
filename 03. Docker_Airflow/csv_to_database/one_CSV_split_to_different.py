import pandas as pd
import os

csv_file = 'csv_to_database/merged_file_common_columns.csv'

df =pd.read_csv(csv_file)

df = df.rename(columns={
    "AS": "ASCR",    
    "HS": "HSCR"
})
print(df.columns)

df = df[['Div', 'Date', 'Time', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR',
    'HTHG', 'HTAG', 'HTR', 'HSCR', 'ASCR', 'HST', 'AST', 'HF', 'AF', 'HC',
    'AC', 'HY', 'AY', 'HR', 'AR', 'B365H', 'B365D', 'B365A', 'BWH', 'BWD',
    'BWA', 'PSH', 'PSD', 'PSA', 'WHH', 'WHD', 'WHA', 'MaxH', 'MaxD', 'MaxA',
    'AvgH', 'AvgD', 'AvgA',]]

# 1. TEAMS

teams = pd.DataFrame(pd.concat([df['HomeTeam'], df['AwayTeam']]).unique(), columns=['TeamName'])
teams['TeamID'] = range(1, len(teams) + 1)
teams = teams[['TeamID', 'TeamName']]


# 2. MATCHES
team_mapping = dict(zip(teams['TeamName'], teams['TeamID']))

matches = df[['Div', 'Date', 'Time', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR']].copy()
matches['MatchID'] = range(1, len(matches) + 1)

matches['HomeTeamID'] = matches['HomeTeam'].map(team_mapping)
matches['AwayTeamID'] = matches['AwayTeam'].map(team_mapping)

matches = matches[['MatchID', 'Div', 'Date', 'Time', 'HomeTeamID', 'AwayTeamID', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR']]

# 3. Create the match_statistics DataFrame to hold all the statistics
match_statistics = df[['HSCR', 'ASCR', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']].copy()
match_statistics['MatchID'] = range(1, len(match_statistics) + 1)
match_statistics = match_statistics[['MatchID', 'HSCR', 'ASCR', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']]


print(teams.shape)
print(matches.shape)
print(match_statistics.shape)


directory = 'New_csv_files'
if not os.path.exists(directory):
    os.makedirs(directory)

all_dataframes = {
    "teams.csv" : teams,
    "matches.csv" : matches,
    "match_statistics.csv" : match_statistics,
}    

for filename, df in all_dataframes.items():
    file_path = os.path.join(directory, filename)
    df.to_csv(file_path, index = False)
print("All CSV files have been created successfully in the new directory")    