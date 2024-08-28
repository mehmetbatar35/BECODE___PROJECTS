# 1. We want to highlight 10 wines to increase our sales. Which ones should we choose and why?


import sqlite3
import pandas as pd

db_path = './db/vivino.db'

conn = sqlite3.connect(db_path)


create_table_sql = '''
CREATE TEMPORARY TABLE wine_performance AS
SELECT 
    w.id,
    w.name as wine_name,
    ROUND((v.ratings_average / NULLIF(v.price_euros, 0)) * 100, 2) AS rating_per_price,
    v.ratings_average,
    v.ratings_count,
    v.price_euros
from 
    wines w
JOIN
    vintages v ON w.id = v.wine_id   
WHERE
    v.ratings_count > 0 and v.price_euros > 0;'''

select_sql = '''
SELECT 
    wine_name,
    ratings_average,
    ratings_count,
    rating_per_price,
    price_euros
from 
    wine_performance
ORDER BY
    ratings_average DESC, ratings_count DESC, rating_per_price DESC
LIMIT 10;  

'''
with conn:
    conn.execute(create_table_sql)


df = pd.read_sql_query(select_sql, conn)
conn.close()

csv_file_path = "01.csv"

df.to_csv(csv_file_path, index = False)


print("Data has been successfully exported to 01.csv")