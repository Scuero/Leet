-- Write your PostgreSQL query statement below
SELECT Users.name, COALESCE(travelled_distance, 0) AS travelled_distance FROM Users LEFT JOIN 
(SELECT user_id, SUM(distance) AS travelled_distance  
FROM Rides GROUP BY user_id)
ON Users.id=user_id ORDER BY travelled_distance DESC