/*
https://platform.stratascratch.com/coding/10087-find-all-posts-which-were-reacted-to-with-a-heart?code_type=1

Find all posts which were reacted to with a heart. For such posts output all columns from facebook_posts table.

Tables: facebook_reactions, facebook_posts
*/

SELECT distinct p.*
FROM facebook_posts p
    JOIN facebook_reactions r ON p.post_id = r.post_id
    AND r.reaction = 'heart'