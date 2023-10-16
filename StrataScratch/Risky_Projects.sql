/*
https://platform.stratascratch.com/coding/10304-risky-projects?code_type=1

Identify projects that are at risk for going overbudget. A project is considered to be overbudget if the cost
of all employees assigned to the project is greater than the budget of the project.

You'll need to prorate the cost of the employees to the duration of the project. For example, if the budget for
a project that takes half a year to complete is $10K, then the total half-year salary of all employees assigned
to the project should not exceed $10K. Salary is defined on a yearly basis, so be careful how to calculate
salaries for the projects that last less or more than one year.

Output a list of projects that are overbudget with their project name, project budget, and prorated total
employee expense (rounded to the next dollar amount).


HINT: to make it simpler, consider that all years have 365 days. You don't need to think about the leap years.

Tables:

linkedin_projects:

| id  | title    | budget | start_date | end_date   |
|-----|----------|--------|------------|------------|
| 1   | Project1 | 29498  | 2018-08-31 | 2019-03-13 |
| 2   | Project2 | 32487  | 2018-01-27 | 2018-12-13 |
| 3   | Project3 | 43909  | 2019-11-05 | 2019-12-09 |
| 4   | Project4 | 15776  | 2018-06-28 | 2018-11-20 |
| 5   | Project5 | 36268  | 2019-03-13 | 2020-01-02 |
| 6   | Project6 | 41611  | 2018-09-18 | 2019-08-28 |
| 7   | Project7 | 34003  | 2020-05-28 | 2020-10-01 |
| 8   | Project8 | 49284  | 2019-12-18 | 2020-04-18 |
| 9   | Project9 | 32341  | 2018-05-24 | 2019-05-11 |
| 10  | Project10 | 47587 | 2018-06-24 | 2018-11-19 |

linkedin_emp_projects:

| emp_id | project_id |
|--------|------------|
| 10592  | 1          |
| 10593  | 2          |
| 10594  | 3          |
| 10595  | 4          |
| 10596  | 5          |
| 10597  | 6          |
| 10598  | 7          |
| 10599  | 8          |
| 10600  | 9          |
| 10601  | 10         |

linkedin_employees:

| emp_id | first_name | last_name | salary |
|--------|------------|-----------|--------|
| 10592  | Jennifer   | Roberts   | 20204  |
| 10593  | Haley      | Ho        | 33154  |
| 10594  | Eric       | Mccarthy  | 32360  |
| 10595  | Gina       | Martinez  | 46388  |
| 10596  | Jason      | Fields    | 12348  |
| 10597  | Joseph     | Hernandez | 47183  |
| 10598  | Catherine  | McCarthy  | 37423  |
| 10599  | Kelsey     | Miles     | 34488  |
| 10600  | Scott      | Lopez     | 24444  |
| 10601  | Gina       | Miller    | 36866  |
| 10602  | Nicole     | Jenkins   | 14327  |
| 10603  | Christopher| Gordon   | 41458   |
| 10604  | Jonathan   | Williams  | 16778  |
*/

with duration as (
    select id,
        title,
        budget,
        (end_date - start_date) as days
    from linkedin_projects
)
select title,
    budget,
    prorated_employee_expense
from (
        select d.id,
            title,
            budget,
            days,
            ceil(sum(salary) / 365 * days) as prorated_employee_expense
        from duration d
            join linkedin_emp_projects lep on lep.project_id = d.id
            join linkedin_employees le on le.id = lep.emp_id
        group by 1, 2, 3, 4
    ) sq
where prorated_employee_expense > budget