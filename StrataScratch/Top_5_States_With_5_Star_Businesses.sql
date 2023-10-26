/*
https://platform.stratascratch.com/coding/10046-top-5-states-with-5-star-businesses?code_type=1

Find the top 5 states with the most 5 star businesses. Output the state name along with the number of 5-star
businesses and order records by the number of 5-star businesses in descending order. In case there are ties in
the number of businesses, return all the unique states. If two states have the same result, sort them in
alphabetical order.

Table: yelp_business
*/

with cte as (
    select
        state,
        count(case when stars = 5 then 1 end) as n_businesses
    from yelp_business
    group by state
)

select
    state,
    n_businesses
from (
    select
        state,
        n_businesses,
        rank() over(order by n_businesses desc) as rnk
    from cte
) sq
where rnk <= 5
order by n_businesses desc, state