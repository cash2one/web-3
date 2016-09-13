# -*- coding: utf-8 -*-
from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/post', methods=['GET'])  # 默认动作就是GET，所以可以省略methods参数
def post():
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
    app.run(debug = True, host='127.0.0.1', port=8090)