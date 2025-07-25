# Write your MySQL query statement below
SELECT Students.student_id, 
Students.student_name, 
Subjects.subject_name, 
count(Examinations.subject_name) AS attended_exams 
FROM Students 
CROSS JOIN Subjects 
LEFT JOIN Examinations  
ON Students.student_id=Examinations.student_id 
AND Subjects.subject_name = Examinations.subject_name
GROUP BY student_id, student_name, subject_name 
ORDER BY student_id, subject_name