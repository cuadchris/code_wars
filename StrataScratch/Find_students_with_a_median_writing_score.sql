/*
https://platform.stratascratch.com/coding/9610-find-students-with-a-median-writing-score?code_type=1

Output ids of students with a median score from the writing SAT.

Table: sat_scores

---------------------------------------------------------------------------------------------------------------------
|   School      |   Teacher     | Student_id | Sat_writing | Sat_verbal | Sat_math | Hrs_studied | Id | Average_sat |
---------------------------------------------------------------------------------------------------------------------
| Washington HS  | Frederickson  |     1      |     583      |    307     |   528    |     190     |  1 |     583   |
| Washington HS  | Frederickson  |     2      |     401      |    791     |   248    |     149     |  2 |     401   |
| Washington HS  | Frederickson  |     3      |     523      |    445     |   756    |     166     |  3 |     523   |
| Washington HS  | Frederickson  |     4      |     306      |    269     |   327    |     137     |  4 |     306   |
| Washington HS  | Frederickson  |     5      |     300      |    539     |   743    |     115     |  5 |     300   |
| Washington HS  | Frederickson  |     6      |     213      |    500     |   771    |     173     |  6 |     213   |
| Washington HS  | Frederickson  |     7      |     548      |    683     |   740    |      47     |  7 |     548   |
| Washington HS  | Frederickson  |     8      |     314      |    503     |   341    |     174     |  8 |     314   |
| Washington HS  | Frederickson  |     9      |     401      |    630     |   666    |     111     |  9 |     401   |
| Washington HS  | Frederickson  |     10     |     532      |    683     |   316    |     134     | 10 |     532   |
| Washington HS  | Frederickson  |     11     |     654      |    422     |   350    |     118     | 11 |     654   |
| Washington HS  | Frederickson  |     12     |     642      |    287     |   282    |             | 12 |     642   |
*/

select student_id
from sat_scores
where sat_writing = (
        select percentile_cont(0.5) within group (
                order by sat_writing
            ) as writing_percentile
        from sat_scores
    )

-- This is an easier way of getting the median.