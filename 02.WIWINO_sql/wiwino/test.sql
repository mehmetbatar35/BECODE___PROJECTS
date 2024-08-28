
select name from sqlite_master where type = 'table';

-- 1. We want to highlight 10 wines to increase our sales. Which ones should we choose and why?


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


-- 2. We have a limited marketing budget for this year. Which country should we prioritise and why?

CREATE TEMPORARY TABLE toplist_counts AS
SELECT country_code, count(id) AS toplist_count
from toplists
GROUP BY country_code;

------------------------

CREATE TEMPORARY TABLE wineries_user_ratio AS
SELECT code as country_code,
        Round(CAST(wineries_count as float) / CAST(users_count as float) * 100, 2) AS wineries_user_ratio
from countries
where users_count > 0; 
------------------------


SELECT c.name as country_name,
        coalesce(t.toplist_count, 0) AS toplist_count,
        coalesce(w.wineries_user_ratio, 0) AS wineries_user_ratio,
        (coalesce(t.toplist_count, 0) * 0.5 + coalesce(w.wineries_user_ratio, 0) * 0.5) AS weighted_score
from countries c
left JOIN toplist_counts t ON c.code = t.country_code
LEFT JOIN wineries_user_ratio w ON c.code = w.country_code
ORDER BY weighted_score DESC
LIMIT 5;

	
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

-- 4. We detected that a big cluster of customers likes a specific combination of tastes. We identified a few keywords that match these tastes: coffee, toast, green apple, cream, and citrus (note that these keywords are case sensitive ⚠️). We would like you to find all the wines that are related to these keywords. Check that at least 10 users confirm those keywords, to ensure the accuracy of the selection. Additionally, identify an appropriate group name for this cluster.


SELECT
    w.id as wine_id,
    w.name as wine_name,
    w.url as wine_url,
    k.name as keywords,
    sum(kw.count) as total_user_count
FROM 
    wines w
JOIN
    keywords_wine kw ON w.id = kw.wine_id
join 
    keywords k ON k.id = kw.keyword_id
WHERE  
    k.name IN ('coffee', 'toast', 'green apple', 'cream', 'citrus')    
GROUP BY
    w.id, w.name, w.url, k.name    
HAVING
    count(DISTINCT k.name) = 1
    AND sum(kw.count) >= 10
ORDER BY
    total_user_count DESC;




select * FROM keywords;
select * FROM keywords_wine; 
-- select *, sum(count) FROM keywords_wine GROUP BY wine_id;
-- select * FROM wines ;

-- 5. We would like to select wines that are easy to find all over the world. Find the top 3 most common grapes all over the world and for each grape, give us the the 5 best rated wines.

SELECT *
FROM grapes
LIMIT 5;
SELECT *
FROM most_used_grapes_per_country
LIMIT 5;


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


-- 6. We would like to create a country leaderboard. Come up with a visual that shows the average wine rating for each country. Do the same for the vintages.


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
