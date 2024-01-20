/*
Find libraries who haven't provided the email address in circulation year 2016 but their notice preference
definition is set to email.

Output the library code.

Table: library_usage
*/

SELECT DISTINCT home_library_code
FROM library_usage
WHERE notice_preference_definition = 'email'
    AND provided_email_address is FALSE
    AND circulation_active_year = 2016