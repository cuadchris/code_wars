/*
https://platform.stratascratch.com/coding/9942-largest-olympics?code_type=1

Find the Olympics with the highest number of athletes. The Olympics game is a combination of the year and the
season, and is found in the 'games' column. Output the Olympics along with the corresponding number of athletes.

Table: olympics_athletes_events
*/

WITH cte AS (
    SELECT games,
        count(DISTINCT id) AS athletes_count
    FROM olympics_athletes_events
    GROUP BY games
    ORDER BY athletes_count DESC
)
SELECT *
FROM cte
WHERE athletes_count = (
        SELECT max(athletes_count)
        FROM cte
    )