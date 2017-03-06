# -*- coding: utf-8 -*-
# @Date:   2017-03-06 17:11:13
# @Last Modified time: 2017-03-06 18:26:33
'''
request——请求对象
'''
from flask import request, render_template


def test_request(app):

    @app.route('/request')
    def test_request():
        '''
        render_template——加载并渲染模板——默认当前路径下的templates
        测试request对象
        :return:
        '''
        return render_template('request.html', request=request)


"""
某些 Flask 全局对象，实际上是特定环境下本地对象的代理。
在测试时会遇到由于没有请求对象而导致依赖于请求的代码会突然崩溃的情况。
使用with语句可以绑定test_request_context()环境管理器进行最简单的单元测试。
with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'

另一种方式是把整个 WSGI 环境传递给 request_context() 方法:
with app.request_context(environ):
    assert request.method == 'POST'
"""
