# encoding:utf-8
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

# 配置文件
DATABASE = os.path.join(os.path.abspath(
    '..'), 'sqlite_db\\flaskr.db')  # 数据存储文件
DEBUG = True
'''
DEBUG标志用于开关交互调试器。因为调试模式允许用户执行服务器上的代码，所以永远不要在生产环境中打开调试模式！
'''
SECRET_KEY = 'development key'  # secret_key（密钥）用于保持客户端会话安全
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)  # 加载配置文件
'''
from_object()会搜索给定的对象中所有变量名均为大字字母的变量（如果该对象是一个字符串就会直接导入它）。
from_envvar()从一个配置文件中导入配置，app.config.from_envvar('FLASKR_SETTINGS', silent=True)
设置一个 FLASKR_SETTINGS 的环境变量来指定一个配置文件，并根据该文件来重载缺省的配置。silent=True告诉Flask如果没有这个环境变量不要报错。
'''


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])  # 关联数据库


def init_db():
    with closing(connect_db()) as db:  # closing()帮助函数允许我们在with代码块保持数据库连接打开。
        # 应用对象的open_resource()方法支持也支持这个功能，
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())  # 可以在 with代码块中直接使用。
        db.commit()


@app.before_request  # before_request() 装饰的函数会在请求之前调用，且不传递参数。
def before_request():
    g.db = connect_db()
'''
把数据库连接保存在 Flask 提供的特殊的g对象中。这个对象与每一个请求是一一对应的，并且只在函数内部有效。不要在其它对象中储存类似信息， 因为在多线程环境下无效。这个特殊的 g 对象会在后台神奇的工作，保证系统正常运行。
'''
'''
after_request()装饰的函数会在请求之后调用，且传递参数给客户端响应对象。必须传递响应对象，所以在出错的情况下就不会执行。
teardown_request()装饰的函数在响应对象构建后被调用。它们不允许修改请求，并且它们的返回值被忽略。如果请求过程中出错，那么这个错误会传递给每个函数；否则传递None。
'''

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()


# 视图函数
@app.route('/')
def show_entries():
    cur = g.db.execute('select title,text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.0.234')
