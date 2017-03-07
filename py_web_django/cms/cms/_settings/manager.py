# -*- coding: utf-8 -*-
# @Date:   2016-12-22 21:14:08
# @Last Modified time: 2017-01-02 21:29:20
# from password import password
############
# 发送邮件
############
#
# 邮件管理员站点
# SERVER_EMAIL = '***@***.com'
#
# 发送邮件的后台类
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#
# 发送邮件的SMTP主机、端口
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
#
# 发送邮件的邮箱、密码
EMAIL_HOST_USER = '2271404280@qq.com'
# EMAIL_HOST_PASSWORD = password
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


################################################
# 使用SENTRY进行错误日志集中管理
# django项目中产生的异常都集中到sentry服务器上
################################################
SENTRY_DSN = '127.0.0.1'

# pip install sentry
# mkdir ~/.sentry
# sentry init ~/.sentry/sentry.conf.py
# SENTRY_WEB_OPTIONS中加一项daemon: True————使sentry以daemon模式运行
# sentry start————启动sentry服务器
# 用浏览器访问 http://localhost:9000/，即可看到sentry的Web界面
#
# 如果项目和sentry位于不同服务器，可能需要安装raven
# pip install raven
#
# 可以接收代码错误通知的用户
# ADMINS = [
#     ('Full Name', 'email@example.com'),
#     ('Full Name', 'anotheremail@example.com')
# ]
#
# 接收错误通知的相关人员
# MANAGERS = ADMINS
#
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
