# encoding:utf-8
from flask import Flask, session, redirect, url_for, escape, request


app = Flask(__name__)


@app.route('/')
def index():
    if 'username' in session:  # session是dict类型
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']  # 设置session中的username变量
        return redirect(url_for('index'))
    return ''''' 
        <form action="" method="post"> 
            <p><input type=text name=username> 
            <p><input type=submit value=Login> 
        </form> 
    '''


@app.route('/logout')
def logout():
    session.pop('username', None)  # 移除session中的username变量
    return redirect(url_for('index'))
# set the secret key.  keep this really secret:
'''
Session, Cookies以及一些第三方扩展都会用到SECRET_KEY值，
这是一个比较重要的配置值，应该尽可能设置为一个很难猜到的值，随机值更佳。
一个密钥应该足够随机。
你的操作系统可以基于一个密码随机生成器来生成漂亮的随机值，这个值可以用来做密钥:
import os
os.urandom(24)
'''
'''
设置密钥：
'''
app.config['SECRET_KEY'] = '\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\'
'''
或者
app.secret_key = '\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\'
或者
app.config.update(SECRET_KEY='\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\')
'''

if __name__ == '__main__':
    app.run(debug=True)
