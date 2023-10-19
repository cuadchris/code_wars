/*
https://platform.stratascratch.com/coding/10322-finding-user-purchases?code_type=1

Write a query that'll identify returning active users. A returning active user is a user that has made a second
purchase within 7 days of any other of their purchases. Output a list of user_ids of these returning active
users.

Table: amazon_transactions
*/

with users_and_days_between as
(select
    user_id,
    created_at - lag(created_at) over(partition by user_id order by created_at) as days
from amazon_transactions)

select
    distinct user_id
from users_and_days_between
where days <= 7