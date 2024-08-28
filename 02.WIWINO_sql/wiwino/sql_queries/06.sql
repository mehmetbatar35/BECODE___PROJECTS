SELECT 
    r.country_code AS country_code, 
    c.name AS country_name, 
    avg(w.ratings_average) as average_rating
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

    AVG(v.ratings_average) AS average_rating
FROM
    vintages v
JOIN wines w ON v.wine_id = w.id 
JOIN regions r ON w.region_id = r.id
join countries c ON r.country_code = c.code
GROUP BY
    r.country_code, c.name
ORDER BY
    average_rating DESC;