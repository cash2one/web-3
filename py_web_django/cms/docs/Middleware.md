django所有的请求、返回都由中间件来完成。

中间件，就是处理HTTP的request和response的，类似插件，比如有Request中间件、view中间件、response中间件、exception中间件等，Middleware都需要在 “project/settings.py” 中 MIDDLEWARE_CLASSES 的定义。


首先，Middleware都需要在 “project/settings.py” 中 MIDDLEWARE_CLASSES 的定义， 一个HTTP请求，将被这里指定的中间件从头到尾处理一遍，暂且称这些需要挨个处理的中间件为处理链，如果链中某个处理器处理后没有返回response，就把请求传递给下一个处理器；如果链中某个处理器返回了response，直接跳出处理链由response中间件处理后返回给客户端，可以称之为短路处理。