###Web应用
- 浏览器发送一个HTTP请求；
- 服务器收到请求，生成一个HTML文档；
- 服务器把HTML文档作为HTTP响应的Body发送给浏览器；
- 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示；

最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

把接受HTTP请求、解析HTTP请求、发送HTTP响应这些底层代码由专门的服务器软件实现，用Python专注于生成HTML文档，不接触到TCP连接、HTTP原始请求和响应格式。所以，需要一个统一的接口，让我们专心用Python编写Web业务。这个接口就是WSGI。

WSGI接口定义非常简单，它只要求Web开发者【实现一个函数，就可以响应HTTP请求】。

###WSGI————Web Server Gateway Interface
- 基于现存的`CGI`标准而设计，提升可移植Web应用开发的共同点；
- WSGI位于web应用程序（框架）与web服务器之间，所在层的位置低于CGI；
- WSGI只是一份标准并没有定义如何去实现；
- 一个简单的普遍适用的服务器与Web框架之间的接口；
- WSGI是Python Web方面最Pythonic的类似于Java中的"servlet" API；
- 解决了Web应用框架和Web服务器之间选择的限制；

web服务器可以是CGI，mod_python（现通常用mod_wsgi代替），FastCGI或者是一个定义了WSGI标准的web服务器就像python标准库提供的独立WSGI服务器称为wsgiref。

PythonWeb服务器网关接口————Python Web Server Gateway Interface，标准在PEP(Python Enhancement Proposal)333中定义并被许多框架实现，其中包括django。

以前，如何选择合适的Web应用程序框架成为困扰Python初学者的一个问题，这是因为，一般而言，，反之亦然。那时的Python应用程序通常是为CGI，FastCGI，mod_python中的一个而设计，甚至是为特定Web服务器的自定义的API接口而设计的。

自从WSGI被开发出来以后，许多其它语言中也出现了类似接口。

- 2003年： 原初的Python版本
- 2007年： Rack，Ruby版本
- 2008年： Lua WSAPI，Lua版本
- 2009年： JSGI，Java版本
- 2009年： PSGI，Perl版本