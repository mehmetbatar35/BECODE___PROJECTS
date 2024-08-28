SELECT count(id)
FROM wines;

SELECT *
FROM wines;

SELECT count(id)
FROM wines;

SELECT count(id)
FROM vintages;

SELECT *
FROM vintages;

SELECT w.name, v.price_euros
FROM vintages v
JOIN wines w on w.id = v.wine_id
ORDER BY v.price_euros DESC
LIMIT 10;