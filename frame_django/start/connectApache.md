###django连接apache
>
```
在Django开发环境，通过“python manage.py runserver 0.0.0.0:8000”可以启动一个简单的HTTP服务器。
当项目开发完成进行发布的时候，这个简单的应用服务器就不能满足需求了。这时候一个比较好的方案是把Django应用集成到Apache。
Django集成到Apache有两种方式：python_mod和mod_wsgi，后者更加稳定。
``

#####接口性能评估
| 接口                            | Requests/sec |
| mod_cgi (ScriptAlias)           | 10           |
| mod_python (PythonHandler)      | 400          |
| mod_wsgi (WSGIDaemonProcess)    | 700          |
| mod_wsgi (.htaccess/SetHandler) | 850          |
| mod_wsgi (WSGIScriptAlias)      | 900          |

从数字看，WSGIScriptAlias 是最优选择。

“任何性能提高，都将被你使用的大型Web框架如Django或TurboGears吃掉，尤其是用了数据库后端，大多数的 overhead 源自Python Web Framework以及任何访问数据库时的瓶颈。mod_wsgi上的overhead只是很小的一块，这一小块上的任何性能提高都很难被注意到。”