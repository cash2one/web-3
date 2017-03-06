# -*- coding: utf-8 -*-
# @Date:   2017-03-06 18:25:41
# @Last Modified time: 2017-03-06 18:43:28
"""
abort() 函数————放弃请求并返回错误代码
404找不到页面，401无法访问页面，200一切正常
"""
from flask import request, render_template, abort, make_response


def test_abort(app):
    @app.route('/get_args', methods=['GET'])
    def get_args():
        """
        request.args.get()————获取GET参数（?id=***），没有参数就赋值0
        :return:
        """
        args = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        try:
            id = int(request.args.get('id', 0))
        except ValueError:
            abort(404)
            this_is_never_executed()  # abort后面的代码永远不会执行
        else:
            if id in args:
                return'get_id = {0}'.format(id)
            else:
                abort(404)

    @app.errorhandler(404)
    def page_not_found(e):
        """
        缺省情况下每种出错代码都会对应显示一个黑白的出错页面
        使用 errorhandler() 装饰器可以定制出错页面
        :param e:
        :return:
        """
        # return render_template('404.html'), 404
        """
        使用make_response()包裹返回表达式
        获得响应对象，进行修改，然后再返回，在视图内部掌控响应对象的结果
        """
        resp = make_response(render_template('404.html'), 404)
        resp.headers['X-Something'] = 'A value'
        # resp.set_cookie('test', 'zdd')
        return resp
