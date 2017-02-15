/*
* @Date:   2016-10-20 17:30:30
* @Last Modified time: 2017-02-15 11:01:22
*/
USE `crm`;
-- 2016 05 20 09 17 56
SELECT
    LEFT(o4.`StartDate`,4),
    SUBSTRING(o4.`StartDate`,5,2),
    SUBSTRING(o4.`StartDate`,7,2),
    SUBSTRING(o4.`StartDate`,9,2),
    SUBSTRING(o4.`StartDate`,11,2),
    RIGHT(o4.`StartDate`,2),
    FROM_UNIXTIME(o4.modify_at) AS modifyAtStr
FROM order_400calllog o4;

-- CONCAT(str1,str2,…)————返回连接参数产生的字符串
-- 如有任何一个参数为NULL，则返回 NULL
-- 一个数字参数被变换为等价的字符串形式

SELECT
    CONCAT(
        LEFT(o4.`StartDate`,4),
        "-",
        SUBSTRING(o4.`StartDate`,5,2),
        "-",
        SUBSTRING(o4.`StartDate`,7,2),
        " ",
        SUBSTRING(o4.`StartDate`,9,2),
        ":",
        SUBSTRING(o4.`StartDate`,11,2),
        ":",
        RIGHT(o4.`StartDate`,2)
        ) AS StartDate
FROM order_400calllog o4;

SELECT
    CASE startdate
    WHEN '' THEN ''
    ELSE CONCAT(
        LEFT(jc.`startdate`,4),
        "-",
        SUBSTRING(jc.`startdate`,5,2),
        "-",
        SUBSTRING(jc.`startdate`,7,2),
        " ",
        SUBSTRING(jc.`startdate`,9,2),
        ":",
        SUBSTRING(jc.`startdate`,11,2),
        ":",
        RIGHT(jc.`startdate`,2)
        )
    END AS startdate
FROM `jiya_connecting` jc;


-- 连接一列字符串
SELECT
    GROUP_CONCAT(oc.id) AS a
FROM `open_customer` oc
WHERE oc.`id` BETWEEN 100 AND 105