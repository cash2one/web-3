- http————超文本传输协议
- url————统一资源定位符

###根据HTTP规范，GET用于信息获取，而且应该是安全的和幂等的。

- 安全意味着GET 请求一般不应产生副作用。就是说，该操作用于获取信息而非修改信息，不会影响资源的状态。
- 幂等的意味着对同一URL的多个请求应该返回同样的结果。

但在实际应用中，以上2条规定并没有这么严格。引用别人文章的例子：比如，新闻站点的头版不断更新。虽然第二次请求会返回不同的一批新闻，该操作仍然被认为是安全的和幂等的，因为它总是返回当前的新闻。从根本上说，如果目标是当用户打开一个链接时，他可以确信从自身的角度来看没有改变资源即可。

###根据HTTP规范，POST表示可能修改变服务器上的资源的请求。
在实际的做的时候，很多人没有按照HTTP规范去做，导致这个问题的原因有很多，比如说：

1. 很多人贪方便，更新资源时用了GET，因为用POST必须要到FORM（表单），这样会麻烦一点。
2. 对资源的增，删，改，查操作，其实都可以通过GET/POST完成，不需要用到PUT和DELETE。
3. 早期的MVC框架设计者们并没有有意识地将URL当作抽象的资源来看待和设计，所以导致一个比较严重的问题是传统的Web MVC框架基本上都只支持GET和POST两种HTTP方法，而不支持PUT和DELETE方法。


GET请求的数据会附在URL之后（把数据放置在HTTP协议头中），以?分割URL和传输数据，参数之间以&相连，如：
login.action?name=hyddd&password=idontknow&verify=%E4%BD%A0%E5%A5%BD。

- 如果数据是英文字母/数字，原样发送；
- 如果数据是空格，转换为+；
- 如果数据是中文或其他字符，用BASE64加密；
    + 得出如：%E4%BD%A0%E5%A5%BD，其中%XX中的XX为该符号以16进制表示的ASCII。

---

因为GET是通过URL提交数据，HTTP协议规范没有对URL长度进行限制，但是特定的浏览器及服务器对URL的长度有限制。

|       浏览器        |        （整个）URL长度限制         |
|---------------------|------------------------------------|
| IE                  | 2083字节(2K+35)                    |
| Netscape、FireFox等 | 没有长度限制，其限制取决于操作系统 |

POST请求把提交的数据则放置在是HTTP包的包体中。HTTP协议规范也没有对POST请求的数据进行大小限制，起限制作用的是服务器的处理程序的处理能力。

#####POST的安全性要比GET的安全性高

通过GET提交数据，用户名和密码将明文出现在URL上，登录页面有可能被浏览器缓存，其他人查看浏览器的历史纪录，就可以拿到账号和密码了；

使用GET提交数据还可能会造成Cross-site request forgery攻击；

Get是向服务器发索取数据的一种请求，而Post是向服务器提交数据的一种请求，在FORM（表单）中，Method默认为"GET"，实质上，GET和POST只是发送机制不同！