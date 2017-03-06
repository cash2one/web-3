# -*- coding: utf-8 -*-
# @Date:   2017-02-20 09:23:16
# @Last Modified time: 2017-03-06 17:31:24
from flask.ext.restful import Api, Resource, reqparse, fields, marshal_with


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

"""
parser = reqparse.RequestParser()  # 新建一个请求解析器RequestParser
parser.add_argument(
    'name',
    type=str,            # 规定参数类型，否则会拒绝并提示help的信息
    action='append',     # 多个值&列表
    dest='public_name',  # 以不同的名称存储参数
    location='',         # 指定解析参数的位置————form、args、headers、cookies、[...]
    )
parser_copy = parser.copy()
parser_copy.add_argument(...)     # 继承解析
arser_copy.replace_argument(...)  # 覆盖父级的任何参数
arser_copy.remove_argument(...)   # 完全删除参数
"""
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('value', type=int, help='a number', action='append')


class UserInfo(Resource):

    def get(self):
        return USERS, 200

    def post(self):
        """
        添加USER
        name=test&value=666&value=777
        :return:
        """
        args = parser.parse_args()
        user_id = int(max(USERS.keys()).lstrip('id')) + 1
        user_id = 'row%i' % user_id
        USERS[user_id] = {'name': args['name'], 'value': args['value']}
        return USERS[user_id], 201


def test_restful(app):
    """
    使用restful Api
    """
    api = Api(app)
    # 将资源类添加到Restful api资源里
    api.add_resource(HelloWorld, '/')
    api.add_resource(UserInfo, '/user')
