-- 2. We have a limited marketing budget for this year. Which country should we prioritise and why?





SELECT 
        c.name as country_name, 
        count(w.id) as total_wines,
        avg(w.ratings_average) average_wine_rating, 
        sum(w.ratings_count) as total_ratings, 
        c.users_count,
        c.wines_count
FROM wines w
JOIN regions r ON w.region_id = r.id
JOIN countries c ON c.code = r.country_code
GROUP BY c.name
ORDER BY average_wine_rating DESC, total_ratings DESC, c.users_count DESC
LIMIT 10;



