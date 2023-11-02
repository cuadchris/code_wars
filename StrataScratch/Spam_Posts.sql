/*
https://platform.stratascratch.com/coding/10134-spam-posts?code_type=1

Calculate the percentage of spam posts in all viewed posts by day. A post is considered a spam if a string
"spam" is inside keywords of the post. Note that the facebook_posts table stores all posts posted by users.
The facebook_post_views table is an action table denoting if a user has viewed a post.

Tables:

facebook_posts:

+---------+--------+-------------------------------------------+-----------------------------+--------------------+
| post_id | poster | post_text                                  | post_keywords               | post_date         |
+---------+--------+-------------------------------------------+-----------------------------+--------------------+
| 0       | 2      | The Lakers game from last night was great. | [basketball, lakers, nba]  | 2019-01-01         |
| 1       | 1      | Lebron James is top class.                 | [basketball, lebron_james, nba] | 2019-01-02    |
| 2       | 2      | Asparagus tastes OK.                      | [asparagus, food]          | 2019-01-01          |
| 3       | 1      | Spaghetti is an Italian food.             | [spaghetti, food]          | 2019-01-02          |
| 4       | 3      | User 3 is not sharing interests           | [#spam#]                   | 2019-01-01          |
| 5       | 3      | User 3 posts SPAM content a lot           | [#spam#]                   | 2019-01-02          |
+---------+--------+-------------------------------------------+-----------------------------+--------------------+

facebook_post_views:

+---------+-----------+
| post_id | viewer_id |
+---------+-----------+
| 4       | 0         |
| 4       | 1         |
| 4       | 2         |
| 5       | 0         |
| 5       | 1         |
| 5       | 2         |
| 3       | 1         |
+---------+-----------+
*/

select
    post_date,
    count(case when post_keywords like '%spam%' then 1 end)::float /
    count(post_date)::float * 100 as spam_share
from facebook_posts fp
join facebook_post_views fpv on fpv.post_id = fp.post_id
group by post_date