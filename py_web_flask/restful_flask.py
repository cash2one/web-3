# -*- coding: utf-8 -*-
# @Date:   2017-02-20 09:23:16
# @Last Modified time: 2017-03-06 10:22:22
from flask import Flask
from flask.ext.restful import Api, Resource, reqparse, fields, marshal_with

app = Flask(__name__)
# 使用restful Api
api = Api(app)


class HelloWorld(Resource):
    """
    REST资源类必须继承自Resource
    并实现/重写父类的一些方法(比如get）
    """

    def get(self):
        return {'hello': 'world'}


USERS = {
    'id1': {
        'name': 'debugo',
        'value': [70, 65]
    },
    'id2': {
        'name': 'leo',
        'value': [65]
    }
}

# 新建一个请求解析器RequestParser，规定类型为type，否则会拒绝并提示help的信息
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('value', type=int, help='rate is a number', action='append')


class UserInfo(Resource):
    def get(self):
        return USERS, 200

    def post(self):
        """
        添加USER
        name=test&value=666
        :return:
        """
        args = parser.parse_args()
        user_id = int(max(USERS.keys()).lstrip('id')) + 1
        user_id = 'row%i' % user_id
        USERS[user_id] = {'name': args['name'], 'value': args['value']}
        return USERS[user_id], 201


# 将资源类添加到Restful api资源里
api.add_resource(HelloWorld, '/')
api.add_resource(UserInfo, '/user')

if __name__ == '__main__':
    app.run(debug=True)
