
# -- 2. We have a limited marketing budget for this year. Which country should we prioritise and why?


import sqlite3
import pandas as pd

db_path = './db/vivino.db'

query = '''
SELECT 
        c.name as country_name, 
        count(w.id) as total_wines,
        avg(w.ratings_average) average_wine_rating, 
        sum(w.ratings_count) as total_ratings, 
        c.users_count,
        c.wines_count
FROM wines w
JOIN regions r ON w.region_id = r.id
JOIN countries c ON c.code = r.country_code
GROUP BY c.name
ORDER BY average_wine_rating DESC, total_ratings DESC, c.users_count DESC
LIMIT 10;
'''

conn = sqlite3.connect(db_path)

df = pd.read_sql_query(query, conn)

conn.close()

csv_file_path = '02.csv'

df.to_csv(csv_file_path, index=False)

print(f"Data has been written to {csv_file_path}")
