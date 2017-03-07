# -*- coding: utf-8 -*-
# @Date:   2016-12-21 16:52:51
# @Last Modified time: 2017-03-07 14:03:23
"""
默认设置————${django}\conf\global_settings.py
用户设置————项目中的 settings
用户设置与默认设置冲突时，覆盖掉默认设置
"""
import os
from _settings.database import *
from _settings.manager import *
from _settings.webpage import *
from _settings.local import *
from _settings.security import *
from _settings.caches import *
#
# os.path.abspath('.')————取决于工作目录，此处不能用
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 定义应用————加入新建app
# django.contrib包————Django自带的优秀附加组件(add-on、功能集、基本代码的组成部分)————可选、
INSTALLED_APPS = [
    'django.contrib.admin',         # 管理工具
    'django.contrib.auth',          # 用户鉴别系统
    'django.contrib.contenttypes',
    'django.contrib.sessions',      # 使用数据库支持的session————匿名会话
    'django.contrib.messages',
    'django.contrib.staticfiles',   # 收集每个应用（和指定地方）的静态文件到一个单独的位置
    # 'django.contrib.comments',    # 用户评注系统
    # 'raven.contrib.django',       # 如果项目和sentry位于不同服务器，需要安装raven
    'base',
    'cms.system',
]
#
# 中间件
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
    'cms.system.common.interceptors.LoginMiddleware',     # 自定义登录拦截器
    'cms.system.common.interceptors.AuthMiddleware',      # 自定义权限验证拦截器
    # 'django.middleware.cache.FetchFromCacheMiddleware'         # 必须放在最后
]

#
# 根URLconf
ROOT_URLCONF = 'cms.urls'


WSGI_APPLICATION = 'cms.wsgi.application'
