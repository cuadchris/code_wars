/*
Find the number of employees working in the Admin department that joined in April or later.

Table: worker
*/


SELECT COUNT(*) AS n_admins
FROM worker
WHERE lower(department) LIKE 'admin'
    AND EXTRACT(
        MONTH
        FROM joining_date
    ) >= 4