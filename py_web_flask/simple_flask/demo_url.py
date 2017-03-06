# -*- coding: utf-8 -*-
# @Date:   2017-03-06 17:10:19
# @Last Modified time: 2017-03-06 17:15:24
"""
route()装饰器绑定URL与函数
路由可以相同，函数名不可
"""
from flask import url_for  # 构造URL


def test_url(app):
    @app.route('/', methods=["GET"])       # 根url（GET请求可以省略methods参数）
    def root(): pass

    @app.route('/var')
    def var(): pass

    @app.route('/var/<name>')             # url使用变量
    def name(name):
        # return "<h1>hello %s</h1>" % name
        pass

    # @app.route('/var/<int:num_int>')    # 整数转换器

    @app.route('/var/<float:num_float>')  # 浮点数转换器
    def float(): pass

    @app.route('/var/<path:post_path>')   # 接受斜线
    def path(): pass

    with app.test_request_context():
        print url_for('root')
        print url_for('var')
        print url_for('var', name='zdd')   # 通过?传参
        print url_for('name', name='zdd')  # 使用变量传参
        print url_for('float', num_float=123)
        """
        结尾不带斜线的URL，如果多打，会报404
        结尾带斜线的URL，如果不带，会被Flask重定向到带斜线的规范URL去
        """
        print url_for('path', post_path='/path/path/')


'''
app.add_url_rule('/add', 'index', index)
'''
