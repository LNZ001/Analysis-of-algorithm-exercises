-- 找出最近一周每天每个商家的订单数
--drop table goods;
create table if not exists goods(id INT, store_id INT, order_time datetime, info INT);
truncate table goods;
insert into goods(id, store_id, order_time, info) values ('1', '1', '2018-06-02 15:10:28', '34');
insert into goods(id, store_id, order_time, info) values ('2', '1', '2018-06-01 15:11:28', '34');
insert into goods(id, store_id, order_time, info) values ('3', '3', '2018-06-02 15:12:28', '34');
insert into goods(id, store_id, order_time, info) values ('4', '2', '2018-05-28 15:13:28', '34');
insert into goods(id, store_id, order_time, info) values ('5', '2', '2018-06-03 15:14:28', '34');
insert into goods(id, store_id, order_time, info) values ('6', '1', '2018-06-02 15:15:28', '34');
insert into goods(id, store_id, order_time, info) values ('7', '1', '2018-05-02 15:15:28', '30');



select date(order_time) day, store_id, count(*)
from goods
where DATEDIFF(CURRENT_DATE, date(order_time)) <= 7
group by store_id, date(order_time)
order by day desc;
