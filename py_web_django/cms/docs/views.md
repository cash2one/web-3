###HttpRequest对象————包含当前请求URL的一些信息
|         属性/方法         |                        说明/举例                         |
|---------------------------|----------------------------------------------------------|
| request.path              | 除域名以外的请求路径，以正斜杠开头-->"/hello/"           |
| request.get_host()        | 主机名（域名）-->"127.0.0.1:8000"、"www.***.com"         |
| request.get_full_path()   | 请求路径，可能包含查询字符串-->"/hello/?p=true"          |
| request.is_secure()       | 是否通过HTTPS访问，返回True/False                        |
|---------------------------|----------------------------------------------------------|
| request.META              | 一个字典————包含了所有本次HTTP请求的Header信息           |
|                           | 比如用户IP、用户Agent（浏览器的名称和版本号）            |
|                           | Header信息的完整列表取决于用户和服务器                   |
|                           | 用户所发送的Header信息                                   |
|                           | 服务器端设置的Header信息                                 |
|                           | header信息————用户浏览器提交的、不应该信任的`额外`数据   |
|                           |                                                          |
|                           | HTTP_REFERER————进站前链接网页                           |
|                           | HTTP_USER_AGENT————用户浏览器的user-agent字符串          |
|                           | REMOTE_ADDR————客户端IP                                  |
|                           | 如果经过代理服务器，那么它可能是以逗号分割的多个IP       |
|---------------------------|----------------------------------------------------------|
| request.GET               | 用户get提交的信息————类字典对象————不需要视图传参        |
|                           | 数据可能来自 form 提交                                   |
|                           | 也可能是URL中的查询字符串(the query string)              |
| request.POST              | 用户post提交的信息————类字典对象————数据来自form提交     |
| request.body              | 获取请求体                                               |
| request.raw_data          | 获取 post提交的xml原始数据                               |
| request.POST.getlist(key) | 获取{'key':[...]}                                        |
| request.raw_post_data     | simplejson.loads(request.raw_post_data)————接收json数据  |
|---------------------------|----------------------------------------------------------|
| request.COOKIES           | 类字典对象————每个HttpRequest对象都有                    |
|                           | 可以使用它读取任何浏览器发送给视图（view）的cookies      |
|---------------------------|----------------------------------------------------------|
| request.session           | 类字典对象，启用SessionMiddleware后，每个HttpRequest都有 |
|                           | request.session[key] = value————创建或修改session        |
|                           | request.session[key][key] = value                        |
|                           | request.session.get(key,default=None)                    |
|                           | del request.session[key]（不存在时报错）                 |
|                           | request.session.set_expiry(value)————设置session超时     |
|                           | 整数（秒；0，用户关闭浏览器失效）、datatime或timedelta   |
|                           | None，依赖settings策略                                   |
|                           | if "**" is request.session————检测session值              |

###简单函数视图
```
def login(request, param):
    """
    param————url匹配的参数
    request.GET/POST————获取url?name=param的参数
    # 处理字典、类字典对象（尽量避免使用dict['key']取值）
    使用try/except语句
    使用dict.get('key')取值，找不到返回None，不报错
    """
    if request.method == 'GET':
        try:
            ua = request.META['HTTP_USER_AGENT']
        except KeyError:
            ua = 'unknown'
        # ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    elif request.method == 'POST':
        ...
```

###HttpResponse对象
|                    属性/方法                     |  说明/举例  |
|--------------------------------------------------|-------------|
| response.set_cookie(key, value)                  | 写cookie    |
| response.delete_cookie(key,path="/",domain=name) | 删除Cookies |
| if "cookie_name" is request.COOKIES              | 检测Cookies |

###类字典对象————行为像Python标准字典对象，但在技术底层上不是标准字典对象
- 都有get()、keys()和values()方法；
- 可以用 for key in request.GET获取所有的键；
- 同时request.GET和request.POST拥有一些普通的字典对象所没有的方法；

###类文件对象————有一些基本文件操作方法，如read()，用来做真正的Python文件对象的代用品

####POST请求重定向
若用户刷新一个包含POST表单的页面，那么请求将会重新发送造成重复。通常会造成重复的数据库记录、发送两封同样的邮件等。
如果用户在POST表单之后被重定向至另外的页面，就不会造成重复的请求了。我们应每次都给成功的POST请求做重定向。

####自定义表单填充信息（类似form验证）
若数据验证失败后，将原来的提交数据返回给模板，并且编辑HTML里的各字段来填充原来的值。以便用户查看哪里出现错误（用户也不需再次填写正确的字段值）。
```
return render_to_response(
　　'***.html', {
　　　　'subject': request.POST.get('subject', ''),
　　　　...
　　}
)
<input type="text" name="subject" value="{{ subject }}" />
```