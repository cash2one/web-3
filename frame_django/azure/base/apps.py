# -*- coding: utf-8 -*-
# @Date:   2016-11-28 12:41:49
# @Last Modified time: 2017-01-02 19:23:22
from __future__ import unicode_literals

from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'base'

# base为公共方法、公共静态文件存放目录
# 没有数据库连接，所以删除migrations文件夹、models.py、admin.py
