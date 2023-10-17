/*
Find the top business categories based on the total number of reviews. Output the category along with the total
number of reviews. Order by total reviews in descending order.

Table: yelp_business
*/

SELECT
    category,
    sum(review_count) as review_cnt
FROM (SELECT
        unnest(string_to_array(categories, ';')) AS category,
        review_count
    FROM yelp_business) sq
GROUP BY category
ORDER BY review_cnt DESC

-- unnest() is powerful.