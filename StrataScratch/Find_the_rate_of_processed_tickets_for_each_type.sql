/*
Find the rate of processed tickets for each type.

Table: facebook_complaints
*/

SELECT type,
    SUM(
        CASE
            WHEN processed THEN 1
            ELSE 0
        END
    )::NUMERIC / COUNT(*) AS processed_rate
FROM facebook_complaints
GROUP BY type