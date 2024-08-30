-- Vintage Quality Over Time
-- Question: How have wine ratings changed over time for different vintages, and which years produced the highest-rated wines?
-- Data Needed: Ratings by vintage year (vintages), wine information (wines).

SELECT 
    v.year,
    
    count(wine_id)
FROM vintages v
JOIN vintage_toplists_rankings t ON v.id = t.vintage_id
GROUP BY v.year
ORDER BY v.year;




-- SELECT count(*)
-- FROM vintages;

-- SELECT *
-- FROM vintage_toplists_rankings;