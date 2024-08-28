
-- 4. We detected that a big cluster of customers likes a specific combination of tastes. 
-- We identified a few keywords that match these tastes: coffee, toast, green apple, cream, and citrus (note that these keywords are case sensitive ⚠️). 
-- We would like you to find all the wines that are related to these keywords. Check that at least 10 users confirm those keywords, to ensure the accuracy of the selection. 
-- Additionally, identify an appropriate group name for this cluster.


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