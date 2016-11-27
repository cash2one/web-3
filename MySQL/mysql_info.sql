/*
* @Date:   2016-11-10 15:35:13
* @Last Modified time: 2016-11-27 19:33:58
*/
-- MySQL常用命令
SELECT VERSION();           -- 显示mysql版本
SELECT CURRENT_DATE;        -- 显示当前日期
SELECT NOW();               -- 查询时间
SELECT USER();              -- 查询当前用户

SELECT VERSION(),CURRENT_DATE,NOW(),USER();


-- 库信息
SHOW DATABASES;                          -- 显示所有数据库
USE `crm`;                               -- 选择当前数据库
SELECT DATABASE();                       -- 查询当前数据库
-- CREATE DATABASE db_name;                 -- 创建数据库
-- DROP DATABASE [if exists] db;            -- 删除数据库，不提醒
-- shell> mysqladmin drop database db_name，删除数据库，有提示


-- 表信息
SHOW TABLES;                             -- 显示所有表
SHOW CREATE TABLE `order_toufang`;       -- 显示建表sql


SHOW COLUMNS FROM `order_toufang`;       -- 描述表————显示所有的列属性
DESCRIBE `order_toufang`;
DESC `order_toufang`;