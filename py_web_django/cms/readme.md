文件夹是个独立的django项目

#####Django
高效的Python Web开发框架（类库），使你能够以最小的代价构建和维护高质量的Web应用。
学习Django就是学习她的命名规则和API。

#####安装使用
- django安装————[python ]pip[.exe] install django==1.7.1
    + 测试django安装
        * python
        * import django
        * django.VERSION————版本
        * django————安装路径
- 安装数据库
    1. 安装和配置数据库服务器本身。
    2. 为你的服务器后端安装连接数据库的Python库（数据库适配器）。

#####Django支持四种数据库
- [PostgreSQL](http://www.postgresql.org/)————[psycopg包](http://www.djangoproject.com/r/python-pgsql/)或者python-psycopg2，psycopg2-python，python-postgresql等。
PostgreSQL在成本、特性、速度和稳定性方面都做的比较平衡。
- [SQLite3](http://www.sqlite.org/)————[pysqlite包](http://initd.org/psycopg/download/)或者python-sqlite3，sqlite-python，pysqlite等。
- [MySQL](http://www.mysql.com/)————[MySQLdb包](http://www.djangoproject.com/r/python-mysql/)
或者python-mysql，python-mysqldb，mysql-python等。
- [Oracle](http://www.oracle.com/)————[cx_Oracle库](http://cx-oracle.sourceforge.net/)

###松耦合原则————保证互换性的软件开发方法
决定URL返回哪个视图函数和实现这个视图函数是在两个不同的地方，修改一块而不会影响另一块

###Django的设计哲学理念————业务逻辑与表现逻辑分离
- 将模板系统视为控制表现及表现相关逻辑的工具，不应提供超出此基本目标的功能；
- 在模板中不能直接调用 Python 代码；
- 语法不应受到 HTML/XML 的束缚；

cmd> python                     打开python交互式shell；
*exit()，cmd下退出程序。*

#####创建项目
- cd (project_dir)
- windows————python ${django-admin.py} startproject ***
    + ${python}/Scripts/django-admin.py，可复制到任何方便的路径
- linux————django-admin startproject ***

#####python ${manage.py} ***（cmd/terminal下）
|     参数     |                             含义                            |
|--------------|-------------------------------------------------------------|
| startapp *** | cd到任意路径，创建App                                       |
| shell        | 打开django交互式shell（测试Django代码，区别于python交互式） |
| runserver    | 通过django自带的轻量级服务器启动Project，开发调试           |

#####后台管理————图形化操作数据库
【127.0.0.1/phpmyadmin图形化Appserv数据库】

*在1.7.1之后版本，django在运行之后会自动生成sqlite3数据库。*

*python文件名不能与python安装文件目录下的libs下的.lib模块重名。*

如果想从south升级到最新的django migration, 可以按以下步骤实现：

- 确保south中的migration全部被应用了；
- 从 INSTALLED_APPS中移除south；
- 删除每个app下migration目录中的所有文件, 除了__init__.py；
- 运行python manager.py makemigrations, Django会初始化migration；
- 运行python manager.py migrate, django会发现数据库和初始化的migration相同, 从而将他们标记为已应用。