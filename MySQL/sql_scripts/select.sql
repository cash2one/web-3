/*
* @Date:   2016-11-09 15:21:29
* @Last Modified time: 2016-11-09 15:24:10
*/

-- 左联查询以左边表为主，右联查询以右边表为主，表关系用ON建立
-- 全联结查询，表名用逗号割开，表关系在where中建立
SELECT bc.`business_circle_id`
FROM `business_circle` bc,`district` d
WHERE bc.`district_id`=d.`district_id`
AND bc.`business_circle_name`='世博/前滩'
AND d.`district_name`='浦东';
