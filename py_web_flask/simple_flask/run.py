# -*- coding: utf-8 -*-
# @Date:   2017-02-20 09:23:16
# @Last Modified time: 2017-03-06 10:21:06
'''
request——请求对象
render_template——模板渲染方法
'''
from flask import Flask, request, render_template, url_for, abort
# __name__，使用一个单一模块
app = Flask(__name__)


@app.route('/')
# 使用 route() 装饰器来告诉 Flask 触发函数的 URL
def hello_world():
    return 'Hello World!'


@app.route('/hello/<name>', methods=['POST', 'GET'])
def hello(name):
    """加载模板"""
    return render_template('hello.html', name=name)

# 使用 request.form 属性处理表单数据


@app.route('/get_args', methods=['GET'])
# 默认动作就是GET，所以可以省略methods参数
def get_args():
    posts = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    try:
        id = int(request.args.get('id', 0))  # 获取GET参数，没有参数就赋值 0
    except ValueError:
        abort(404)  # 返回 404
    else:
        if id in posts:
            return'post_id = {0}'.format(id)
        else:
            abort(404)


if __name__ == '__main__':
    # 调试模式
    # app.run(debug=True)
    app.debug = True
    app.run(host='127.0.0.1')
