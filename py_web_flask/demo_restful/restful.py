# coding:utf-8
from flask import Flask
from flask.ext import restful  # importRESTful的模块

app = Flask(__name__)
api = restful.Api(app)  # 使用restful Api

# REST资源类Hello world必须继承自restful.Resource,并实现/重写父类的一些方法(比如get）


class HelloWorld(restful.Resource):

    def get(self):
        return {'hello': 'world'}

# 将Hello world添加到Restful api资源里，并没有使用装饰器
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
