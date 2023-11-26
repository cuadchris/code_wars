/*
Find the percentage of shipable orders.
Consider an order is shipable if the customer's address is known.

Tables: orders, customers
*/

SELECT
    100 * SUM(CASE WHEN is_shipable THEN 1 END)::NUMERIC / COUNT(*) AS percent_shipable
FROM
    (SELECT
        o.id,
        CASE WHEN address IS NULL THEN False ELSE True END AS is_shipable
    FROM    
        orders o
    INNER JOIN
        customers c
    ON
        o.cust_id = c.id) sq