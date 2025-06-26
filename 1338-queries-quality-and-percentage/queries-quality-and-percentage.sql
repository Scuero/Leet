# Write your MySQL query statement below
SELECT query_name, 
ROUND(AVG(CAST(rating AS DECIMAL) / position), 2) as quality, 
ROUND(SUM(CASE WHEN rating <3 THEN 1 ELSE 0 END)/COUNT(*)*100,2) AS poor_query_percentage 
FROM queries 
GROUP BY query_name