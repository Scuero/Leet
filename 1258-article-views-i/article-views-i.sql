-- Write your PostgreSQL query statement below
SELECT author_id AS id FROM views GROUP BY author_id, viewer_id HAVING author_id=viewer_id