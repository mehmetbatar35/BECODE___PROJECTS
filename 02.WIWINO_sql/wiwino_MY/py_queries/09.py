# -- Question: Which wines are most popular among different user demographics (e.g., by country or region of the users)?




import sqlite3
import pandas as pd

db_path = 'db/vivino.db'

query = '''
SELECT 
    name,
    ratings_average,    
    ratings_count,
    price_euros,
    (ratings_average / price_euros) value_for_money
FROM vintages
ORDER BY value_for_money DESC
LIMIT 10;
'''

conn = sqlite3.connect(db_path)

df = pd.read_sql_query(query, conn)

conn.close()

csv_file_path = '09.csv'

df.to_csv(csv_file_path, index=False)

print(f"Data has been written to {csv_file_path}")
