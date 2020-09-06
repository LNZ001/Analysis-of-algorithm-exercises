--CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
--BEGIN
--  SET n = N-1;
--  RETURN (
--  SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT n,1
--  );
--END

create function getNthHighestSalary (N int) returns int
begin
    return(
        select distinct Salary
        from (
            select Salary, @r:=IF(@p=Salary, @r, @r+1) as rnk, @p:=Salary -- 这两句是if前后检查的常见写法
            from Employee,
            (select @r:=0, @p:=NULL) init -- 这句在from后面，跟着的初始化是关键.
            order by Salary desc) tmp
        where rnk = N
        )
    );
end;


select distinct Salary as
from (
    select Salary, @r:=IF(@p=Salary, @r, @r+1) as rnk, @p:=Salary
    from Employee,
    (select @r:=0, @p:=NULL) init
    order by Salary desc
) tmp
where rnk = N;
