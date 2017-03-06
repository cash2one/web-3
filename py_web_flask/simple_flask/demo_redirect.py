# -*- coding: utf-8 -*-
# @Date:   2017-03-06 17:43:11
# @Last Modified time: 2017-03-06 18:32:25
"""
flask重定向————redirect()
"""
from flask import url_for, redirect


'''
redirect(location, code=302)
the redirect status code. defaults to 302.Supported codes are 301, 302, 303, 305, and 307. 300 is not supported.
Example:redirect(url_for('customer_invalid', id=id,...))
'''


def test_redirect(app):
    @app.route('/')
    def hello():
        return redirect(url_for('foo'))

    @app.route('/foo')
    def foo():
        return 'Hello Foo!'
