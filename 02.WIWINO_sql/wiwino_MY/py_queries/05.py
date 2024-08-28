#  5. We would like to select wines that are easy to find all over the world. Find the top 3 most common grapes all over the world and for each grape, give us the the 5 best rated wines.


import sqlite3
import pandas as pd

connexion = sqlite3.connect('./db/vivino.db')
cursor = connexion.cursor()
import sys

sys.stdout.reconfigure(encoding='utf-8')

query5 = '''
SELECT 
    g.id as grape_id,
    g.name AS grape_name,
    sum(m.wines_count) AS total_wines_count
FROM 
    grapes g
JOIN 
    most_used_grapes_per_country m ON g.id = m.grape_id
GROUP BY
    g.id, g.name    
ORDER BY
    total_wines_count DESC
LIMIT 3;
'''
cursor.execute(query5)
result = cursor.fetchall()



top_grape = []

for i in range(len(result)):
    top_grape.append(result[i][1])
    print(f"The number {i + 1} popular grape is {result[i][1]}. There are {result[i][2]} wines made of it.")

results = []    

for grape in top_grape:
    query = f'''
        select 
            w.name AS wine,
            r.name as region,
            c.name as country,
            w.ratings_average AS rating
        from 
            wines w
        join regions r on w.region_id = r.id
        join countries c on c.code = r.country_code
        where 
            w.name like '%{grape}%'
        ORDER BY 
            ratings_average DESC, ratings_count DESC
        LIMIT 5
        '''
    cursor.execute(query)
    result = cursor.fetchall()
    # results.append(result)

    for wine in result:
        results.append({
            'grape' : grape,
            'wine': wine[0],
            'region': wine[1],
            'country': wine[2],
            'rating': wine[3]
        })

df = pd.DataFrame(results)

csv_file_path = '05.csv'
df.to_csv(csv_file_path, index= False, encoding='utf-8')

print(f"Results have been written to {csv_file_path}")
connexion.close()





for i, grape_results in enumerate(results):
    print(f"The best wines from {top_grape[i]} are: ")
    for wine in grape_results:
        print(f"{wine[0]}, from {wine[2]}, rated {wine[3]}")
    print("-------------------------------------")


