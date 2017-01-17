# coding:utf-8
from system.models import SimpleUser


def init_user_info(userid):
    u = SimpleUser.objects.filter(id=userid)[1]
    # role =

"""
select
ur.role_id, r.role_name, r.role_code
from user_role ur, role r
where ur.role_id = r.id
<include refid="Base_Conditions"/>
"""