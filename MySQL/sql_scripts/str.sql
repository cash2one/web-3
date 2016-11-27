/*
* @Date:   2016-10-20 17:30:30
* @Last Modified time: 2016-10-20 17:41:44
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