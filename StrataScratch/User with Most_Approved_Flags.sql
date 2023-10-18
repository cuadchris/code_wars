/*
https://platform.stratascratch.com/coding/2104-user-with-most-approved-flags?code_type=1

Which user flagged the most distinct videos that ended up approved by YouTube? Output, in one column, their full
name or names in case of a tie. In the user's full name, include a space between the first and the last name.

Tables: user_flags, flag_review
*/

select full_name
from (
        select concat(user_firstname, ' ', user_lastname) as full_name,
            rank() over(
                order by count(
                        distinct case
                            when reviewed_outcome = 'APPROVED' then video_id
                        end
                    ) desc
            ) as rnk
        from user_flags uf
            join flag_review fr on fr.flag_id = uf.flag_id
        group by full_name
    ) sq
where rnk = 1