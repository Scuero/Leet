-- Write your PostgreSQL query statement below
SELECT MAX(num) as num from MyNumbers WHERE num in (SELECT num FROM MyNumbers GROUP BY num HAVING count(*)=1)