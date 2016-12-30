select
    *
from (
    select
        h.id,
        o.name,
        o.circle_name,
        o.city_id,
        h.house_area,
        concat(h.price, "（元/平/天）") as price,
        concat(h.month_price, "（元/月）") as month_price,
        h.deliver_standard, h.floor_no,
        case when h.house_area >= 8.0 then 1 else 0 end as houseareabeginquanzhong,
        case when h.house_area <= 10.0 then 1 else 0 end as houseareaendquanzhong,
        case when h.price >= 0.0 then 1 else 0 end as pricebeginquanzhong,
        case when h.price <= 2.0 then 1 else 0 end as priceendquanzhong,
        case when h.month_price >= 0.0 then 1 else 0 end as monthpricebeginquanzhong,
        case when h.month_price <= 600.0 then 1 else 0 end as monthpriceendquanzhong,
        case h.canregister
            when 0 then '无'
            when 1 then '是'
            when 2 then '否'
            else ''
        end as canregisterstr,
        case h.howpay
            when 0 then '无'
            when 1 then '押一付一'
            when 2 then '押一付三'
            when 3 then '押一付六'
            when 4 then '押二付三'
            when 5 then '押二付六'
            else ''
        end as howpaystr
    from house h join office o on h.office_id=o.id
    where h.`invalid_type`=0
        and h.house_area > 6.4
        and h.house_area < 12.0
        and h.price < 2.4
        and h.month_price < 720.0
    order by houseareabeginquanzhong+houseareaendquanzhong+pricebeginquanzhong+priceendquanzhong+monthpricebeginquanzhong+monthpriceendquanzhong desc
    )
as house limit 0,20