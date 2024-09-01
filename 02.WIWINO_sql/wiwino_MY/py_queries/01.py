# 1. We want to highlight 10 wines to increase our sales. Which ones should we choose and why?


import sqlite3
import pandas as pd

db_path = './db/vivino.db'

query = '''
SELECT 
    v.name AS wine_name,
    avg(v.ratings_average) avg_rat,
    sum(v.ratings_count) count_sum,
    ROUND(AVG(v.ratings_average / NULLIF(v.price_euros, 0)) * 100, 2) AS rating_per_price
FROM 
    wines w
JOIN
    vintages v ON w.id = v.wine_id   
GROUP BY v.name
ORDER BY
    avg_rat DESC, 
    count_sum DESC,
    rating_per_price DESC
LIMIT 10;
'''

conn = sqlite3.connect(db_path)

df = pd.read_sql_query(query, conn)

conn.close()

csv_file_path = '01.csv'

df.to_csv(csv_file_path, index=False)

print(f"Data has been written to {csv_file_path}")