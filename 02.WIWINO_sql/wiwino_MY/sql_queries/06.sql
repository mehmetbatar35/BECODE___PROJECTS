
-- 6. We would like to create a country leaderboard. Come up with a visual that shows the average wine rating for each country. Do the same for the vintages.

SELECT 
    r.country_code AS country_code, 
    c.name AS country_name, 
    avg(w.ratings_average) as average_rating,
    w.ratings_count

FROM wines w
JOIN regions r ON w.region_id = r.id
join countries c ON r.country_code = c.code
GROUP BY 
    r.country_code, c.name
ORDER BY
    average_rating DESC;


----

SELECT
    r.country_code AS country_code,
    c.name AS country_name,

    AVG(v.ratings_average) AS average_rating,
    v.ratings_count
FROM
    vintages v
JOIN wines w ON v.wine_id = w.id 
JOIN regions r ON w.region_id = r.id
join countries c ON r.country_code = c.code
GROUP BY
    country_code, country_name
ORDER BY
    average_rating DESC;



