# encoding:utf-8
'''
如果要返回json字符串，可以使用如下方法：
jsonStr={'result':'hello world'}
return jsonify(jsonStr)
# 或者json.dumps(jsonStr)
jsonStr 是dict类型，然后通过jsonify方法直接将dict类型转换为json串。
当然也可以使用json.dumps（jsonStr）将dict转换 为json字符串。
jsonify是flask自带的json处理类，返回的为flask结果，处理json串还携带了content- type="application/json"。
json.dumps是单纯的转换为json串。另外json.dumps能够处理的类型比 jsonify多，比如list类型。
'''
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
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


@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
