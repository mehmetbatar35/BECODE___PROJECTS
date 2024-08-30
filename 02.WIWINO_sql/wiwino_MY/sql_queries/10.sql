-- Question: Which wines are most popular among different user demographics (e.g., by country or region of the users)?



-----------COUNTRIES



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
