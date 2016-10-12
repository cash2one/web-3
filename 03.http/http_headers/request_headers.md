###请求头
#####第一行：Method Request-URI HTTP-Version
- Method是大小写敏感的，包括OPTIONS、GET、HEAD、POST、PUT、DELETE、TRACE；
- Request-URI表示请求的URL。URI格式，为星号（*）时，说明请求并不用于某个特定的资源地址，而是用于服务器本身；
- HTTP- Version表示支持的HTTP版本；

|        Header       |                作用                |                  示例                 |
|---------------------|------------------------------------|---------------------------------------|
| Host                | 指定请求的服务器的域名和端口号     | www.zcmhi.com                         |
|                     | 没有返回400                        |                                       |
| Authorization       | HTTP授权的授权证书                 |                                       |
| Accept              | 浏览器端接受的媒体类型             | text/html、`*/*`                      |
|                     | 类型不对返回406                    |                                       |
| Accept-Language     | 浏览器接收的语言                   | en-us、zh-CN                          |
| Accept-Encoding     | 浏览器接收编码的压缩方法           | gzip,deflate                          |
| Accept-Charset      | 浏览器接受的字符编码集             | iso-8859-5                            |
| If-Match            | 只有请求内容与实体相匹配才执行请求 |                                       |
| If-None-Match       | ETag 改变（对比先前）才执行        |                                       |
|                     | 未改变返回304                      |                                       |
| If-Modified-Since   | 请求对象在指定时间之后修改，才执行 |                                       |
|                     | 否则返回代码304                    |                                       |
| If-Unmodified-Since |                                    |                                       |
| If-Range            | 如果请求的对象没变，获取缺少的部分 |                                       |
|                     | 如果对象改变了，获取整个对象       |                                       |
|                     | 通过ETag验证                       |                                       |
|                     | 总是跟 Range 头部一起使用          |                                       |
| Range               | 只请求实体的一部分，指定范围       | bytes=500-999,bytes=-500,bytes=500-;  |
|                     | 服务器可以忽略此请求头             |                                       |
|                     | GET包含Range，错误码是206，不是200 |                                       |
| Referer             | 先前网页的地址————来路             | http://...                            |
| User-Agent          | 客户端操作系统和浏览器名称、版本   |                                       |
| Host（必须）        | 指定请求的服务器的域名和端口号     | www.zcmhi.com（缺省端口号80）         |
|                     | 通常从HTTP URL中提取出来           |                                       |
| Cookie（最重要）    | 发送cookie值给HTTP 服务器          | $Version=1; Skin=new;                 |
| Upgrade             | 向服务器指定传输协议               | HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11 |

**extension-header允许客户端定义新的实体头，但是这些域可能无法未接受方识别。**