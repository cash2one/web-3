# -*- coding: utf-8 -*-
# @Date:   2016-11-28 09:23:52
# @Last Modified time: 2017-03-06 18:46:09
import sys
import os
APP_PATH = os.path.join(os.path.abspath('.'), 'simple_flask')
# Expand Python classes path with your app's path
sys.path.insert(0, APP_PATH)

# 从flask运行入口文件导入app
from simple_flask.run import app

# Put logging code (and imports) here ...

# Initialize WSGI app object
application = app

'''
mod_wsgi在解析wsgi文件时，只认application
另外，同IIS不同的是，不需要给APP_PATH文件夹加入NETWORK SERVICE用户的访问权限。
'''
