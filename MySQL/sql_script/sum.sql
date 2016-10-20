/*
* @Date:   2016-10-20 17:35:55
* @Last Modified time: 2016-10-20 17:36:42
*/
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