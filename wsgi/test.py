# -*- coding: utf-8 -*-
# @Date:   2016-11-24 15:43:13
# @Last Modified time: 2016-11-24 15:44:44
#
# 测试uwsgi


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]

# 通过uwsgi运行该文件
# uwsgi --http :8001 --wsgi-file test.py
# 通过浏览器访问localhost
