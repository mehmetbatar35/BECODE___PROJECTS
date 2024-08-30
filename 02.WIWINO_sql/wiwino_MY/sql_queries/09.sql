





-- Best Value Wines
-- Question: Which wines offer the best value for money, considering their ratings and prices?
-- Data Needed: Ratings and prices (vintages).


SELECT 
    name,
    ratings_average,    
    ratings_count,
    price_euros,
    (ratings_average / price_euros) value_for_money
FROM vintages
ORDER BY value_for_money DESC
LIMIT 10;