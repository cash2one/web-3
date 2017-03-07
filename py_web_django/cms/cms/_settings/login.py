# -*- coding: utf-8 -*-
# @Date:   2016-12-21 09:17:11
# @Last Modified time: 2016-12-21 09:21:34
#
# 定义django admin使用的User模型
# 默认————django.contrib.auth.models import User
AUTH_USER_MODEL = 'auth.User'
#
# 进行用户验证的python类
# 如果有多个————调用django.contrib.auth.authenticate()会一一尝试
# 如果用户名和密码在多个后台中都是合法的，Django 将在第一个匹配成功后停止处理
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
#
# （后台系统）登录登出重定向
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/accounts/profile/'


'''
django自带的用户信息验证————authenticate(username=username,password=password)
# @login_required(login_url="/accounts/login")————默认使用settings.LOGIN_URL
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
'''
