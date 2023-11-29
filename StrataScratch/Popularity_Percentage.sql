/*
Find the popularity percentage for each user on Meta/Facebook. The popularity percentage is defined as the
total number of friends the user has divided by the total number of users on the platform, then converted into
a percentage by multiplying by 100.

Output each user along with their popularity percentage. Order records in ascending order by user id.
The 'user1' and 'user2' column are pairs of friends.

Table: facebook_friends
*/

WITH cte AS (
    SELECT user1,
        user2
    FROM facebook_friends
    UNION
    SELECT user2 AS user1,
        user1 AS user2
    FROM facebook_friends
)
SELECT user1,
    count(*)::float / (
        SELECT count(DISTINCT user1)
        FROM cte
    ) * 100 AS popularity_percent
FROM cte
GROUP BY 1
ORDER BY 1