# encoding:utf-8
'''
session对象，允许你在不同请求之间储存信息。相当于用密钥签名加密的cookie，即用户可以查看你的cookie，但是如果没有密钥就无法修改它。
'''
# 使用会话之前你必须设置一个密钥。
from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)


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
'''
生成随机数的关键在于一个好的随机种子，困此一个好的密钥应当有足够的随机性。你的操作系统可以使用一个随机生成器来生成一个好的随机种子：
>>> import os
>>> os.urandom(24)
'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
只要复制这个随机种子到你的代码中就行了。
'''

if __name__ == '__main__':
    app.debug = True
    app.run()
