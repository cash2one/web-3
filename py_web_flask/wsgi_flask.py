# -*- coding: utf-8 -*-
# @Date:   2016-11-28 09:23:52
# @Last Modified time: 2017-03-06 10:57:03
import sys

# Expand Python classes path with your app's path
sys.path.insert(0, "c:/Test_Web")

# 从flask运行入口文件导入app
from simple_flask import app

# Put logging code (and imports) here ...

# Initialize WSGI app object
application = app

'''
注意，application一定不能改成别的。因为mod_wsgi在解析这个文件时，只认application。
另外，同IIS不同的时，不需要给C:Test_Web文件夹加入NETWORK SERVICE用户的访问权限。
'''
