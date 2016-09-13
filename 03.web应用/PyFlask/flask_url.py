# encoding:utf-8
from flask import Flask

app = Flask(__name__)  # 实例化app


@app.route('/')  # 装饰器绑定URL与函数
def hello_world():
    return 'Hello World'


@app.route('/index')
def index():
    return 'Index Page'


@app.route('/<username>')  # URL添加变量
def show_user(username):
    return 'User %s' % username


@app.route('/var/<int:post_int>')  # 整数转换器
def show_int(post_int):  # 路由可以相同，函数名不可
    return 'Post %d' % post_int


@app.route('/var/<float:post_float>')  # 浮点数转换器
def show_float(post_float):
    return 'Post %d' % post_float


@app.route('/var/<path:post_path>')  # 接受斜线
def show_path(post_path):
    return 'Post %s' % post_path


@app.route('/projects/')  # URL重定向
def projects():  # 结尾带斜线的URL，如果不带，会被Flask重定向到带斜线的规范URL去
    return 'projects page'


@app.route('/about')
def about():  # 结尾不带斜线的URL，如果多打，会报404
    return 'about page'


from flask import url_for  # 构造URL


@app.route('/structure')
def structure(): pass


@app.route('/structure/login')
def login(): pass


@app.route('/structure/<username>')
def user(username): pass

with app.test_request_context():
    print url_for('structure')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('user', username='John Doe')

            
@app.route('/add')
def index():
    pass
#Is equivalent to the following:
def index():
    pass
app.add_url_rule('/add', 'index', index)    

if __name__ == '__main__':
    # app.debug = True#调试模式，两种都可
    app.run(host='', port=5555, debug=True)
