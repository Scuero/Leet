-- Write your PostgreSQL query statement below

SELECT name, bonus FROM (Employee e LEFT JOIN Bonus b ON e.empId=b.empId) WHERE bonus<1000 OR bonus is NULL