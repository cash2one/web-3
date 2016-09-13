# encoding:utf-8
'''
forward和redirect的区别		
forward内部跳转，redirect重定向跳转的区别

1.从地址栏显示来说
forward是服务器请求资源,服务器直接访问目标地址的URL,把那个URL的响应内容读取过来,然后把这些内容再发给浏览器.浏览器根本不知道服务器发送的内容从哪里来的,所以它的地址栏还是原来的地址.
redirect是服务端根据逻辑,发送一个状态码,告诉浏览器重新去请求那个地址.所以地址栏显示的是新的URL.

2.从数据共享来说
forward:转发页面和转发到的页面可以共享request里面的数据.
redirect:不能共享数据.

3.从运用地方来说
forward:一般用于用户登陆的时候,根据角色转发到相应的模块.
redirect:一般用于用户注销登陆时返回主页面和跳转到其它的网站等.

4.从效率来说
forward:高.
redirect:低.
'''
# flask重定向
from flask import Flask, url_for, redirect, abort, render_template, make_response

app = Flask(__name__)

'''
使用 redirect() 函数可以重定向
redirect(location, code=302)
the redirect status code. defaults to 302.Supported codes are 301, 302, 303, 305, and 307. 300 is not supported.
Example:redirect(url_for('customer_invalid', id=id,...))
'''


@app.route('/')
def hello():
    return redirect(url_for('foo'))


@app.route('/foo')
def foo():
    return 'Hello Foo!'


'''
使用 abort() 可以更早退出请求，并返回错误代码
'''


@app.route('/404')
def notfind():
    abort(404)  # 404找不到页面，401无法访问页面，200一切正常
    this_is_never_executed()


'''
缺省情况下每种出错代码都会对应显示一个黑白的出错页面。使用 errorhandler() 装饰器可以定制出错页面:
'''


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


'''
使用make_response()函数，包裹返回表达式，获得响应对象，并对该对象进行修改，然后再返回，在视图内部掌控响应对象的结果
'''


@app.route('/401')
def error():
    abort(401)


@app.errorhandler(401)
def not_found(error):
    resp = make_response(render_template('error.html'), 401)
    resp.headers['X-Something'] = 'A value'
    return resp


if __name__ == '__main__':
    app.debug = True
    app.run()
