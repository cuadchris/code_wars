/*
https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=1

Calculate each user's average session time. A session is defined as the time difference between a page_load and
page_exit. For simplicity, assume a user has only 1 session per day and if there are multiple of the same events
on that day, consider only the latest page_load and earliest page_exit, with an obvious restriction that load
time event should happen before exit time event . Output the user_id and their average session time.

Table: facebook_web_log

| user_id | timestamp           | action     |
|---------|---------------------|------------|
| int     | datetime            | varchar    |
|         |                     |            |
| 0       | 2019-04-25 13:30:15 | page_load  |
| 0       | 2019-04-25 13:30:18 | page_load  |
| 0       | 2019-04-25 13:30:40 | scroll_down|
| 0       | 2019-04-25 13:30:45 | scroll_up  |
| 0       | 2019-04-25 13:31:10 | scroll_down|
| 0       | 2019-04-25 13:31:25 | scroll_down|
| 0       | 2019-04-25 13:31:40 | page_exit  |
| 1       | 2019-04-25 13:40:00 | page_load  |
| 1       | 2019-04-25 13:40:10 | scroll_down|
| 1       | 2019-04-25 13:40:15 | scroll_down|
| 1       | 2019-04-25 13:40:20 | scroll_down|
| 1       | 2019-04-25 13:40:25 | scroll_down|
| 1       | 2019-04-25 13:40:30 | scroll_down|
| 1       | 2019-04-25 13:40:35 | page_exit  |
| 2       | 2019-04-25 13:41:21 | page_load  |
| 2       | 2019-04-25 13:41:30 | scroll_down|
| 2       | 2019-04-25 13:41:35 | scroll_down|
| 2       | 2019-04-25 13:41:40 | scroll_up  |
| 1       | 2019-04-26 11:15:00 | page_load  |
| 1       | 2019-04-26 11:15:10 | scroll_down|
| 1       | 2019-04-26 11:15:20 | scroll_down|
| 1       | 2019-04-26 11:15:25 | scroll_up  |
| 1       | 2019-04-26 11:15:35 | page_exit  |
| 0       | 2019-04-28 14:30:15 | page_load  |
| 0       | 2019-04-28 14:30:10 | page_load  |
| 0       | 2019-04-28 13:30:40 | scroll_down|
| 0       | 2019-04-28 15:31:40 | page_exit  |
*/

select
    user_id,
    avg(avg_sesh)
from (select
        f1.user_id,
        date(f1.timestamp) as date,
        min(f2.timestamp) - max(f1.timestamp) as avg_sesh
    from facebook_web_log f1
    join facebook_web_log f2
    on f1.user_id = f2.user_id
    where f1.action = 'page_load'
    and f2.action = 'page_exit'
    and f2.timestamp > f1.timestamp
    group by 1, 2) sq
group by 1