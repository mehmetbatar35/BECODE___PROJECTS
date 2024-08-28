
-- 7. One of our VIP clients likes Cabernet Sauvignon and would like our top 5 recommendations. Which wines would you recommend to him?

SELECT *
FROM wines
WHERE name LIKE '%Cabernet Sauvignon%'
ORDER BY ratings_average desc, ratings_count DESC
LIMIT 5
