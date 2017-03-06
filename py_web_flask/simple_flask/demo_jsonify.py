# -*- coding: utf-8 -*-
# @Date:   2016-11-28 09:23:51
# @Last Modified time: 2017-03-06 17:27:31
'''
返回json字符串
jsonify(dict)————flask自带的json处理类，返回的为flask结果（携带了content- type="application/json"）
json.dumps(dict)————单纯的转换为json串，能够处理的类型比 jsonify多，比如list类型
'''
from flask import jsonify


def test_jsonify(app):
    dicts = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'done': False
        }
    ]

    @app.route('/json', methods=['GET'])
    def get_dicts():
        return jsonify({'dicts': dicts})
