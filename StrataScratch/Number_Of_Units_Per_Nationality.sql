/*
https://platform.stratascratch.com/coding/10156-number-of-units-per-nationality?code_type=1

Find the number of apartments per nationality that are owned by people under 30 years old.

Output the nationality along with the number of apartments.

Sort records by the apartments count in descending order.

Tables: airbnb_hosts, airbnb_units
*/

select
    nationality,
    count(distinct unit_id) as apartment_count
from airbnb_hosts ah
join airbnb_units au on au.host_id = ah.host_id
where age < 30 and unit_type = 'Apartment'
group by nationality
order by apartment_count desc