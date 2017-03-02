###django连接apache
>
```
在Django开发环境，通过“python manage.py runserver 0.0.0.0:8000”可以启动一个简单的HTTP服务器。
当项目开发完成进行发布的时候，这个简单的应用服务器就不能满足需求了。这时候一个比较好的方案是把Django应用集成到Apache。
Django集成到Apache有两种方式：python_mod和mod_wsgi，后者更加稳定。
``

#####接口性能评估
|               接口              | Requests/sec |
|---------------------------------|--------------|
| mod_cgi (ScriptAlias)           |           10 |
| mod_python (PythonHandler)      |          400 |
| mod_wsgi (WSGIDaemonProcess)    |          700 |
| mod_wsgi (.htaccess/SetHandler) |          850 |
| mod_wsgi (WSGIScriptAlias)      |          900 |

从数字看，WSGIScriptAlias 是最优选择。

“任何性能提高，都将被你使用的大型Web框架如Django或TurboGears吃掉，尤其是用了数据库后端，大多数的 overhead 源自Python Web Framework以及任何访问数据库时的瓶颈。mod_wsgi上的overhead只是很小的一块，这一小块上的任何性能提高都很难被注意到。”


###[下载mod_wsgi](http://www.lfd.uci.edu/~gohlke/pythonlibs/#mod_wsgi)
解压（.whl包），把里面的mod_wsgi.so拷贝到Apache路径\modules下。

或者

###[下载源代码](https://github.com/GrahamDumpleton/mod_wsgi/releases)自己编译
下载解压后，在win32目录下找到与自己的python和apache服务器版本对应（或相近）的.mk文件，用记事本打开，将其中的APACHE_ROOTDIR和PYTHON_ROOTDIR修改为自己的apache和python的根目录。

###设置环境变量（path、include、lib）
在cmd窗口中输入:
```
set path =
    C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\bin;
    C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin;
    C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7;
set include = C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include;
set lib = C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib;
```
设置好环境变量，然后输入：nmake -f ap24py34-win32-VC10.mk install，就开始进行编译了。

*include <C:\Python27\include\Python.h>*