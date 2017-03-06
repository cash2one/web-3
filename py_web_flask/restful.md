###REST————web services和APIs的标准架构————很多APP的架构
- REST的六个特性
    + Client-Server：服务器端与客户端分离；
    + Stateless：每次客户端请求必需包含完整的信息————每一次请求都是独立的；
    + Cacheable（可缓存）：服务器端必需指定哪些请求是可以缓存的；
    + Layered System（分层结构）：服务器端与客户端通讯必需标准化，服务器的变更并不会影响客户端；
    + Uniform Interface（统一接口）：客户端与服务器端的通讯方法必需是统一的；
    + Code on demand（按需执行代码）：服务器端可以在上下文中执行代码；

诸如docker、daemon等服务都是提供了RESTful API，docker的CLI可以通过该API的URL地址与之通信。

#####Flask-RESTful————快速构建REST API的Flask插件
- 它能和现有的ORM配合实现轻量级数据抽象。
- Flask-RESTful鼓励小型化实践，非常简单易学。