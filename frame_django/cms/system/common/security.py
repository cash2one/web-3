# -*- coding: utf-8 -*-
# @Date:   2016-12-21 17:45:51
# @Last Modified time: 2017-01-03 16:38:28
from django.contrib.auth.hashers import *
from system.models import *


def create_pwd(ps):
    # make_password————创建密码
    # 第二个参数为None时每次产生的密码都不用
    # 第三个参数为算法
    return make_password(ps, None, 'pbkdf2_sha256')


def check_pwd(phone, ps):
    try:
        u = SimpleUser.objects.get(phone=phone)
    except Exception, e:
        return False
    # check_password————验证密码的正确与否
    # 接收明文和密文，返回False/True
    pwd_bool = check_password(ps, u.passwd)
    return pwd_bool

