####HttpRequest对象————包含当前请求URL的一些信息

|         属性/方法         |                         说明/举例                          |
|---------------------------|------------------------------------------------------------|
| request.path              | 除域名以外的请求路径，以正斜杠开头-->"/hello/"             |
| request.get_host()        | 主机名（域名）-->"127.0.0.1:8000"、"www.***.com"           |
| request.get_full_path()   | 请求路径，可能包含查询字符串-->"/hello/?p=true"            |
| request.is_secure()       | 是否通过HTTPS访问，返回True/False                          |
|---------------------------|------------------------------------------------------------|
| request.META              | 一个字典————包含了所有本次HTTP请求的Header信息             |
|                           | 比如用户IP、用户Agent（浏览器的名称和版本号）              |
|                           | Header信息的完整列表取决于用户和服务器                     |
|                           | 用户所发送的Header信息                                     |
|                           | 服务器端设置的Header信息                                   |
|                           | header信息————用户浏览器提交的、不应该信任的`额外`数据     |
|                           | 用try/except语句或者字典的get()方法来处理                  |
|                           | HTTP_REFERER————进站前链接网页                             |
|                           | HTTP_USER_AGENT————用户浏览器的user-agent字符串            |
|                           | REMOTE_ADDR————客户端IP                                    |
|                           | 如果经过代理服务器，那么它可能是以逗号分割的多个IP         |
|---------------------------|------------------------------------------------------------|
| request.GET               | 用户get提交的信息————类字典对象————不需要视图传参          |
|                           | 数据可能来自 form 提交                                     |
|                           | 也可能是URL中的查询字符串(the query string)                |
| request.POST              | 用户post提交的信息————类字典对象————数据来自form提交       |
| request.raw_data          | 获取 post提交的xml原始数据                                 |
| request.POST.getlist(key) | 获取{'key':[...]}                                          |
|---------------------------|------------------------------------------------------------|
| request.COOKIES           | 类字典对象————每一个HttpRequest对象都有                    |
|                           | 可以使用它读取任何浏览器发送给视图（view）的cookies        |
|---------------------------|------------------------------------------------------------|
| request.session           | 类字典对象————启用SessionMiddleware后，每个HttpRequest都有 |

simplejson.loads(request.raw_post_data)
json.loads(request.body)

```
def show_color(request):
    if "favorite_color" in request.COOKIES:
        fav_color = request.session["fav_color"]
        ...
写cookies，需要使用 HttpResponse对象的 set_cookie()方法。
response.set_cookie(
    "favorite_color",
    request.GET["favorite_color"]
    )
request.session['foo'] = 'bar'
del request.session['foo']
request.session['foo'] = {}
request.session['foo']['bar'] = 'baz'
```

```
*GOOD (VERSION 1)*
    def ua_display_good1(request):
        try:
            ua = request.META['HTTP_USER_AGENT']
        except KeyError:
            ua = 'unknown'
        return HttpResponse("Your browser is %s" % ua)

*GOOD (VERSION 2)*
    def ua_display_good2(request):
        ua = request.META.get('HTTP_USER_AGENT', 'unknown')
        return HttpResponse("Your browser is %s" % ua)
```

###类字典对象————行为像Python标准字典对象，但在技术底层上不是标准字典对象
- 都有get()、keys()和values()方法；
- 可以用 for key in request.GET获取所有的键；
- 同时request.GET和request.POST拥有一些普通的字典对象所没有的方法；

###类文件对象————有一些基本文件操作方法，如read()，用来做真正的Python文件对象的代用品

###EmailMessage
- django.core.mail.send_mail()————EmailMessage类的一个发送e-mail的函数；
    + 服务器需要配置成能够对外发送邮件，并且在Django中设置出站服务器地址；
- 更高级的方法，比如附件，多部分邮件，以及对于邮件头部的完整控制；

若用户刷新一个包含POST表单的页面，那么请求将会重新发送造成重复。这通常会造成非期望的结果，比如说重复的数据库记录、发送两封同样的邮件等。 如果用户在POST表单之后被重定向至另外的页面，就不会造成重复的请求了。
我们应每次都给成功的POST请求做重定向。

若数据验证失败后，将原来的提交数据返回给模板，并且编辑HTML里的各字段来填充原来的值。以便用户查看哪里出现错误（用户也不需再次填写正确的字段值）。  

    return render_to_response(  
    　　'contact_form.html', {  
    　　　　'errors': errors,  
    　　　　'subject': request.POST.get('subject', ''),  
    　　　　'message': request.POST.get('message', ''),  
    　　　　'email': request.POST.get('email', ''),  
    　　}  
    )  

    <form action="/contact/" method="post">  
    　　<p>  
    　　Subject: <input type="text" name="subject" value="{{ subject }}" />
    　　</p>  
    　　<p>  
    　　Your e-mail (optional): <input type="text" name="email" value="{{ email }}" />  
    　　</p>  
    　　<p>  
    　　Message: <textarea name="message" rows="10" cols="50">{{ message }}</textarea>  
    　　<p>
    　　<input type="submit" value="Submit">
    </form>