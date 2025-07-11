-- Write your PostgreSQL query statement below
SELECT Employees.name, unique_id 
FROM Employees 
LEFT JOIN EmployeeUNI 
ON EmployeeUNI.id=Employees.id