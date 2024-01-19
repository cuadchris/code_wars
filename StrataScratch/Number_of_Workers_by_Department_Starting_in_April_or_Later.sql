/*
Find the number of workers by department who joined in or after April.

Output the department name along with the corresponding number of workers.

Sort records based on the number of workers in descending order.

Table: worker
*/


SELECT department,
    COUNT(worker_id) AS num_workers
FROM worker
WHERE EXTRACT(
        MONTH
        FROM joining_date
    ) >= 4
GROUP BY department
ORDER BY num_workers DESC