# -*- coding: utf-8 -*-
# @Date:   2016-10-10 13:29:42
# @Last Modified time: 2016-10-10 14:39:01
#
# 可以接收代码错误通知的用户
#
ADMINS = [
    ('Full Name', 'email@example.com'),
    ('Full Name', 'anotheremail@example.com')
]
#
# 认证用户后端类
#
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
#
# 接收错误通知的相关人员
#
MANAGERS = ADMINS

INTERNAL_IPS = []
#
# 邮件管理员站点
#
SERVER_EMAIL = 'xinxinyu2011@163.com'
#
# 邮件配置
#
#
# SMTP地址、端口
#
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
#
# 自己的邮箱、密码
#
EMAIL_HOST_USER = 'pythonsuper@gmail.com'
EMAIL_HOST_PASSWORD = '******'
#
# 邮件Subject-line前缀，默认是'[django]'
EMAIL_SUBJECT_PREFIX = u'[CoorCar网]'
#
# 与SMTP服务器通信时，是否启动TLS安全链接，默认是false
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'tuweizhong <tuweizhong@163.com>'
