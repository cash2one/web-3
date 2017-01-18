# coding:utf-8
import json
from system.common.security import check_pwd
from system.models import SimpleUser, UserRole, Role
from django.conf import settings
from django.core.cache import cache


def init_user_info(user_id=None):
    u = SimpleUser.objects.filter(id=user_id).values()[0]
    role = Role.objects.extra(select={'role_id': 'id'}).defer('id').values('id', 'role_name', 'role_code')
    if user_id:
        role = role.filter(userrole__user=user_id)
    if role.count() == 1:
        u = u.update(role[0])
    return u


def create_session(request, u):
    """
    if check_pwd(phone, passwd):
        request.session['phone'] = phone
        request.session['passwd'] = passwd
        return True
    return False
    """


def login(request, user_id):
    u = init_user_info(user_id)
    # 获取是否取消登录验证注解
    #
    # 验证session是否存在
    if request.session:
        # 当用户的current_role为空或 - 100时，则用户为多角色且没有选择角色，进入多角色选择界面
        pass
    else:
        # 获取用户cookies信息
        if request.COOKIES:
            create_session(request, u)
            pass


def read_from_cache(user_id):
    key = user_id
    value = cache.get(key, None)  # 获取缓存数据，key唯一
    if value is None:
        data = None
    else:
        data = json.loads(value)
    return data


def write_to_cache(user_id, u):
    # key = 'user_id_of_' + user_id
    key = user_id
    # 存储缓存数据
    # key唯一
    # data为存储的数据
    # 60*15为缓存数据的时间
    cache.set(key, json.dumps(u), settings.NEVER_REDIS_TIMEOUT)
