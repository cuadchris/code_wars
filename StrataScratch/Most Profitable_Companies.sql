/*
Find the 3 most profitable companies in the entire world.
Output the result along with the corresponding company name.
Sort the result based on profits in descending order.

Table: forbes_global_2010_2014
*/

SELECT company,
       profit
FROM
  (SELECT *,
          rank() OVER (
                       ORDER BY profit DESC) as rank
   FROM
     (SELECT company,
             sum(profits) AS profit
      FROM forbes_global_2010_2014
      GROUP BY company) sq) sq2
WHERE rank <=3

-- Could also do this for this particular table.

select
    company,
    profits
from forbes_global_2010_2014
order by 2 desc
limit 3