####HttpRequest对象————包含当前请求URL的一些信息
|        属性/方法        |                    说明/举例                     |
|-------------------------|--------------------------------------------------|
| request.path            | 除域名以外的请求路径，以正斜杠开头-->"/hello/"   |
| request.get_host()      | 主机名（域名）-->"127.0.0.1:8000"、"www.***.com" |
| request.get_full_path() | 请求路径，可能包含查询字符串-->"/hello/?p=true"  |
| request.is_secure()     | 是否通过HTTPS访问，返回True/False                |

####request.META——————一个Python字典，包含了所有本次HTTP请求的Header信息，比如用户IP地址和用户Agent（浏览器的名称和版本号）。
注意，Header信息的完整列表取决于用户所发送的Header信息和服务器端设置的Header信息。这个字典中几个常见的键值有：

- HTTP_REFERER，进站前链接网页，如果有的话。（是REFERRER的笔误。）
- HTTP_USER_AGENT，用户浏览器的user-agent字符串，如果有的话。 例如： "Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17"。
- REMOTE_ADDR 客户端IP，如："12.345.67.89" 。(如果申请是经过代理服务器的话，那么它可能是以逗号分割的多个IP地址，如："12.345.67.89,23.456.78.90" )。

注意，因为 request.META 是一个普通的Python字典，因此当你试图访问一个不存在的键时，会触发一个KeyError异常。（HTTP header信息是由用户的浏览器所提交的、不应该给予信任的“额外”数据，因此你总是应该好好设计你的应用以便当一个特定的Header数据不存在时，给出一个优雅的回应。）你应该用 try/except 语句，或者用Python字典的 get()方法来处理这些“可能不存在的键”：  
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

#### HttpRequest对象还有两个属性包含了用户所提交的信息： request.GET 和 request.POST。

二者都是类字典对象，你可以通过它们来访问GET和POST数据。POST数据来自HTML中的〈form〉标签提交，而GET数据可能来自〈form〉提交也可能是URL中的查询字符串(the query string)。

- 类字典对象，他们的行为像Python里标准的字典对象，但在技术底层上他们不是标准字典对象。 比如说，request.GET和request.POST都有get()、keys()和values()方法，你可以用用 for key in request.GET获取所有的键。同时request.GET和request.POST拥有一些普通的字典对象所没有的方法。
- 类文件对象，这些Python对象有一些基本的方法，如read()，用来做真正的Python文件对象的代用品。

- request.GET['q']，获取name值为"p"的Html标签提交。
- `<form action="/search/" method="get">`  
    + action=""将表单提交给与当前页面相同的URL。
- request.raw_data 这个是获取 post提交的xml原始数据。

send_mail(  
　　request.POST['subject'],  
　　request.POST['message'],  
　　request.POST.get('email', 'noreply@example.com'),  
　　['siteowner@example.com'],  
)  
django.core.mail.send_mail()是Django的EmailMessage类的一个发送e-mail的函数。  
有四个必选参数：
    + 主题
    + 正文
    + 寄信人
    + 收件人列表
EmailMessage类提供了更高级的方法，比如附件，多部分邮件，以及对于邮件头部的完整控制。若要使用send_mail()函数来发送邮件，那么服务器需要配置成能够对外发送邮件，并且在Django中设置出站服务器地址。  
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


    每一个HttpRequest对象都有一个COOKIES对象，该对象的行为类似一个字典，你可以使用它读取任何浏览器发送给视图（view）的cookies。  
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

从内部来看，每个session都只是一个普通的Django model（在 django.contrib.sessions.models 中定义)。
每个session都由一个随机的32字节哈希串来标识，并存储于cookie中。 因为它是一个标准的模型，所以你可以使用Django数据库API来存取session。

    settings配置：
    MIDDLEWARE_CLASSES = [
        'django.contrib.sessions.middleware.SessionMiddleware'#必须有
        ]  
    INSTALLED_APPS = [
        'django.contrib.sessions' #必须有
        ]
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
        默认为 False ，会话cookie可以在用户浏览器中保持 SESSION_COOKIE_AGE 秒。
        设置为 True ，当浏览器关闭时，Django会使cookie失效。
    SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2
        会话cookie在用户浏览器中保持时间（默认1,209,600 秒，即两周）。
    SESSION_COOKIE_DOMAIN = None
        使用会话cookie（session cookies）的站点，默认设成None用于单个站点。
        设成一个字符串，如".example.com"以用于跨站点（cross-domain）的cookie；
    SESSION_COOKIE_NAME = "sessionid"
        会话中使用的cookie的名字，可以是任意的字符串。    
    SESSION_COOKIE_SECURE = False
        是否在session中使用安全cookie。
        如果设置True, cookie就只会通过HTTPS来安全传输。

关于Session框架内部工作方式的技术细节：

- Session字典接受任何支持序列化的Python对象（参考Python内建pickle模块的文档）。
- Session 数据存在数据库表 django_session 中，在需要的时候才会读取。如果你从不使用 request.session ，Django不会动相关数据库表的一根毛。
- Django只在需要的时候才送出cookie。如果你压根儿就没有设置任何会话数据，它不会 送出会话cookie(除非 SESSION_SAVE_EVERY_REQUEST 设置为 True )。
- Django session 框架完全而且只能基于cookie。它不会把会话ID编码在URL中（像某些工具(PHP,JSP)那样）。这是一个有意而为之的设计。把session放在URL中不只是难看，更重要的是这让你的站点 很容易受到攻击——通过 Referer header进行session ID窃听而实施的攻击。  
**源代码详见 django.contrib.sessions 。**

