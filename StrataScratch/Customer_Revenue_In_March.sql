/*
https://platform.stratascratch.com/coding/9782-customer-revenue-in-march?code_type=1


Calculate the total revenue from each customer in March 2019. Include only customers who were active in March
2019.

Output the revenue along with the customer id and sort the results based on the revenue in descending order.

Table: orders

Example data:
-----------------------------------------------------------------
| id | cust_id | order_date | order_details | total_order_cost  |
-----------------------------------------------------------------
|  1 |    3    | 2019-03-04 |     Coat      |       100         |
|  2 |    3    | 2019-03-01 |     Shoes     |        80         |
|  3 |    3    | 2019-03-07 |     Skirt     |        30         |
|  4 |    7    | 2019-02-01 |     Coat      |        25         |
|  5 |    7    | 2019-03-10 |     Shoes     |        80         |
|  6 |   15    | 2019-02-01 |     Boats     |       100         |
|  7 |   15    | 2019-01-11 |     Shirts    |        60         |
|  8 |   15    | 2019-03-11 |    Slipper    |        20         |
|  9 |   15    | 2019-03-01 |     Jeans     |        80         |
| 10 |   15    | 2019-03-09 |     Shirts    |        50         |
| 11 |    5    | 2019-02-01 |     Shoes     |        80         |
| 12 |   12    | 2019-01-11 |     Shirts    |        60         |
| 13 |   12    | 2019-03-11 |    Slipper    |        20         |
| 14 |    4    | 2019-02-01 |     Shoes     |        80         |
| 15 |    4    | 2019-01-11 |     Shirts    |        60         |
| 16 |    3    | 2019-04-19 |     Shirts    |        50         |
| 17 |    7    | 2019-04-19 |      Suit     |       150         |
| 18 |   15    | 2019-04-19 |     Skirt     |        30         |
| 19 |   15    | 2019-04-20 |    Dresses    |       200         |
-----------------------------------------------------------------
*/

SELECT
    cust_id,
    SUM(total_order_cost) AS revenue
FROM
    orders
WHERE
    EXTRACT(MONTH FROM order_date) = 3 AND
    EXTRACT(YEAR FROM order_date) = 2019
GROUP BY
    cust_id
ORDER BY revenue DESC