/*
https://platform.stratascratch.com/coding/514-marketing-campaign-success-advanced?code_type=1

You have a table of in-app purchases by user. Users that make their first in-app purchase are placed in a
marketing campaign where they see call-to-actions for more in-app purchases. Find the number of users that made
additional in-app purchases due to the success of the marketing campaign.

The marketing campaign doesn't start until one day after the initial in-app purchase so users that only made
one or multiple purchases on the first day do not count, nor do we count users that over time purchase only the
products they purchased on the first day.

Table: marketing_campaign
*/

with cte as (
    select
        user_id,
        first_value(created_at) over(partition by user_id order by created_at) as fp_date
    from marketing_campaign
),

cte2 as (
    select
        mc.user_id,
        mc.created_at,
        array_agg(product_id) as p_ids
    from marketing_campaign mc
    join cte c on c.user_id = mc.user_id
    where created_at = fp_date
    group by 1, 2
)

select
    count(distinct mc.user_id)
from cte2
join marketing_campaign mc on mc.user_id = cte2.user_id
and mc.created_at > cte2.created_at
and mc.product_id not in (select unnest(p_ids))