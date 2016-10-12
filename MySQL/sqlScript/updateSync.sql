/*
* @Date:   2016-09-07 10:26:01
* @Last Modified time: 2016-09-07 11:20:03
*/
USE crm;

--
UPDATE
    `pb_house` ph

SET
    create_id         =(SELECT create_id FROM `house` h WHERE h.Id=ph.house_id),
    create_name       =(SELECT create_name FROM `house` h WHERE h.Id=ph.house_id),
    investigator_id   =(SELECT investigator_accendant_id FROM `house` h WHERE h.Id=ph.house_id),
    investigator_name =(SELECT investigator_accendant_name FROM `house` h WHERE h.Id=ph.house_id);

-- 每set一次都有select整个house，效率低下



UPDATE pb_house p
-- inner join...on，在表间关联来做更新和删除操作，非常有用.
INNER JOIN
(
    SELECT
        h.id,
        h.`investigator`,
        h.`investigator_name`,
        h.`create_id`,
        h.`create_name`
    FROM house h
    WHERE h.`Id`IN
    (
    SELECT p.`house_id` FROM pb_house p
    )
)
h

ON p.`house_id` = h.id

SET
    p.create_id         = h.create_id,
    p.create_name       = h.create_name,
    p.investigator_id   = h.investigator_accendant_id,
    p.investigator_name = h.investigator_accendant_name;
