/*
Find the average total compensation based on employee titles and gender. Total compensation is calculated by
adding both the salary and bonus of each employee. However, not every employee receives a bonus so disregard
employees without bonuses in your calculation. Employee can receive more than one bonus.
Output the employee title, gender (i.e., sex), along with the average total compensation.


Tables: sf_employee:

-------------------------------------------------------------------------------------------------------------------
| Id | First_name | Last_name | Age | Sex | Employee_title | Department | Salary | Target |        Email          |
-------------------------------------------------------------------------------------------------------------------
|  5 |     Max     |  George   | 26  |  M  |      Sales      |   Sales    | 1300  |  200   | Max@company.com      |
| 13 |    Katty    |   Bond    | 56  |  F  |     Manager     | Management |150000 |   0   | Katty@company.com     |
| 11 |   Richerd   |   Gear    | 57  |  M  |     Manager     | Management |250000 |   0   | Richerd@company.com   |
| 10 |  Jennifer   |   Dion    | 34  |  F  |      Sales      |   Sales    | 1000  |  200   | Jennifer@company.com |
| 19 |   George    |   Joe     | 50  |  M  |     Manager     | Management |100000 |   0   | George@company.com    |
| 18 |   Laila     |   Mark    | 26  |  F  |      Sales      |   Sales    | 1000  |  200   | Laila@company.com    |
| 20 |   Sarrah    |   Bicky   | 31  |  F  | Senior Sales    |   Sales    | 2000  |  200   | Sarrah@company.com   |
| 21 |   Suzan     |    Lee    | 34  |  F  |      Sales      |   Sales    | 1300  |  200   | Suzan@company.com    |
| 22 |   Mandy     |   John    | 31  |  F  |      Sales      |   Sales    | 1300  |  200   | Mandy@company.com    |
| 23 |  Britney    |   Berry   | 45  |  F  |      Sales      |   Sales    | 1200  |  200   | Britney@company.com  |
| 25 |    Jack     |   Mick    | 29  |  M  |      Sales      |   Sales    | 1300  |  200   | Jack@company.com     |
| 26 |     Ben     |   Ten     | 43  |  M  |      Sales      |   Sales    | 1300  |  150   | Ben@company.com      |
| 27 |     Tom     |  Fridy    | 32  |  M  |      Sales      |   Sales    | 1200  |  200   | Tom@company.com      |
| 29 |  Antoney    |   Adam    | 34  |  M  |      Sales      |   Sales    |        |        | Antoney@company.com |
-------------------------------------------------------------------------------------------------------------------


sf_bonus:

---------------------------------
| Worker_ref_id |   Bonus       |
---------------------------------
|       1       |     5000      |
|       2       |     3000      |
|       3       |     4000      |
|       1       |     4500      |
|       2       |     3500      |
|      14       |     1200      |
|      17       |     2500      |
|      30       |      500      |
---------------------------------
*/

SELECT e.employee_title,
       e.sex,
       AVG(e.salary + b.ttl_bonus) AS avg_compensation
FROM sf_employee e
JOIN
  (SELECT worker_ref_id,
          SUM(bonus) AS ttl_bonus
   FROM sf_bonus
   GROUP BY worker_ref_id) b ON e.id = b.worker_ref_id
GROUP BY employee_title,
         sex