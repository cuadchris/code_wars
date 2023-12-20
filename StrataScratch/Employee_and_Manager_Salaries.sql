/*
https://platform.stratascratch.com/coding/9894-employee-and-manager-salaries?code_type=1

Find employees who are earning more than their managers. Output the employee's first name along with the
corresponding salary.

Table: employee
*/

SELECT
        a.first_name AS employee_name, 
        a.salary AS employee_salary
FROM employee a
JOIN employee b ON  a.manager_id = b.id
WHERE a.salary > b.salary