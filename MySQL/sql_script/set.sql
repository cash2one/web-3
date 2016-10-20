/*
* @Date:   2016-09-12 13:26:23
* @Last Modified time: 2016-09-12 13:30:40
*/

-- mysql中变量不用事前申明，在用的时候直接用“@变量名”使用就可以了。
-- set @num=1; 或 set @num:=1; //这里要使用变量来保存数据，直接使用@num变量
-- select @num:=1; 或 select @num:=字段名 from 表名 where ...
-- 使用set时可以用“=”或“：=”，但是使用select时必须用“：=赋值”

SELECT @num:=company FROM `customer`;