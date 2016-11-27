/*
* @Date:   2016-11-23 09:15:57
* @Last Modified time: 2016-11-23 09:17:16
*/
SELECT
    c.`order_price_begin`,
    c.`order_area_begin`,
    (c.`order_price_begin`*c.`order_area_begin`*30) AS total_begin,
    c.`order_price_month_begin`,
    c.`order_price_end`,
    c.`order_area_end`,
    (c.`order_price_end`*c.`order_area_end`*30) AS total_end,
    c.`order_price_month_end`
FROM `customer` c
WHERE c.`order_price_month_end` !=c.`order_price_end`*c.`order_area_end`*30
OR c.`order_price_month_begin`  !=c.`order_price_begin`*c.`order_area_begin`*30;