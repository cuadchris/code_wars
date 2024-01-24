/*
Write a query that returns the number of unique users per client per month

Table: fact_events
*/

SELECT client_id,
    EXTRACT(
        month
        from time_id
    ) as month,
    count(DISTINCT user_id) as users_num
FROM fact_events
GROUP BY client_id,
    EXTRACT(
        month
        from time_id
    )