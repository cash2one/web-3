# -*- coding: utf-8 -*-
# @Date:   2016-12-07 17:23:51
# @Last Modified time: 2016-12-07 17:24:29
#
# 密码加密模块
from django.contrib.auth.hashers import *
from base.models import *


def create_pwd(ps):
    # 创建密码
    # 第二个参数为None时每次产生的密码都不用
    # 第三个参数为算法
    return make_password(ps, None, 'pbkdf2_sha256')


def check_pwd(phone, ps):
    try:
        u = SimpleUser.objects.get(phone=phone)
    except Exception, e:
        return False
    # check_password————接收明文和密文，返回False/True，验证密码的正确与否
    pwd_bool = check_password(ps, u.passwd)
    return pwd_bool


def create_session(request, phone, passwd):
    # 创建或修改session————request.session[key] = value
    # 获取session————request.session.get(key,default=None)
    # 删除session（不存在时报错）————del request.session[key]
    if check_pwd(phone, passwd):
        request.session['phone'] = phone
        request.session['passwd'] = passwd
        return True
    return False
