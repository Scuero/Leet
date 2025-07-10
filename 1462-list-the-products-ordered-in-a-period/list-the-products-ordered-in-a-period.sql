-- Write your PostgreSQL query statement below
SELECT product_name, unit
FROM
(SELECT product_id, SUM(unit) AS unit 
FROM (SELECT * 
FROM Orders 
WHERE order_date 
BETWEEN '2020-02-01' AND '2020-02-29') 
GROUP BY product_id
HAVING SUM(unit)>=100) AS filt
INNER JOIN Products 
ON Products.product_id= filt.product_id