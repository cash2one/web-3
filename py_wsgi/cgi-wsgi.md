```
    浏览器                      chrome、firefox、ie等
      ｜
    web服务器                   nginx、apache等
      ｜
    网关接口                    CGI、FastCGI、WSGI等
      ｜
    Python（程序、Web框架）     Django、Flask、Tornado等
```
###Web应用
- 浏览器发送一个HTTP请求；
- 服务器收到请求，生成一个HTML文档；
- 服务器把HTML文档作为HTTP响应的Body发送给浏览器；
- 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示；

最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

#####CGI标准————PythonWeb开发最简单、原始和直接的办法（1998年流行）
- 首先做一个Python脚本，输出HTML代码，然后保存成.cgi扩展名的文件，通过浏览器访问此文件；
- 用户请求CGI，脚本代码打印Content-Type行，换行；
- 再接下来是一些HTML的起始标签，然后连接数据库并执行一些查询操作，获取指定数据，在遍历数据的同时，生成一个HTML列表；
- 最后，输出HTML的结束标签并且关闭数据库连接；

#####WSGI————Python Web服务器网关接口————Web Server Gateway Interface
- 把接受HTTP请求、解析HTTP请求、发送HTTP响应这些底层代码由专门的服务器软件实现；
- 一个统一的接口，只要求Web开发者`实现一个函数，就可以响应HTTP请求`；
- 让Python专注于编写Web业务（生成HTML文档），不接触TCP连接、HTTP原始请求和响应格式；
- 基于现存的`CGI`标准而设计，提升可移植Web应用开发的共同点；
- 位于web应用程序（框架）与web服务器之间，所在层的位置低于CGI；
- WSGI只是一份标准并没有定义如何去实现；
- 一个简单的普遍适用的服务器与Web框架之间的接口；
- WSGI是Python Web方面最Pythonic的类似于Java中的"servlet" API；
- 解决了Web应用框架和Web服务器之间选择的限制；

web服务器可以是CGI，mod_python（现通常用mod_wsgi代替），FastCGI或者是一个定义了WSGI标准的web服务器就像python标准库提供的独立WSGI服务器称为wsgiref。

PythonWeb服务器网关接口————Python Web Server Gateway Interface，标准在PEP(Python Enhancement Proposal)333中定义并被许多框架实现，其中包括django。

以前，如何选择合适的Web应用程序框架成为困扰Python初学者的一个问题，这是因为，一般而言，Web应用框架的选择将限制可用的Web服务器的选择，反之亦然。那时的Python应用程序通常是为CGI，FastCGI，mod_python中的一个而设计，甚至是为特定Web服务器的自定义的API接口而设计的。

自从WSGI被开发出来以后，许多其它语言中也出现了类似接口。

- 2003年： 原初的Python版本
- 2007年： Rack，Ruby版本
- 2008年： Lua WSAPI，Lua版本
- 2009年： JSGI，Java版本
- 2009年： PSGI，Perl版本

###Python Paste————WSGI底层工具集，包括多线程、SSL和 基于Cookies、sessions等的验证(authentication)库，可以用Paste方便地搭建自己的Web框架。