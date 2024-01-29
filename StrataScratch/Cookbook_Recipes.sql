/*
https://platform.stratascratch.com/coding/2089-cookbook-recipes?code_type=1

You are given the table with titles of recipes from a cookbook and their page numbers. You are asked to represent
how the recipes will be distributed in the book. Produce a table consisting of three columns: left_page_number,
left_title and right_title. The k-th row (counting from 0), should contain the number and the title of the page
with the number 2 x k in the first and second columns respectively, and the title of the page with the number
2 x k + 1 in the third column. Each page contains at most 1 recipe. If the page does not contain a recipe, the
appropriate cell should remain empty (NULL value). Page 0 (the internal side of the front cover) is guaranteed
to be empty.

Table: cookbook_titles
*/

WITH series AS (
    SELECT generate_series AS page_number
    FROM generate_series(
            0,
            (
                SELECT max(page_number)
                FROM cookbook_titles
            )
        )
),
cookbook_titles_v2 AS (
    SELECT s.page_number,
        c.title
    FROM series s
        LEFT JOIN cookbook_titles c ON s.page_number = c.page_number
)
SELECT (
        row_number() over(
            ORDER BY page_number / 2
        ) -1
    ) * 2 AS left_page_number,
    string_agg(
        CASE
            WHEN page_number % 2 = 0 THEN title
        END,
        ','
    ) AS left_title,
    string_agg(
        CASE
            WHEN page_number % 2 = 1 THEN title
        END,
        ','
    ) AS right_title
FROM cookbook_titles_v2
GROUP BY page_number / 2