
# -- Question: Which wines are most popular among different user demographics (e.g., by country or region of the users)?



# -----------COUNTRIES


import sqlite3
import pandas as pd

db_path = 'db/vivino.db'

query = '''
SELECT 
    c.name as country_name,
    count(w.id) total_wine,
    AVG(ratings_average) AS rating_averages,
    sum(ratings_count) AS rating_count
FROM wines w
JOIN regions r ON w.region_id = r.id
JOIN countries c ON r.country_code = c.code
GROUP BY country_name
ORDER BY total_wine DESC
LIMIT 10;


'''

conn = sqlite3.connect(db_path)

df = pd.read_sql_query(query, conn)

conn.close()

csv_file_path = '10.csv'

df.to_csv(csv_file_path, index=False)

print(f"Data has been written to {csv_file_path}")



