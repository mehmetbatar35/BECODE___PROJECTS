
import sqlite3
import pandas as pd

db_path = './db/vivino.db'

query = '''
SELECT 
    wi.id AS winery_id,
    wi.name as winery_name,
    avg(w.ratings_average) as avg_wine_rating,
    sum(w.ratings_count) as total_ratings_count
from 
    wineries wi
JOIN
    wines w ON wi.id = w.winery_id
GROUP BY 
    wi.id, wi.name
ORDER BY
    avg_wine_rating DESC, total_ratings_count DESC
LIMIT 3;  
'''

conn = sqlite3.connect(db_path)

df = pd.read_sql_query(query, conn)

conn.close()

csv_file_path = '03.csv'

df.to_csv(csv_file_path, index=False)

print(f"Data has been written to {csv_file_path}")