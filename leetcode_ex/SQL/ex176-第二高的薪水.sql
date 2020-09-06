-- 排序找第二个
SELECT IFNULL((
SELECT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1,1
) as s, NULL) as SecondHighestSalary;


-- 比最大的小的第一个.
SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
WHERE
Salary <
(
SELECT DISTINCT max(Salary)
FROM Employee




);
