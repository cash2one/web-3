# coding:utf-8
from flask import Flask  # 导入了 Flask 类
app = Flask(__name__)  # __name__，使用一个单一模块


@app.route('/')  # 使用 route() 装饰器来告诉 Flask 触发函数的 URL
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    # app.debug = True  # 调试模式
    app.run(debug=True)
