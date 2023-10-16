/*
https://platform.stratascratch.com/coding/2099-election-results?code_type=1

The election is conducted in a city and everyone can vote for one or more candidates, or choose not to vote at
all. Each person has 1 vote so if they vote for multiple candidates, their vote gets equally split across these
candidates. For example, if a person votes for 2 candidates, these candidates receive an equivalent of 0.5 vote
each.
Find out who got the most votes and won the election. Output the name of the candidate or multiple names in
case of a tie. To avoid issues with a floating-point error you can round the number of votes received by a
candidate to 3 decimal places.

voting_results Table:

voter: varchar
candidate: varchar
*/

with voter_worth as
(select
    voter,
    count(case when candidate is not null then 1 end) as vote_count
from voting_results
group by voter),

candidate_rank as
(select
    vr.candidate,
    rank() over(order by sum(case when vote_count > 0 then round(1/vote_count) end) desc) as rnk
from voting_results vr
join voter_worth vw on vw.voter = vr.voter
group by vr.candidate)

select
    candidate
from candidate_rank
where rnk = 1