####TCP、UDP都是通信协议，http是基于TCP的。

HTTP本身就是一个协议，是从Web服务器传输超文本到本地浏览器的传送协议。
HTTP全称是HyperText Transfer Protocal，即：超文本传输协议，从1990年开始就在WWW上广泛应用，是现今在WWW上应用最多的协议，Http是应用层协议，当你上网浏览网页的时候，浏览器和Web服务器之间就会通过HTTP在Internet上进行数据的发送和接收。Http是一个基于请求/响应模式的、无状态的协议。即我们通常所说的Request/Response。

http协议是无状态的，同一个客户端的这次请求和上次请求是没有对应关系，对http服务器来说，它并不知道这两个请求来自同一个客户端。为了解决这个问题，Web程序引入了Cookie机制来维护状态。


通信流程：
首先客户端发送一个请求(request)给服务器；
服务器在接收到这个请求后生成一个响应(response)返回给客户端。

#####HTTP的Request/Response：

- Request格式：
    + Request line，请求行；
        * Method————请求方法：POST、GET；当使用GET方法的时候，body是为空的。
        * Path-to-resoure————请求的资源；
        * Http/version-number————HTTP协议的版本号；
    + Request header，请求头；
        * 在HTTP/1.1协议中，所有的请求头，除Host外，都是可选的。  
    **header和body之间有个空行。**
    + body，可选的消息体。

请求行和标题必须以<CR><LF> 作为结尾（也就是，回车然后换行）。空行内必须只有<CR><LF>而无其他空格。

- Response格式：
    + Response line，HTTP状态行；
        * HTTP/version-number————HTTP协议的版本号；
        * status-code————状态码，告诉客户端服务器是否产生了预期的Response；
        * message
    + Response header，应答头；  
    **header和body之间有个空行。**
    + body，可选的消息体。

URL(Uniform Resource Locator) 地址用于描述一个网络上的资源，  
基本格式：`schema://host[:port#]/path/…/[?query-string][#anchor]`  
URL例子：`http://www.mywebsite.com/sj/test/test.aspx?name=sviergn&x=true#stuff`

|     参数     |                  含义                  |         举例        |
|--------------|----------------------------------------|---------------------|
| scheme       | 指定低层的协议(例如：http、https、ftp) | http                |
| host         | HTTP服务器的IP地址或者域名             | www.mywebsite.com   |
| port#        | HTTP服务器的端口，默认是80             | 80                  |
| path         | 访问资源的路径                         | /sj/test/test.aspx  |
| query-string | 发送给http服务器的数据                 | name=sviergn&x=true |
| anchor-      | 锚                                     | stuff               |


####缓存机制
HTTP/1.1中缓存的目的是为了在很多情况下减少发送请求，同时在许多情况下可以不需要发送完整响应。前者减少了网络回路的数量；HTTP利用一个“过期（expiration）”机制来为此目的。后者减少了网络应用的带宽；HTTP用“验证（validation）”机制来为此目的。


基于HTTP的应用

1. HTTP代理
2. 多线程下载
下载工具开启多个发出HTTP请求的线程
每个http请求只请求资源文件的一部分：Content-Range: bytes 20000-40000/47000
合并每个线程下载的文件

HTTPS传输协议原理：
两种基本的加解密算法类型
对称加密：密钥只有一个，加密解密为同一个密码，且加解密速度快，典型的对称加密算法有DES、AES等。
非对称加密：密钥成对出现（且根据公钥无法推知私钥，根据私钥也无法推知公钥），加密解密使用不同密钥（公钥加密需要私钥解密，私钥加密需要公钥解密），相对对称加密速度较慢，典型的非对称加密算法有RSA、DSA等。
