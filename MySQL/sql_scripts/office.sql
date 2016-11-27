/*
* @Date:   2016-11-09 14:32:45
* @Last Modified time: 2016-11-09 16:13:46
*/
use `crm`;

update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='世博/前滩'
        AND d.`district_name` LIKE'浦东%'
        ),
    o.`circle_name`='世博/前滩'
    WHERE o.`Id` IN (
        3589, 3946, 3964, 4166, 4175, 4176, 4195, 4320, 4338, 4457, 4489, 4547, 4567, 4578, 4580, 4637, 4682, 4721, 4897, 200372, 200772, 200853, 200921, 200938, 200966, 200977, 200978, 200979, 201001
        );

update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='其他'
        AND d.`district_name` LIKE'浦东%'
        ),
    o.`circle_name`='其他'
    WHERE o.`Id` IN (
        3574, 3614, 3635, 3673, 3750, 3754, 3815, 3819, 3828, 3912, 3914, 3915, 3973, 4032, 4040, 4041, 4045, 4149, 4154, 4164, 4188, 4200, 4231, 4235, 4251, 4342, 4345, 4346, 4350, 4354, 4368, 4373, 4389, 4412, 4511, 4514, 4515, 4520, 4536, 4556, 4574, 4576, 4618, 4680, 4718, 4753, 4754, 4796, 4805, 4811, 4832, 4846, 4848, 4852, 4857, 4870, 4876, 4886, 4899, 4900, 4973, 5016, 5026, 5066, 200367, 200406, 200485, 200486, 200554, 200659, 200667, 200787, 200799, 200814, 200911, 200917, 200931, 201030
        );


update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='大虹桥'
        AND d.`district_name` LIKE'闵行%'
        ),
    o.`circle_name`='大虹桥'
    WHERE o.`Id` IN (
        113, 3393, 3725, 3760, 3794, 3797, 3878, 3917, 3944, 3947, 3954, 3965, 3967, 3983, 4003, 4008, 4009, 4012, 4049, 4324, 4375, 4450, 4468, 4482, 4561, 4591, 4607, 4615, 4673, 4675, 4740, 4823, 4883, 4884, 4889, 4927, 4930, 5041, 200258, 200337, 200382, 200480, 200668, 200669, 200683, 200684, 200891, 200892, 200893, 200925, 200926, 200939, 200940
        );

update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='其他'
        AND d.`district_name` LIKE'闵行%'
        ),
    o.`circle_name`='其他'
    WHERE o.`Id` IN (
        3821, 3862, 4001, 4005, 4028, 4083, 4089, 4101, 4102, 4112, 4192, 4215, 4252, 4303, 4406, 4467, 4495, 4522, 4533, 4535, 4553, 4557, 4609, 4620, 4623, 4738, 4746, 4761, 4790, 4821, 4854, 4859, 4861, 4888, 4918, 4920, 4923, 4933, 200357, 200665, 200689, 200691, 200692, 200693, 200694, 200696, 200697, 200718, 200767, 200839, 200843, 201033
        );

update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='其他'
        AND d.`district_name` LIKE'静安%'
        ),
    o.`circle_name`='其他'
    WHERE o.`Id` IN (
        3378, 3380, 3505, 3506, 3507, 3508, 3509, 3510, 3511, 3512, 3513, 3514, 3515, 3516, 3517, 3518, 3519, 3520, 3521, 4438, 5144, 5145, 5146, 5148, 5169, 5170, 5176, 5177, 5180, 5191, 200573, 200909
        );


update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='虹桥开发区'
        AND d.`district_name` LIKE'长宁%'
        ),
    o.`circle_name`='虹桥开发区'
    WHERE o.`Id` IN (
        3642, 3672, 3676, 3736, 3833, 3837, 4010, 4084, 4161, 4299, 4477, 4704, 4799, 4828, 4902, 5182, 200178, 200179, 200180, 200181, 200182, 200183, 200191, 201043
        );


update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='徐汇滨江'
        AND d.`district_name` LIKE'徐汇%'
        ),
    o.`circle_name`='徐汇滨江'
    WHERE o.`Id` IN (
        3425, 3426, 3429, 3430, 3937, 4082, 4097, 4417, 4587, 4622, 4745, 5046, 200171, 200292, 200534, 200991
        );

