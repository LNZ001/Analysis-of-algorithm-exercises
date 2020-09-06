-- Result
-- studentId projectId score

-- 找出偏科学生
select *
from (
select *, sum(score), sum(IF(r.score <= t.avg_score, 1, NULL)) counts
from Result r join
(
select projectId, avg(score) avg_score
from Result
group by projectId) t on r.projectId = t.projectId
group by studentId
order by sum(score) desc
)
where counts >= 2
-- 大概清楚了， 没写完。