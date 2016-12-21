# -*- coding: utf-8 -*-
# @Date:   2016-12-18 15:51:59
# @Last Modified time: 2016-12-21 17:15:06
#
from password import password
#
# 邮件管理员站点
# SERVER_EMAIL = 'xinxinyu2011@163.com'
#
# 发送邮件使用的后台类
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# 发送邮件的SMTP主机、端口
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
#
# 用来发送邮件的邮箱、密码
EMAIL_HOST_USER = '2271404280@qq.com'
EMAIL_HOST_PASSWORD = password
#
# 与SMTP服务器通信时使用的安全链接协议
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
#
# 邮件Subject-line前缀，默认是'[django]'
EMAIL_SUBJECT_PREFIX = u'[Personal Space]'
#
# 发件人
DEFAULT_FROM_EMAIL = 'D <2271404280@qq.com>'
