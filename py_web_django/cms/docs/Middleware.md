django所有的请求、返回都由中间件来完成。

中间件，就是处理HTTP的request和response的，类似插件，比如有Request中间件、view中间件、response中间件、exception中间件等，Middleware都需要在 “project/settings.py” 中 MIDDLEWARE_CLASSES 的定义。