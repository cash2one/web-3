# -*- coding: utf-8 -*-
# @Date:   2016-12-12 09:42:51
# @Last Modified time: 2016-12-12 09:43:11
#
# django自带的用户信息验证————authenticate(username=username,password=password)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# @login_required(login_url="/accounts/login")
# 默认使用settings.LOGIN_URL
