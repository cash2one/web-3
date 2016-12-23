# -*- coding: utf-8 -*-
# @Date:   2016-12-12 10:47:42
# @Last Modified time: 2016-12-12 10:47:53
#
# 进行用户验证的python类的路径————调用django.contrib.auth.authenticate()会一一尝试
# 如果用户名和密码在多个后台中都是合法的，Django 将在第一个匹配成功后停止处理
from django.contrib.auth.backends import ModelBackend

from django.contrib.sessions.middleware import SessionMiddleware