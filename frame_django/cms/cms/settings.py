# -*- coding: utf-8 -*-
# @Date:   2016-12-21 16:52:51
# @Last Modified time: 2017-01-02 21:28:42
"""
默认设置————${django}\conf\global_settings.py
用户设置————项目中的 settings
用户设置与默认设置冲突时，覆盖掉默认设置
"""
import os
from settings_slice.database import *
from settings_slice.manage import *
from settings_slice.webpage import *
from settings_slice.local import *
from settings_slice.security import *
from settings_slice.session import *
#
# os.path.abspath('.')————取决于工作目录，此处不能用
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 定义应用————加入新建app
# django.contrib包————Django自带的优秀附加组件(add-on)————可选
# django.contrib是一套庞大的功能集，它是Django基本代码的组成部分
INSTALLED_APPS = [
    # 管理工具
    # 第一次运行syncdb命令时，系统会请你创建一个超级用户————旧版
    'django.contrib.admin',
    # 用户鉴别系统
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 使用数据库支持的session————匿名会话
    'django.contrib.sessions',
    'django.contrib.messages',
    # 收集每个应用（和指定地方）的静态文件到一个单独的位置
    'django.contrib.staticfiles',
    # 用户评注系统
    # django.contrib.comments,
    # 如果项目和sentry位于不同服务器，可能需要安装raven
    # 'raven.contrib.django',
    'base',
    'login',
]
#
# 中间件
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    # Session中间件
    # 在 request 中附加 session 属性
    # 在 response 的时候，适当的情况下保存 session 并发出相应的 cookie 到客户端
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 对跨站请求伪造简单易用的防护————默认验证每一个form的post请求
    # 跨站攻击————同时登陆多个网站时，恶意网站利用用户浏览器中的认证信息在其它网站上完成某些操作
    # 登录CSRF————攻击站点触发用户浏览器用其它人的认证信息登录到其它站点
    'django.middleware.csrf.CsrfViewMiddleware',
    # 用户登录判断
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 点击劫持防御
    # 不允许资源加载到（别人的）frame或者iframe中
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 开启国际化的支持（放在Session后）————翻译管理工具
    # 'django.middleware.locale.LocaleMiddleware',
    # 自定义登录拦截器
    'login.common.interceptor_middlewares.LoginMiddleware',
    # 自定义权限验证拦截器
    'login.common.interceptor_middlewares.MenuMiddleware',
]
#
# 根URLconf
ROOT_URLCONF = 'cms.urls'


WSGI_APPLICATION = 'cms.wsgi.application'
