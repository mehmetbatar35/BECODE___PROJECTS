

# 7. One of our VIP clients likes Cabernet Sauvignon and would like our top 5 recommendations. Which wines would you recommend to him?

import sqlite3
import pandas as pd

db_path = './db/vivino.db'

query = '''
SELECT *
FROM wines
WHERE name LIKE '%Cabernet Sauvignon%'
ORDER BY ratings_average DESC, ratings_count DESC
LIMIT 5;
'''

conn = sqlite3.connect(db_path)

df = pd.read_sql_query(query, conn)

conn.close()

csv_file_path = '07.csv'

df.to_csv(csv_file_path, index=False)

print(f"Data has been written to {csv_file_path}")
