/*
https://platform.stratascratch.com/coding/10064-highest-energy-consumption?code_type=1

Meta/Facebook | Medium

Find the date with the highest total energy consumption from the Meta/Facebook data centers. Output the date
along with the total energy consumption across all data centers.

Tables:


fb_eu_energy:

---------------------------------
|    Date    |  Consumption   |
---------------------------------
| 2020-01-01 |      400       |
| 2020-01-02 |      350       |
| 2020-01-03 |      500       |
| 2020-01-04 |      500       |
| 2020-01-07 |      600       |
---------------------------------


fb_asia_energy:

---------------------------------
|    Date    |  Consumption   |
---------------------------------
| 2020-01-01 |      400       |
| 2020-01-02 |      400       |
| 2020-01-04 |      675       |
| 2020-01-05 |     1200       |
| 2020-01-06 |      750       |
| 2020-01-07 |      400       |
---------------------------------


fb_na_energy:

---------------------------------
|    Date    |  Consumption   |
---------------------------------
| 2020-01-01 |      250       |
| 2020-01-02 |      375       |
| 2020-01-03 |      600       |
| 2020-01-06 |      500       |
| 2020-01-07 |      250       |
---------------------------------
*/

with unions as (
    select *
    from fb_eu_energy
    union
    select *
    from fb_asia_energy
    union
    select *
    from fb_na_energy
)

select
    date,
    total_energy
from (
    select
        date,
        sum(consumption) as total_energy,
        rank() over(order by sum(consumption) desc) as rnk
    from unions
    group by date
) sq
where rnk = 1