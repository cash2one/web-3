#####闪现系统
一个好的应用和用户接口都有良好的反馈，否则到后来用户就会讨厌这个应用。 Flask 通过闪现系统来提供了一个易用的反馈方式。闪现系统的基本工作原理是在请求结束时 记录一个消息，提供且只提供给下一个请求使用。通常通过一个布局模板来展现闪现的消息。

flash() 用于闪现一个消息。在模板中，使用 get_flashed_messages() 来操作消息。
'''
'''
有时候可能会遇到数据出错需要纠正的情况。多数时候在类似情况下返回400_Bad_Request就没事了，但也有不会返回的时候，而代码还得继续运行下去。这时候就需要使用日志来记录这些不正常的东西了。

app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
logger 是一个标准的 Python Logger 类
'''
'''
WSGI，PythonWeb服务器网关接口
如果想要在应用中添加一个 WSGI 中间件，那么可以包装内部的 WSGI 应用。假设为了 解决 lighttpd 的错误，你要使用一个来自 Werkzeug 包的中间件，那么可以这样做:

from werkzeug.contrib.fixers import LighttpdCGIRootFix
app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)