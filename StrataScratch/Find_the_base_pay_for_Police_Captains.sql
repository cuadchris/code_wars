/*
https://platform.stratascratch.com/coding/9972-find-the-base-pay-for-police-captains?code_type=1

Find the base pay for Police Captains.
Output the employee name along with the corresponding base pay.

Table: sf_public_salaries
*/

SELECT employeename,
    basepay
FROM sf_public_salaries
WHERE jobtitle ILIKE '%CAPTAIN%POLICE%'
