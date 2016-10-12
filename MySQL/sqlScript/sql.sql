/*
* @Date:   2016-09-26 15:17:39
* @Last Modified time: 2016-10-11 17:50:57
*/

-- 执行sql脚本，可以有2种方法:
-- shell>mysql -h localhost -u root -p123456 < $path\***.sql (注意路径不用加引号)
-- mysql>source $path\***.sql (注意路径不用加引号) 或者 \. $path\***.sql (注意路径不用加引号)

USE `crm`;
-- SUM IF语句
select
    grd.id,
    grd.accendant_id,
    grd.accendant_deptname,
    grd.rent_type,
    FROM_UNIXTIME(grd.modify_at) AS modifyAtStr,
    grd.rent,
    SUM(IF(grd.rent_type=1, grd.rent, 0)) AS baseRent,
    SUM(IF(grd.rent_type=2, grd.rent, 0)) AS yejiRent,
    SUM(IF(grd.rent_type=3, grd.rent, 0)) AS jiangliRent,
    SUM(IF(grd.rent_type=4, grd.rent, 0)) AS chengfaRent,
    ABS(SUM(IF(grd.rent_type=5, grd.rent, 0))) AS xiaohaoRent,
    SUM(IF(rent_type=5,1,0)) AS kehuCount,  -- 统计rent_type为5的
    SUM(grd.rent) AS totalRent
from gw_rent_detail grd
WHERE grd.accendant_deptname != ""
GROUP BY grd.accendant_id;

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