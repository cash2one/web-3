# -*- coding: utf-8 -*-
# @Date:   2016-12-01 22:46:25
# @Last Modified time: 2016-12-06 07:40:05
#
import os
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
#
# 静态文件查找器
STATICFILES_FINDERS = [
    # 从STATICFILES_DIRS目录查找————默认开
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # 从每一个INSTALLED_APPS/static目录查找————默认
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
]
#
# 不属于任何一个特定应用的静态文件
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "azure/static"),
]
#
# python manage.py collectstatic————自动收集static文件并复制到STATIC_ROOT
# 用于部署的绝对路径————默认None
STATIC_ROOT = os.path.join(BASE_DIR, "static")
#
# STATIC_ROOT中的静态文件的访问URL————默认None————结尾必须是反斜线
# /static/
# 生产环境里根据web服务器静态文件服务器配置的路径来查找
# http://***————使用网络路径
# 可以在html里硬编码/static/，但是此路径可能发生变化，所以最好使用load标签
STATIC_URL = '/static/'
#
# 静态文件收集引擎
# 如果静态文件与Django在同一台服务器上，将使用默认引擎将静态文件收集到STATIC_ROOT中
# STATIC_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
