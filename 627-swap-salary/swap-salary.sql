-- Write your PostgreSQL query statement below
UPDATE Salary set sex = CASE WHEN sex='m' then 'f' WHEN sex='f' THEN 'm' END