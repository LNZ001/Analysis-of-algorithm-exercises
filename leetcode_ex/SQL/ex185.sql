Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, DepartmentId int);
Create table If Not Exists Department (Id int, Name varchar(255));
Truncate table Employee;
insert into Employee (Id, Name, Salary, DepartmentId) values ('1', 'Joe', '85000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('2', 'Henry', '80000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('3', 'Sam', '60000', '2');
insert into Employee (Id, Name, Salary, DepartmentId) values ('4', 'Max', '90000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('5', 'Janet', '69000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('6', 'Randy', '85000', '1');
insert into Employee (Id, Name, Salary, DepartmentId) values ('7', 'Will', '70000', '1');
Truncate table Department;
insert into Department (Id, Name) values ('1', 'IT');
insert into Department (Id, Name) values ('2', 'Sales');

-- 每个都找一次比他高出的不重数量。
select d.Name as `Department` ,e.Name as `Employee`, e.Salary
from Employee e JOIN Department d ON d.Id = e.DepartmentId
where 3 >
(
	select count(distinct e2.Salary)
	from Employee e2
	where e2.Salary > e.Salary AND e2.DepartmentId = e.DepartmentId
)

-- 先计算出每个部门第三高的薪资，没有就
-- 分组 top n 问题.
select d.Name as Department, t.Employee, t.Salary
from
(select Name as Employee, Salary, DepartmentId,
@rank:=IF(@preDepartmentId = DepartmentId, IF(@preSalary=Salary, @rank+0, @rank+1), 1) SalaryRank,
@preDepartmentId:=DepartmentId,
@preSalary:=Salary
from Employee, (select @preDepartmentId := null, @preSalary := null, @rank:=0) as init
order by DepartmentId, Salary DESC) t join Department d on t.DepartmentId = d.Id
where t.SalaryRank <= 3
