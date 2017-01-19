# -*- coding: utf-8 -*-
# @Date:   2016-12-22 21:14:08
# @Last Modified time: 2017-01-02 19:47:17
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
# 可以访问的域名————防止黑客构造包来发送请求
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
# 开发模式
# DEBUG为True
# （views匹配不到或者include不到）显示 TemplateDoesNotExist
# sql_queries————[{'sql': ..., 'time': ...},...]————请求期间到目前为止每个SQL 查询及花费的时间————按查询的顺序排序
# DEBUG为False
# 页面不会引发错误信息，静态文件都交给nginx、apache来处理
#
DEBUG = False
if platform.system() == "Windows":
    DEBUG = True
#
# 是否抑制视图的普通异常处理（异常继续上传）
# DEBUG_PROPAGATE_EXCEPTIONS = False
#
# Password validation
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
# INTERNAL_IPS = []
#
# 使用XFrameOptionsMiddleware中间件，为任何开放的HttpResponse设置X-Frame-Options协议头
# 默认为SAMEORIGIN，设为DENY————关闭
# @xframe_options_exempt————为特定视图去除X-Frame-Options协议头
# @xframe_options_deny————视图不能显示在iframe框架里
# @xframe_options_sameorigin————视图可以显示在iframe框架里
X_FRAME_OPTIONS = 'SAMEORIGIN'
# X_FRAME_OPTIONS = 'DENY'
