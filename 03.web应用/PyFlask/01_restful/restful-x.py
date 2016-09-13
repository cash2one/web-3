# coding:utf-8
from flask import Flask
from flask.ext.restful import reqparse, Api, Resource, fields, marshal_with

app = Flask(__name__)
api = Api(app)

USERS = {'id1': {'name': 'debugo', 'value': [
    70, 65]}, 'id2': {'name': 'leo', 'value': [65]}}
# 新建一个请求解析器RequestParser，规定类型为type，否则会拒绝并提示help的信息
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('value', type=int,
                    help='rate is a number', action='append')


class UserInfo(Resource):

    def get(self):
        return USERS, 200

    def post(self):
        args = parser.parse_args()
        user_id = int(max(USERS.keys()).lstrip('id')) + 1
        user_id = 'row%i' % user_id
        USERS[user_id] = {'name': args['name'], 'values': args['values']}
        return USERS[user_id], 201

api.add_resource(UserInfo, '/')

if __name__ == '__main__':
    app.run(debug=True)
