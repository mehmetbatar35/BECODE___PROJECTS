



-- Wine Popularity by User Demographics
-- Question: Which wines are most popular among different user demographics (e.g., by country or region of the users)?
-- Data Needed: User demographics (potentially inferred from users_count in countries), wine ratings (wines, vintages).



SELECT 
    r.name as region_name,
    count(w.id) total_wine,
    AVG(ratings_average) AS rating_averages,
    sum(ratings_count) AS rating_count
FROM wines w
JOIN regions r ON w.region_id = r.id
GROUP BY r.name
ORDER BY total_wine DESC
LIMIT 10;


































-- Wineries with Consistent Quality
-- Question: Which wineries have consistently produced high-rated wines over multiple vintages?
-- Data Needed: Wine ratings by winery and vintage (wineries, wines, vintages).


-- SELECT 
--     wn.name as winery_name,
--     AVG(v.ratings_average) AS avg_rating,
--     -- count(v.id) as vintage_count
-- FROM 
--     wineries wn
-- JOIN 
--     wines w ON wn.id = w.winery_id
-- JOIN
--     vintages v on v.wine_id = w.id
-- GROUP BY    
--     wn.name
-- ORDER BY
--     avg_rating DESC;


-- SELECT 
--     wn.name as winery_name,
--     sum(w.ratings_count),
--     sum(w.ratings_average) AS avg_rating,
--     COUNT(w.id)
-- FROM 
--     wineries wn
-- JOIN 
--     wines w ON wn.id = w.winery_id

-- GROUP BY    
--     wn.name
-- ORDER BY
--     avg_rating DESC;