Create table If Not Exists Scores (Id int, Score DECIMAL(3,2))
Truncate table Scores
insert into Scores (Id, Score) values ('1', '3.5')
insert into Scores (Id, Score) values ('2', '3.65')
insert into Scores (Id, Score) values ('3', '4.0')
insert into Scores (Id, Score) values ('4', '3.85')
insert into Scores (Id, Score) values ('5', '4.0')
insert into Scores (Id, Score) values ('6', '3.65')

select a.Score, a.Rank
from
(select Id, Score, @n:=IF(@p=Score, @n, @n+1) Rank, @p:=Score
from Scores, (select @n:=1, @p:=NULL) init
order by Score desc) as a