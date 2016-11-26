##消息体结构
- 第一部分————Request/Response line；
- 第二部分————Request/Response header；
- 第三部分————body；
- header和body之间有个空行；

###头域
对请求/响应头域的扩展要求通讯双方都支持，如果存在不支持的请求头域，一般将会作为实体头域处理。

- 每个头域由一个域名、冒号（:）和域值三部分组成；
- 域名是大小写无关的；
- 域值前可以添加任何数量的空格符；
- 头域可以被扩展为多行，在每行开始处，使用至少一个空格或制表符；

###通用头
|     Header     |                  作用                  |                  示例                  |
|----------------|----------------------------------------|----------------------------------------|
| Cache-Control  | 指定Response-Request缓存机制           |                                        |
|                |                                        |                                        |
| Connection     | 是否持久连接（HTTP 1.1默认持久）       | keep-alive，继续使用上次建立的连接     |
|                |                                        | close，及时关闭连接                    |
| Date           | 生成请求/消息的具体时间和日期          | Sat, 11 Feb 2012 11:35:14 GM           |
| Pragma         | 用来包含实现特定的指令                 | no-cache，不缓存                       |
| Via            | 通知中间网关或代理服务器地址、通信协议 | 1.0 fred, 1.1 nowhere.com (Apache/1.1) |
| Content-Type   | 内容类型                               | application/x-www-form-urlencoded      |
|                |                                        | text/html; charset=utf-8               |
| Content-Length | 内容长度（十进制数字字节）             | 38                                     |
|                | 在数据下行的过程中                     | 19847                                  |
|                | Content-Length的方式                   |                                        |
|                | 要预先在服务器中缓存所有数据           |                                        |
|                | 然后所有数据一起发给客户端             |                                        |


####Cache -Control————指定请求和响应遵循的缓存机制
- 请求时的缓存指令————no-cache、no-store、max-age、 max-stale、min-fresh、only-if-cached；
    + max-age————客户机可以接收生存期不大于指定时间（以秒为单位）的响应；
    + min-fresh————客户机可以接收响应时间小于当前时间加上指定时间的响应；
    + max-stale————客户机可以接收超出超时期间的响应消息；
- 响应消息中的指令————public、private、no-cache、no-store、no-transform、must-revalidate、proxy-revalidate、max-age；
    + Public————可以被任何缓存所缓存；
    + Private————内容只缓存到私有缓存中，对于其他用户的请求无效；

- no-store————防止重要的信息被无意的发布。在请求消息中发送将使得请求和响应消息都不使用缓存；
- no-cache————请求或响应消息不能缓存；

---
实体信息一般由实体头域和实体组成。

实体可以是一个经过编码的字节流，它的编码方式由Content-Encoding或Content-Type定义，它的长度由Content-Length或Content-Range定义。

实体头域包含关于实体的原信息，实体头包括Allow、Content-Base、Content-Encoding、Content-Language、Content-Length、Content-Location、Content-MD5、Content-Range、Content-Type、 Etag、Expires、Last-Modified、extension-header。