update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='不夜城/火车站'
        AND d.`district_name` LIKE'闸北%'
        ),
    o.`circle_name`='不夜城/火车站'
    WHERE o.`Id` IN (
        80, 81, 87, 88, 91, 3201, 3202, 3203, 3204, 3205, 3609, 3644, 3749, 3777, 3786, 3848, 3850, 3884, 3897, 3925, 3928, 4017, 4120, 4129, 4139, 4144, 4165, 4226, 4241, 4247, 4265, 4329, 4352, 4363, 4403, 4432, 4433, 4435, 4436, 4455, 4479, 4481, 4519, 4552, 4661, 4674, 4730, 4757, 4772, 4801, 4824, 4827, 4837, 4840, 4847, 4849, 4851, 4947, 5044, 5054, 5063, 5091, 200152, 200347, 200410, 200411, 200412, 200413, 200414, 200415, 200416, 200417, 200418, 200419, 200420, 200421, 200422, 200423, 200424, 200426, 200427, 200428, 200429, 200430, 200431, 200432, 200433, 200449, 200518, 200519, 200520, 200521, 200522, 200571, 200777, 200838, 200870, 200986
        );


update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='大柏树'
        AND d.`district_name` LIKE'虹口%'
        ),
    o.`circle_name`='大柏树'
    WHERE o.`Id` IN (
        3826, 3879, 3961, 3985, 4128, 4325, 4409, 4466, 4616, 4739, 4809, 200187, 200359, 200436, 200441, 200444, 200852, 201027
        );

update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='长风商务区'
        AND d.`district_name` LIKE'普陀%'
        ),
    o.`circle_name`='长风商务区'
    WHERE o.`Id` IN (
        3650, 3746, 3762, 3801, 3831, 3840, 3918, 3976, 3990, 3995, 4185, 4219, 4440, 200207, 200311, 200383, 200500, 200561, 200574, 200575, 200576, 200577, 200578, 200579, 200589, 200590, 200607, 200608, 200675
        );

update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='金沙江路'
        AND d.`district_name` LIKE'普陀%'
        ),
    o.`circle_name`='金沙江路'
    WHERE o.`Id` IN (
        3813, 3845, 3849, 4002, 4392, 4509, 4566, 4581, 4596, 4633, 4878, 200540, 200547, 200582, 200615, 200617, 200890
        );


update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='其他'
        AND d.`district_name` LIKE'普陀%'
        ),
    o.`circle_name`='其他'
    WHERE o.`Id` IN (
        3612, 3800, 3835, 3921, 3953, 3956, 3988, 4071, 4074, 4232, 4243, 4333, 4390, 4408, 4444, 4506, 4542, 4655, 4692, 4803, 4833, 4866, 4928, 5042, 200475, 200551, 200560, 200562, 200563, 200567, 200580, 200583, 200585, 200586, 200587, 200588, 200602, 200603, 200604, 200605, 200606, 200613, 200614, 200616, 200705, 200901
        );


update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='新江湾'
        AND d.`district_name` LIKE'杨浦%'
        ),
    o.`circle_name`='新江湾'
    WHERE o.`Id` IN (
        3778, 4023, 4025, 4104, 4153, 4179, 4236, 4386, 4449, 4712, 4813, 4896, 200636, 200637, 200638, 200639, 200660, 200662, 200894
        );


update `office` o set
    o.`circle_id`=(
        SELECT bc.`business_circle_id`
        FROM `business_circle` bc,`district` d
        WHERE bc.`district_id`=d.`district_id`
        AND bc.`business_circle_name`='大虹桥'
        AND d.`district_name` LIKE'长宁%'
        ),
    o.`circle_name`='大虹桥'
    WHERE o.`Id` IN (
        97, 105, 107, 109, 1488, 3207, 3211, 3212, 3213, 3214, 3215, 3216, 3221, 3226, 3227, 3228, 3229, 3230, 3311, 3611, 3636, 3637, 3641, 3671, 3714, 3720, 3747, 3763, 3773, 3788, 3795, 3810, 3829, 3834, 3841, 3882, 4095, 4107, 4113, 4116, 4135, 4223, 4308, 4361, 4396, 4453, 4498, 4562, 4595, 4613, 4664, 4667, 4669, 4706, 4726, 4817, 4822, 4830, 4913, 4952, 4953, 4990, 5053, 5162, 5184, 5186, 5189, 200163, 200165, 200166, 200168, 200170, 200317, 200364, 200648, 200722, 200841, 200854, 200924, 200941, 200945, 200954, 200982
        );

-- 验证

-- SELECT
-- o.`circle_id`,
-- bc.`business_circle_id`,
-- o.`circle_name`,
-- bc.`business_circle_name`
-- FROM `office` o
-- LEFT JOIN `business_circle` bc
-- ON o.`circle_id`=bc.`business_circle_id`
-- WHERE o.`Id` IN (
--         3589, 3946, 3964, 4166, 4175, 4176, 4195, 4320, 4338, 4457, 4489, 4547, 4567, 4578, 4580, 4637, 4682, 4721, 4897, 200372, 200772, 200853, 200921, 200938, 200966, 200977, 200978, 200979, 201001
--         );