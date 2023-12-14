/*
https://platform.stratascratch.com/coding/9892-second-highest-salary?code_type=1

Find the second highest salary of employees.

Table: employee
*/

select
    salary
from 
    (select distinct
        salary,
        dense_rank() over(order by salary desc) as rnk
    from employee) sq
where rnk = 2