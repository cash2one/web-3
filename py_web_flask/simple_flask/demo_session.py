# -*- coding: utf-8 -*-
# @Date:   2016-11-28 09:23:51
# @Last Modified time: 2017-03-06 18:41:57
'''
session对象————可以在不同请求之间储存信息
相当于用密钥签名加密的cookie，即用户可以查看你的cookie，但是如果没有密钥就无法修改它。
'''
from flask import session, redirect, url_for, escape, request
"""
使用会话之前你必须设置一个密钥。
    随机种子生成器
    >>> import os
    >>> os.urandom(24)
"""


def test_session(app):
    @app.route('/')
    def index():
        if 'username' in session:
            return 'Logged in as %s' % escape(session['username'])
        return 'You are not logged in'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return '''
            <form action="" method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''

    @app.route('/logout')
    def logout():
        # 如果会话中有用户名就删除它。
        session.pop('username', None)
        return redirect(url_for('index'))

    # 设置密钥，复杂一点：
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
