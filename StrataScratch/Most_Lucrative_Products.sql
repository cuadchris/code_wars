/*
You have been asked to find the 5 most lucrative products in terms of total revenue for the first half of 2022
(from January to June inclusive).

Output their IDs and the total revenue.

Table: online_orders
*/

WITH cte AS (
    SELECT product_id,
        SUM(cost_in_dollars * units_sold) AS revenue,
        RANK() OVER (
            ORDER BY SUM(cost_in_dollars * units_sold) DESC
        ) AS rnk
    FROM online_orders
    WHERE EXTRACT(
            MONTH
            FROM date
        ) BETWEEN 1 AND 6
    GROUP BY product_id
)
SELECT product_id,
    revenue
FROM cte
WHERE rnk <= 5;