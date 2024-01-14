/*
https://platform.stratascratch.com/coding/2005-share-of-active-users?code_type=1

Output share of US users that are active. Active users are the ones with an "open" status in the table.

Table: fb_active_users
*/


SELECT active_users / total_users::float AS active_users_share
FROM (
        SELECT count(user_id) total_users,
            count(
                CASE
                    WHEN status = 'open' THEN 1
                    ELSE NULL
                END
            ) AS active_users
        FROM fb_active_users
        WHERE country = 'USA'
    ) subq