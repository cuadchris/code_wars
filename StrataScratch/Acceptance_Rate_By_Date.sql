/*
https://platform.stratascratch.com/coding/10285-acceptance-rate-by-date?code_type=1

What is the overall friend acceptance rate by date? Your output should have the rate of acceptances by the date
the request was sent. Order by the earliest date to latest.


Assume that each friend request starts by a user sending (i.e., user_id_sender) a friend request to another user
(i.e., user_id_receiver) that's logged in the table with action = 'sent'. If the request is accepted, the table
logs action = 'accepted'. If the request is not accepted, no record of action = 'accepted' is logged.

Table: fb_friend_requests
*/

with cte as (
    select
        f1.user_id_sender,
        f1.user_id_receiver,
        f1.date,
        f1.action,
        f2.action
    from fb_friend_requests f1
    join fb_friend_requests f2
    on f1.user_id_sender = f2.user_id_sender and
    f1.user_id_receiver = f2.user_id_receiver and
    f2.date > f1.date
),

num_accepts as (
    select
        date,
        count(date)::float as accepted
    from cte
    group by date
),

num_requests as (
    select
        date,
        count(action)::float as requested
    from fb_friend_requests
    where action = 'sent'
    group by date
)

select
    nr.date,
    accepted / requested as percentage_acceptance
from num_requests nr
join num_accepts na on na.date = nr.date