######SELECT

|               语句              |             含义             |
|---------------------------------|------------------------------|
| *                               | 查询表中所有                 |
| column1,column2,...             | 查询表中某（几）列           |
| column1 [AS] name1,...          | 查询时定义别名               |
| column1??column2 AS info        | “或”运算，全假则假，否则连接 |
| column1??' 字符 '??... AS info  | “或”运算，连接字符           |
| CONCAT(column1,':',column2,...) | 联合字符或者多个列           |

SELECT中加上DISTINCT去除重复字段

######[WHERE]
|               语句              |              含义             |
|---------------------------------|-------------------------------|
| columnx=[>、<、>=、<=]valux     |                               |
| columnx BETWEEN valu1 AND valu2 | 限制数值（字符串）范围        |
| columnx IN (valu1,valu2,...)    | 限制条件查询                  |
| columnx LIKE '_s%'              | 正则匹配查询（第二个字母是s） |
| columnx IS NULL                 | 利用null值进行检索            |

*WHERE语句之间以`AND、OR、NOT`连接，优先级：AND>OR*

######FROM tb
|           参数           |            含义            |
|--------------------------|----------------------------|
| [name]                   | 给表指定别名               |
| [GROUP BY column1[,...]] | 分组                       |
| [ORDER BY *** DESC,...]  | 排序                       |
| [LIMIT [num1,]num2]      | 返回num2条（从第num1开始） |

>当你确认查询结果只有一条数据时（如核对用户名密码），可以加上LIMIT 1的限制条件，当系统查询到一条数据后即停止搜索而不会继续查找下一条记录，这样可有效提高查询效率。

######;

*子查询相当于左联查一个*


#####<>————!=
<>在任何SQL中都起作用，但是!=在某些软件中是语法错误，不兼容

#####不包含
select * from tt where 字段 not like '%张%'  and 字段 not like '%王%' and 字段 not like '%李%'