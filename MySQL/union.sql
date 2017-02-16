/*
* @Date:   2017-02-16 15:20:48
* @Last Modified time: 2017-02-16 15:20:57
*/
    <select id="selectCustomerByUserIdListPage" resultMap="opencustomerMap" parameterType="com.uban.crm.domain.open.OpenCustomer">
        SELECT
        oc.id AS openCustomerId,
        oc.`customer_name`,
        oc.city_id,
        oc.city_name,
        oc.`district_id`,
        oc.`district_name`,
        oc.`circle_id`,
        oc.`circle_name`,
        oc.`order_area_begin`,
        oc.`order_area_end`,
        oc.`order_price_begin`,
        oc.`order_price_end`,
        '未接单' AS isAccept,
        oc.create_at
        FROM `open_customer_send` ocs
        LEFT JOIN `open_customer` oc ON ocs.`customer_id`=oc.`id`
        <trim prefix="where" prefixOverrides="and|or">
            <if test="vo.userId != null">
                and ocs.user_id = #{vo.userId}
            </if>
        </trim>
        UNION
        (
        select
        oc.id AS openCustomerId,
        oc.`customer_name`,
        oc.city_id,
        oc.city_name,
        oc.`district_id`,
        oc.`district_name`,
        oc.`circle_id`,
        oc.`circle_name`,
        oc.`order_area_begin`,
        oc.`order_area_end`,
        oc.`order_price_begin`,
        oc.`order_price_end`,
        ouc.tag,
        case ouc.`systemresource` when 0 then '接单' when 1 then '私客' else '' end AS isAccept,
        oc.create_at
        from `open_user_customer` ouc
        left join `open_customer` oc on ouc.`open_customer_id`=oc.`id`
        <trim prefix="where" prefixOverrides="and|or">
            <if test="vo.userId != null">
                and ouc.user_id = #{vo.userId}
            </if>
        </trim>
        order by oc.create_at DESC
        )
    </select>