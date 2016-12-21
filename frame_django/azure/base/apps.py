# -*- coding: utf-8 -*-
# @Date:   2016-11-28 12:41:49
# @Last Modified time: 2016-12-21 09:58:53
from __future__ import unicode_literals

from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'base'

# base为公共方法、公共静态文件存放目录
# 只有简单的测试页面，所以删除views.py、forms.py
# 没有数据库连接，所以删除migrations文件夹、models.py、admin.py
