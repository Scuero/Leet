-- Write your PostgreSQL query statement below

SELECT id FROM (SELECT *, LAG(recordDate) OVER (ORDER BY recordDate) AS fechaAnt, LAG(temperature) OVER (ORDER BY recordDate) AS tempAnt FROM Weather) WHERE recorddate-fechaAnt=1 AND temperature>tempAnt