/*
For each video, find how many unique users flagged it. A unique user can be identified using the combination of
their first name and last name. Do not consider rows in which there is no flag ID.

Table: user_flags
*/

SELECT video_id,
    count(
        DISTINCT concat(
            COALESCE(user_firstname, ''),
            COALESCE(user_lastname, '')
        )
    ) num_unique_users
FROM user_flags AS uf
WHERE flag_id IS NOT NULL
GROUP BY video_id