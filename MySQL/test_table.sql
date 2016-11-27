/*
* @Date:   2016-10-08 09:18:56
* @Last Modified time: 2016-11-10 18:28:00
*/
-- 创建表
-- IF NOT EXISTS————可选，创建时判断表是否存在
-- 自增长列必须是键
-- 复和主键————一列不能唯一区分一个表里的记录时，把多个列组合起来区分表记录的唯一性
-- 主键一定是唯一性索引，唯一性索引并不一定就是主键
CREATE TABLE IF NOT EXISTS tb1(
    col1 VARCHAR(100),                              -- 设定列
    col2 VARCHAR(20) NOT NULL DEFAULT '经理',       -- 设定默认值
    id INT NOT NULL,                                -- 设定非空
    -- primary key PK_positon (id),                    -- 设定主键
    primary key PK_depart_pos (col1,col2),          -- 设定复和主键
    -- id INT NOT NULL primary key,                    -- 设定非空主键
    -- id INT NOT NULL auto_increment primary key,     -- 设定非空自增长主键
    UNIQUE (col1,col2)                              -- 设定唯一值，限制一个或多个字段不准重复
);


-- 修改表结构
ALTER TABLE tb1 RENAME new_tb;                                       -- 重命名表
ALTER TABLE new_tb ADD col3 CHAR(10);                                -- 给表增加列
ALTER TABLE new_tb MODIFY col3 CHAR(10) NOT NULL;                    -- 修改表的列类型
ALTER TABLE new_tb CHANGE col1 col2 INT unsigned;                    -- 修改列名和属性
ALTER TABLE new_tb ALTER col3 SET DEFAULT '..';                      -- 修改列的默认值
ALTER TABLE new_tb ALTER col3 DROP DEFAULT;                          -- 删除表的列的默认值
ALTER TABLE new_tb DROP COLUMN col3;                                 -- 删除表的列
ALTER TABLE new_tb DROP PRIMARY KEY;                                 -- 删除表的主键
ALTER TABLE new_tb ADD PRIMARY KEY PK_depart_pos (col1,col2);        -- 增加主键


-- 删除表
DROP TABLE `new_tb`;


-- 创建临时表————连接MySQL期间存在
CREATE TEMPORARY TABLE tb2(
    SELECT * FROM tb1 WHERE 1<>1       -- 复制表结构
    -- SELECT * FROM tb1
);