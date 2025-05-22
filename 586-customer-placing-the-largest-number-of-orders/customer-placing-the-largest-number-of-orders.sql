-- Write your PostgreSQL query statement below
SELECT customer_number FROM (SELECT customer_number, count(*) FROM orders GROUP BY customer_number) ORDER BY count DESC LIMIT 1