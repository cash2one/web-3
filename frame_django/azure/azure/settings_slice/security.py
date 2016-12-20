# -*- coding: utf-8 -*-
# @Date:   2016-11-29 10:19:11
# @Last Modified time: 2016-12-08 13:27:52
#
# import re
import platform
#
# Django 支持的哈希算法类
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
]
#
# 设置哪些域名可以访问————防止黑客构造包来发送请求
# 即使在Apache/Nginx中绑定了，这里不允许的话，也是不能访问的
ALLOWED_HOSTS = ['*']
#
# 不允许访问的客户端————反爬虫
# DISALLOWED_USER_AGENTS = [
#     re.compile(r'^NaverBot.*'),
#     re.compile(r'^EmailSiphon.*'),
#     re.compile(r'^SiteSucker.*'),
#     re.compile(r'^sohu-search')
# ]
#
# 开发模式————缓存、出错信息等与正式环境有很大的区别
# 如果DEBUG设置为True，（views匹配不到或者include不到）显示 TemplateDoesNotExist
# 如果DEBUG设置为False，页面不会引发错误信息，静态文件都交给nginx、apache来处理
DEBUG = False
if platform.system() == "Windows":
    DEBUG = True
#
# 是否抑制视图的普通异常处理（异常继续上传）
# DEBUG_PROPAGATE_EXCEPTIONS = False
#
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
#
# 定义django admin使用的User模型
AUTH_USER_MODEL = 'auth.User'
# AUTH_USER_MODEL = 'azure.authentication_modify.User'
#
# 进行用户验证的python类————调用django.contrib.auth.authenticate()会一一尝试
# 如果用户名和密码在多个后台中都是合法的，Django 将在第一个匹配成功后停止处理
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

# 可以接收代码错误通知的用户
# ADMINS = [
#     ('Full Name', 'email@example.com'),
#     ('Full Name', 'anotheremail@example.com')
# ]
#
# 接收错误通知的相关人员
# MANAGERS = ADMINS
#
# INTERNAL_IPS = []
#
# 使用XFrameOptionsMiddleware中间件，为任何开放的HttpResponse设置X-Frame-Options协议头
# 默认为SAMEORIGIN，设为DENY————关闭
# @xframe_options_exempt————为特定视图去除X-Frame-Options协议头
# @xframe_options_deny————视图不能显示在iframe框架里
# @xframe_options_sameorigin————视图可以显示在iframe框架里
X_FRAME_OPTIONS = 'SAMEORIGIN'
# X_FRAME_OPTIONS = 'DENY'
#
# （后台系统）登录登出重定向
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/accounts/profile/'
