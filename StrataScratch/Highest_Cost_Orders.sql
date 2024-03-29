/*
https://platform.stratascratch.com/coding/9915-highest-cost-orders?code_type=1

Find the customer with the highest daily total order cost between 2019-02-01 to 2019-05-01. If customer had
more than one order on a certain day, sum the order costs on daily basis. Output customer's first name, total
cost of their items, and the date.

For simplicity, you can assume that every first name in the dataset is unique.

Tables: customers, orders
*/

select c.first_name,
    sum(o.total_order_cost) as total_order_cost,
    o.order_date
from customers c
    join orders o on c.id = o.cust_id
where o.order_date between '2019-02-01' and '2019-05-01'
group by first_name,
    cust_id,
    order_date
order by total_order_cost desc
limit 1