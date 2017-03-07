# -*- coding: utf-8 -*-
# @Date:   2017-02-20 09:23:16
# @Last Modified time: 2017-03-07 13:37:53
from flask import Flask, make_response
app = Flask(__name__)

from demo_url import test_url
from demo_request import test_request
from demo_abort import test_abort
from demo_jsonify import test_jsonify
from demo_restful import test_restful
from demo_redirect import test_redirect
from demo_session import test_session
# test_url(app)
# test_request(app)
# test_jsonify(app)
test_restful(app)
# test_abort(app)
# test_redirect(app)
# test_session(app)


if __name__ == '__main__':
    # test_url()
    # 调试模式
    # app.run(debug=True, host='127.0.0.1')
    app.debug = True
    app.run(host='127.0.0.1')
