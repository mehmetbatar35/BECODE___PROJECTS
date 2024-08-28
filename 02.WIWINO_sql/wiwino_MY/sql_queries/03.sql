-- 3. We would like to give awards to the best wineries. Come up with 3 relevant ones. Which wineries should we choose and why?

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