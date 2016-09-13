# encoding:utf-8
from flask import Flask, request
'''
1.使用method属性可以操作当前请求方法（GET、POST等）
{{ request.method }}


2.使用form属性处理表单数据
request.form.get("提交控件的值",默认赋值,指定数据类型)从页面获取post提交的数据
{{ request.args }}和{{ request.form }}返回的是ImmutableMultiDict([])，可以通过to_dict()转成dict类型的
例如：request.args.to_dict()['id']
request.form['']，当form属性中不存在这个键时会发生什么？会引发一个KeyError。如果你不像捕捉一个标准错误一样捕捉KeyError，那么会显示一个 HTTP 400 Bad Request 错误页面。因此，多数情况下你不必处理这个问题。


3.使用args属性操作URL（如 ?key=value ）中提交的参数：searchword = request.args.get('key', '')
request.args.get("请求控件的值",默认赋值,指定数据类型)
从地址栏获取get请求的数据（在页面中打印{{ request.args }}，与地址栏中?后面的内容完全一致）
用户可能会改变URL导致出现一个400请求出错页面，这样降低了用户友好度。因此，我们推荐使用get或通过捕捉KeyError来访问 URL 参数。


4.用Flask处理文件上传要确保在你的HTML表单中设置enctype="multipart/form-data"属性
已上传的文件被储存在内存或文件系统的临时位置，通过请求对象files属性来访问上传的文件，每个上传的文件都储存在这个字典型属性中。
{{ request.files }}返回的是ImmutableMultiDict([])
request.files.get('...')接收<input type="file" name="..." />上传的文件
或者
f = request.files['the_file']
f.save('/var/www/uploads/uploaded_file.txt')
通过Werkzeug提供的secure_filename()函数，使用filename属性，可以知道文件上传之前其在客户端系统中的名称
请牢记这个值是 可以伪造的，永远不要信任这个值。
f.save('/var/www/uploads/' + secure_filename(f.filename))


5.使用cookies属性，访问cookies
request.cookies.get('username')
使用 cookies.get(key) 来代替 cookies[key] ，以避免当cookie不存在时引发KeyError。
使用请求对象的set_cookie方法来设置cookies。
cookies 设置在响应对象上。通常只是从视图函数返回字符串，Flask会把它们转换为响应对象。如果你想显式地转换，那么可以使用 make_response() 函数，然后再修改它。
@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
请求对象的cookies属性是一个包含了客户端传输的所有cookies的字典。在Flask中，如果能够使用会话，那么就不要直接使用cookies，因为会话比较安全一些。


6.{{ request.path }}获取页面地址栏路径
例如：在/customer/userlist地址栏路径下
{{ request.path.lower().startswith("/custom") }}返回True
{{ request.path.lower().endswith("tomer/userlist") }}返回True


7.{{ request.host.lower() }}获取host服务地址
例如：在任意页面
{{ request.host.lower().startswith('tower.local.cor') }}返回True
{{ request.host.lower().endswith('p.uban.com:20000') }}返回True


8.{{ request.remote_addr }}获取服务器IP地址


9.{{ request.url_rule }}获取页面地址栏路径
{{ request.url_rule.rule == request.path }}


10.request.json


11.{{ request.headers }}返回请求信息
request.headers.get


'''
app = Flask(__name__)
'''
某些对象在 Flask 中是全局对象，但是不是通常意义下的全局对象。这些对象实际上是 特定环境下本地对象的代理。
在测试 时会遇到由于没有请求对象而导致依赖于请求的代码会突然崩溃的情况。
使用with语句可以绑定test_request_context()环境管理器进行最简单的单元测试。
'''
with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'

'''
另一种方式是把整个 WSGI 环境传递给 request_context() 方法:
'''
with app.request_context(environ):
    assert request.method == 'POST'


if __name__ == '__main__':
    app.debug = True
    app.run()
