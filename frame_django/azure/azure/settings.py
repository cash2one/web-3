# -*- coding: utf-8 -*-
# @Date:   2016-11-28 11:03:52
# @Last Modified time: 2016-12-21 17:17:08
#
import os
#
# 根路径（django的路径符————"/"————同Linux）
# django自动为href添加站点前缀
# os.path.abspath('.')————取决于工作目录，此处不能用
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# 根URLconf
ROOT_URLCONF = 'azure.urls'
#
# 定义应用————加入新建app
# django.contrib包————Django自带的优秀附加组件(add-on)————可选
# django.contrib是一套庞大的功能集，它是Django基本代码的组成部分，Django框架就是由众多包含附加组件的基本代码构成的
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
    # 'forward'
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
    # 点击劫持的防御————不允许资源加载到（别人的）frame或者iframe中
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 开启国际化的支持（放在Session后）————把管理工具翻译你想要的语言
    # 'django.middleware.locale.LocaleMiddleware',
    # 自定义登录拦截器
    'login.common.interceptor.InterceptorMiddleware'
]
#=========================================================================
from settings_slice.security import *
from settings_slice.session import *
from settings_slice.databases import *
from settings_slice.templates import *
from settings_slice.static import *
# from settings_slice.upload import *
from settings_slice.local import *
from settings_slice.email import *
#=========================================================================
# 是否输出Etag头————节省带宽，但降低性能
# USE_ETAGS = False
# DEFAULT_CONTENT_TYPE = 'text/html'
# DEFAULT_CHARSET = 'utf-8'
# FILE_CHARSET = 'utf-8'
#
# 是否在每个URL后添加斜杠
# APPEND_SLASH = False
#
# 是否自动添加www
# PREPEND_WWW = False
# ABSOLUTE_URL_OVERRIDES = {}
# ALLOWED_INCLUDE_ROOTS = []
#
# 404异常不报错的url
# IGNORABLE_404_URLS = [
#     re.compile(r'^/apple-touch-icon.*\.png$'),
#     re.compile(r'^/favicon.ico$'),
#     re.compile(r'^/robots.txt$'),
#     re.compile(r'^/phpmyadmin/'),
#     re.compile(r'\.(cgi|php|pl)$'),
# ]
