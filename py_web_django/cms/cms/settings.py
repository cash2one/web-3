# -*- coding: utf-8 -*-
# @Date:   2016-12-21 16:52:51
# @Last Modified time: 2017-03-07 14:03:23
"""
default settings————${django}\conf\global_settings.py
default settings covered by project settings
"""
import os
from _settings.database import *
from _settings.manager import *
from _settings.webpage import *
from _settings.local import *
from _settings.security import *
from _settings.caches import *

INSTALLED_APPS = [
    "django.contrib.admin",          # 管理站点
    "django.contrib.auth",           # 认证系统
    "django.contrib.contenttypes",   # 用于内容类型的框架
    "django.contrib.sessions",       # 会话框架
    "django.contrib.messages",       # 消息框架
    "django.contrib.staticfiles",    # 管理（收集）静态文件的框架
    # 'django.contrib.comments',     # 用户评注系统
    # 'raven.contrib.django',        # 如果项目和sentry位于不同服务器，需要安装raven
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


MIDDLEWARE_CLASSES = [
    # 'django.middleware.cache.UpdateCacheMiddleware',           # 开启全站缓存————必须放在开始位置
    'django.middleware.security.SecurityMiddleware',
    # 给request加session属性，在response时，适当的情况下保存 session 并发送相应的cookie到客户端
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 对跨站请求伪造简单易用的防护————默认验证每一个form的post请求
    # 跨站攻击————同时登陆多个网站时，恶意网站利用用户浏览器中的认证信息在其它网站上完成某些操作
    # 登录CSRF————攻击站点触发用户浏览器用其它人的认证信息登录到其它站点
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',   # 用户登录判断（后台）
    'django.contrib.messages.middleware.MessageMiddleware',
    # 点击劫持防御————不允许资源加载到（别人的）frame/iframe中
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',               # 国际化的支持（放在Session后）————翻译管理工具
    # 'cms.test_apps.system.common.interceptors.LoginMiddleware',     # 自定义登录拦截器
    # 'cms.test_apps.system.common.interceptors.AuthMiddleware',      # 自定义权限验证拦截器
    # 'django.middleware.cache.FetchFromCacheMiddleware'         # 必须放在最后
]

#
# 根URLconf
ROOT_URLCONF = 'cms.urls'


WSGI_APPLICATION = 'cms.wsgi.application'
