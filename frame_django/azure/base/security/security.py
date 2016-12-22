# -*- coding: utf-8 -*-
# @Date:   2016-12-07 17:23:51
# @Last Modified time: 2016-12-07 17:24:29
#
# 密码加密模块
from django.contrib.auth.hashers import *
from base.models import SimpleUser
from django.core.mail import send_mail
from django.contrib.auth.models import Permission
from base.models import *
from django.contrib.contenttypes.models import ContentType

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


# 创建自定义权限
def test_premission():
    content_type = ContentType.objects.get_for_model(SimpleUser)
    # 每个permission都是django.contrib.auth.Permission类型的实例
    #
    # content_type————反应了permission属于哪个model
    # codename————代码逻辑中检查权限时要用
    # name————permission的描述，将permission打印到屏幕或页面时默认显示
    premission = Permission.objects.create(
        codename = "test",
        name = "can test",
        content_type = content_type
    )
    return premission
