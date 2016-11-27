/*
* @Date:   2016-09-26 15:17:39
* @Last Modified time: 2016-10-20 17:36:12
*/

-- 执行sql脚本，可以有2种方法:
-- shell>mysql -h localhost -u root -p123456 < $path\***.sql (注意路径不用加引号)
-- mysql>source $path\***.sql (注意路径不用加引号) 或者 \. $path\***.sql (注意路径不用加引号)

USE `crm`;


-- CASE语句
select
    grd.id,
    grd.accendant_id,
    grd.rent_type,
    CASE grd.rent_type
        WHEN 1 THEN '基础积分'
        WHEN 2 THEN '业绩转化积分'
        WHEN 3 THEN '奖励积分'
        WHEN 4 THEN '惩罚积分'
    ELSE '' END AS rent_type_str
from gw_rent_detail grd;


UPDATE `export_column_config` ecc
    SET ecc.`column_order`=
        CASE ecc.`column_order`
            WHEN 94.00 THEN 5.00
            WHEN 95.00 THEN 6.00
            WHEN 96.00 THEN 7.00
            WHEN 97.00 THEN 8.00
            WHEN 98.00 THEN 9.00
            WHEN 1.00 THEN 1.00
            WHEN 2.00 THEN ecc.`column_order`+8
            ELSE ecc.`column_order`+7 --  (4.00,93.00)
        END
WHERE ecc.`export_config_id`=(select ec.`Id` from `export_config` ec where ec.`report_name`='分佣表');

UPDATE `export_column_config` ecc
    SET ecc.`column_order`=ecc.`column_order`+1
WHERE ecc.`export_config_id`=(select ec.`Id` from `export_config` ec where ec.`report_name`='分佣表')
AND ecc.`column_order`>18;