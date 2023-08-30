-- https://www.codewars.com/kata/64de2c3a529cadf9db8c5f33/sql

-- DESCRIPTION:

-- Write a query to produce a result set that lists an array of student names (ordered by their student_id in 
-- ascending order) for each subject where these students achieved the highest mark for that subject. Your result 
-- should also include the subject name and the highest mark achieved.

-- Table Schema:

-- students:
-- student_id (integer) - Unique identifier for each student.
-- student_name (varchar) - Name of the student.
-- details (varchar) - Additional details related to the student (for this challenge, it may have a static value 
-- like 'X').

-- subjects:
-- subject_id  (varchar) - Unique identifier for each subject (e.g., 'M' for Math).
-- subject_name (varchar) - Name of the subject (e.g., 'Math', 'English').

-- marks:
-- student_id (integer) - Identifier linking to the students table.
-- subject_id (varchar) - Identifier linking to the subjects table.
-- mark_rate (integer) - The mark or score the student has received for the subject.
-- Resultant Dataset Columns:

-- student_names (varchar[]) - Array of student names who scored the top mark for a subject, ordered by their 
-- student ID in ascending order.
-- subject_name (varchar) - Name of the subject.
-- mark_rate (integer) - The highest mark achieved in the subject.
-- The result set should be ordered by the subject_id in ascending order.

-- GLHF!​

-- Desired Output
-- ​The desired output should look like this:​

-- student_names	subject_name	mark_rate
-- {Paul,Lukas}	English	100
-- {George}	History	98
-- {John}	Math	95

SELECT
    ARRAY_AGG(s.student_name ORDER BY s.student_id) AS student_names,
    sub.subject_name,
    m.mark_rate
FROM
    subjects sub
JOIN (
    SELECT
        subject_id,
        MAX(mark_rate) AS mark_rate
    FROM
        marks
    GROUP BY
        subject_id
) m ON sub.subject_id = m.subject_id
JOIN (
    SELECT
        s.student_id,
        s.student_name,
        m.subject_id,
        m.mark_rate
    FROM
        students s
    JOIN
        marks m ON s.student_id = m.student_id
) h ON sub.subject_id = h.subject_id AND m.mark_rate = h.mark_rate
JOIN students s ON h.student_id = s.student_id
GROUP BY
    sub.subject_name,
    m.mark_rate,
    sub.subject_id
ORDER BY
    sub.subject_id;