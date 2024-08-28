-- 5. We would like to select wines that are easy to find all over the world. Find the top 3 most common grapes all over the world and for each grape, give us the the 5 best rated wines.




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

SELECT *
FROM wines
WHERE name LIKE '%Cabernet Sauvignon%'
ORDER BY ratings_average DESC, ratings_count DESC
LIMIT 5;

SELECT *
FROM wines
WHERE name LIKE '%Merlot%'
ORDER BY ratings_average DESC, ratings_count DESC
LIMIT 5;

SELECT *
FROM wines
WHERE name LIKE '%Chardonnay%'
ORDER BY ratings_average DESC, ratings_count DESC
LIMIT 5;



