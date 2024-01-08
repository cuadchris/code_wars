/*
Find the employee with the highest salary per department.
Output the department name, employee's first name along with the corresponding salary.

Table: employee
*/

SELECT department AS department,
    first_name AS employee_name,
    salary
FROM employee
WHERE (department, salary) IN (
        SELECT department,
            MAX(salary)
        FROM employee
        GROUP BY department
    );