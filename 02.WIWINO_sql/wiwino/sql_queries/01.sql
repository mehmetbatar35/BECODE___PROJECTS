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
    v.ratings_count > 0 and v.price_euros > 0;

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