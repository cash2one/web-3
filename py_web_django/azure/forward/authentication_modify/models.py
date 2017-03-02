# -*- coding: utf-8 -*-
# @Date:   2016-12-12 09:42:51
# @Last Modified time: 2016-12-12 09:43:11
#
from django.db import models
#
# django自带的用户登录信息模型————User
# 修改方式————继承、扩展、自定义（修改AUTH_USER_MODEL）
# 在创建任何迁移或者第一次运行 manage.py migrate 前设置它
from django.contrib.auth.models import User
#
# django自带的用户信息验证————authenticate(username=username,password=password)
from django.contrib.auth import authenticate, login


# 扩展自带User————存储新字段到已有的User里


class UserProfile(models.Model):
    # OneToOneField————关联到一个存储额外信息的Model
    user = models.OneToOneField(User)
    department = models.CharField(max_length=100)