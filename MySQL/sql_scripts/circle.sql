/*
* @Date:   2016-11-09 12:56:06
* @Last Modified time: 2016-11-09 16:16:58
*/
use `crm`;

update `business_circle`
    set `business_circle_name` ='其他'
    where `business_circle_id` =261;

update `business_circle`
    set `business_circle_name` ='大柏树'
    where `business_circle_id` =262;

update `business_circle`
    set `business_circle_name` ='其他'
    where `business_circle_id` =272;

update `business_circle`
    set `business_circle_name` ='其他'
    where `business_circle_id` =279;

update `business_circle`
    set `business_circle_name` ='大虹桥'
    where `business_circle_id` =282;

update `business_circle`
    set `business_circle_name` ='世博/前滩'
    where `business_circle_id` =297;

update `business_circle`
    set `business_circle_name` ='其他'
    where `business_circle_id` =301;

update `business_circle`
    set `business_circle_name` ='其他'
    where `business_circle_id` =305;

update `business_circle`
    set `business_circle_name` ='长风商务区'
    where `business_circle_id` =308;

update `business_circle`
    set `business_circle_name` ='金沙江路'
    where `business_circle_id` =310;

update `business_circle`
    set `business_circle_name` ='徐汇滨江'
    where `business_circle_id` =318;

update `business_circle`
    set `business_circle_name` ='其他'
    where `business_circle_id` =320;

update `business_circle`
    set `business_circle_name` ='新江湾'
    where `business_circle_id` =325;

update `business_circle`
    set `business_circle_name` ='不夜城/火车站'
    where `business_circle_id` =327;

update `business_circle`
    set `business_circle_name` ='大虹桥'
    where `business_circle_id` =45;

update `business_circle`
    set `business_circle_name` ='虹桥开发区'
    where `business_circle_id` =332;

-- 验证
-- select
-- *
-- from `business_circle` bc
-- where bc.`business_circle_id` in (
--     61, 262, 272, 279, 282, 297, 301, 305, 308, 310, 318, 320, 325, 327, 45, 332
--     )


delete from `business_circle` where `business_circle_id` =255;
delete from `business_circle` where `business_circle_id` =14;
delete from `business_circle` where `business_circle_id` =265;
delete from `business_circle` where `business_circle_id` =275;
delete from `business_circle` where `business_circle_id` =280;
delete from `business_circle` where `business_circle_id` =333;
delete from `business_circle` where `business_circle_id` =281;
delete from `business_circle` where `business_circle_id` =285;
delete from `business_circle` where `business_circle_id` =287;
delete from `business_circle` where `business_circle_id` =289;
delete from `business_circle` where `business_circle_id` =290;
delete from `business_circle` where `business_circle_id` =291;
delete from `business_circle` where `business_circle_id` =292;
delete from `business_circle` where `business_circle_id` =294;
delete from `business_circle` where `business_circle_id` =295;
delete from `business_circle` where `business_circle_id` =296;
delete from `business_circle` where `business_circle_id` =302;
delete from `business_circle` where `business_circle_id` =304;
delete from `business_circle` where `business_circle_id` =306;
delete from `business_circle` where `business_circle_id` =307;
delete from `business_circle` where `business_circle_id` =309;
delete from `business_circle` where `business_circle_id` =322;
delete from `business_circle` where `business_circle_id` =46;

-- 验证
-- select
-- *
-- from `business_circle` bc
-- where bc.`business_circle_id` in (
--     255, 14, 265, 275, 280, 333, 281, 285, 287, 289, 290, 291, 292, 294, 295, 296, 302, 304, 306, 307, 309, 322, 46
--     )

-- insert into `business_circle` set
--     `district_id`          = (select `district_id` from `district` d where d.`district_name`='静安区'),
--     `business_circle_name` = '北京西路';


insert into
    `business_circle`
    (
        `district_id`,
        `business_circle_name`
        )
    values
    (
        (select `district_id` from `district` d where d.`district_name` LIKE'静安%'),
        '北京西路'
        ),
    (
        (select `district_id` from `district` d where d.`district_name` LIKE'卢湾%'),
        '其他'
        ),
    (
        (select `district_id` from `district` d where d.`district_name` LIKE'卢湾%'),
        '肇嘉浜路'
        ),
    (
        (select `district_id` from `district` d where d.`district_name` LIKE'闸北%'),
        '其他'
        ),
    (
        (select `district_id` from `district` d where d.`district_name` LIKE'闸北%'),
        '市北工业园'
        ),
    (
        (select `district_id` from `district` d where d.`district_name` LIKE'闸北%'),
        '中山北路'
        ),
    (
        (select `district_id` from `district` d where d.`district_name` LIKE'长宁%'),
        '临空园区'
        ),
    (
        (select `district_id` from `district` d where d.`district_name` LIKE'长宁%'),
        '延安西路'
        );

-- 验证
-- SELECT
-- d.`district_id`,
-- bc.*
-- FROM `business_circle` bc
-- LEFT JOIN `district` d
-- ON bc.`district_id`=d.`district_id`
-- ORDER BY bc.`business_circle_id` DESC