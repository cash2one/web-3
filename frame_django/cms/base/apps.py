# -*- coding: utf-8 -*-
# @Date:   2016-12-22 21:14:08
# @Last Modified time: 2017-01-02 21:57:22
from __future__ import unicode_literals

from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'base'
# base为公共方法、公共静态文件存放目录
# 没有数据库连接，所以删除migrations文件夹、models.py、admin.py、urls.py、forms.py、views.py
