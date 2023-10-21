/*
https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=1

Given a table of purchases by date, calculate the month-over-month percentage change in revenue. The output
should include the year-month date (YYYY-MM) and percentage change, rounded to the 2nd decimal point, and sorted
from the beginning of the year to the end of the year.
The percentage change column will be populated from the 2nd month forward and can be calculated as
((this month's revenue - last month's revenue) / last month's revenue)*100.

Table: sf_transactions
*/

with month_and_revenue as
(select
    to_char(created_at::date, 'YYYY-MM') AS year_month,
    sum(value) as revenue
from sf_transactions
group by year_month)

select
    year_month,
    round(((revenue - lag(revenue) over(order by year_month)) /
    lag(revenue) over(order by year_month)) * 100, 2) as revenue_diff_pct
from month_and_revenue