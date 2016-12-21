# -*- coding: utf-8 -*-
# @Date:   2016-12-20 12:18:32
# @Last Modified time: 2016-12-21 17:15:27
#
# 使用SENTRY进行错误日志集中管理
# django项目中产生的异常都集中到sentry服务器上
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
