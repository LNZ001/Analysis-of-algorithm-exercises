
Create table If Not Exists Logs (Id int, Num int);
Truncate table Logs
insert into Logs (Id, Num) values ('1', '1')
insert into Logs (Id, Num) values ('2', '1')
insert into Logs (Id, Num) values ('3', '1')
insert into Logs (Id, Num) values ('4', '2')
insert into Logs (Id, Num) values ('5', '1')
insert into Logs (Id, Num) values ('6', '2')
insert into Logs (Id, Num) values ('7', '2')

-- 方法1
select distinct l1.Num as ConsecutiveNums
from Logs l1
join Logs l2
join Logs l3
where l1.Id = l2.Id-1
and l1.Id = l3.Id+1
and l1.Num = l2.Num
and l1.Num = l3.Num

-- 方法2
select distinct t.Num as ConsecutiveNums
from
(
select Id, Num, @n:=IF(@li=Id-1 and @ln=Num, @n+1, 1) n, @c:=IF(@n=3, 1, 0) c, @li:=Id li, @ln:=Num ln
from Logs, (select @li:=NULL, @ln:=NULL, @c:= 0, @n:=0) init
order by Id
) t
where t.c = 1