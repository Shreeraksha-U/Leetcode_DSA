# Write your MySQL query statement below

with rankedscores as 

( select id, score, 
        dense_rank() over(order by score 
        desc) as rnk1

  from scores
  )
select score, rnk1 as "rank"
from rankedscores
order by score desc