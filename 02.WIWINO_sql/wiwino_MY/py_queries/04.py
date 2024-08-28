
import sqlite3
import pandas as pd

db_path = './db/vivino.db'

query = '''
SELECT
    w.id as wine_id,
    w.name as wine_name,
    w.url as wine_url,
    k.name as keywords,
    sum(kw.count) as total_user_count
FROM 
    wines w
JOIN
    keywords_wine kw ON w.id = kw.wine_id
join 
    keywords k ON k.id = kw.keyword_id
WHERE  
    k.name IN ('coffee', 'toast', 'green apple', 'cream', 'citrus')    
GROUP BY
    w.id, w.name, w.url, k.name    
HAVING
    count(DISTINCT k.name) = 1
    AND sum(kw.count) >= 10
ORDER BY
    total_user_count DESC; 
'''

conn = sqlite3.connect(db_path)

df = pd.read_sql_query(query, conn)

conn.close()

csv_file_path = '04.csv'

df.to_csv(csv_file_path, index=False)

print(f"Data has been written to {csv_file_path}")