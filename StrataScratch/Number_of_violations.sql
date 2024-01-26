/*
https://platform.stratascratch.com/coding/9728-inspections-that-resulted-in-violations?code_type=1

You're given a dataset of health inspections. Count the number of violation in an inspection in 'Roxanne Cafe'
for each year. If an inspection resulted in a violation, there will be a value in the 'violation_id' column.
Output the number of violations by year in ascending order.

Table: sf_restaurant_health_violations
*/

SELECT EXTRACT (
        YEAR
        FROM inspection_date::DATE
    ) AS YEAR,
    count(*) AS n_inspections
FROM sf_restaurant_health_violations
WHERE business_name = 'Roxanne Cafe'
    AND violation_id IS NOT NULL
GROUP BY YEAR
ORDER BY YEAR