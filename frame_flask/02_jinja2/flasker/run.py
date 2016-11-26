# encoding:utf-8
'''
request——请求对象
render_template——模板渲染方法

'''
from flask import Flask, request, render_template, url_for
app = Flask(__name__)


# 使用 request.form 属性处理表单数据
@app.route('/hello/<name>', methods=['POST', 'GET'])
def hello(name):
    return render_template('hello.html', name=name)  # 加载模板


if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.0.234')
