####一. Django
Django：一个可以使Web开发工作愉快并且高效的Web开发框架，使你能够以最小的代价构建和维护高质量的Web应用。
本质上来说， Django 只不过是用 Python 编写的一组类库。学习Django就是学习她的命名规则和API。

####二.  安装使用
#####1. django安装
- [python ]pip[.exe] install django==1.7.1

#####2. 测试django安装
- python
- import django
- django.VERSION

#####3.  安装数据库
1. 安装和配置数据库服务器本身。
2. 为你的服务器后端安装连接数据库的Python库（数据库适配器）。

Django支持四种数据库

- [PostgreSQL](http://www.postgresql.org/)————[psycopg包](http://www.djangoproject.com/r/python-pgsql/)或者python-psycopg2，psycopg2-python，python-postgresql等。
PostgreSQL在成本、特性、速度和稳定性方面都做的比较平衡。
- [SQLite3](http://www.sqlite.org/)————[pysqlite包](http://initd.org/psycopg/download/)或者python-sqlite3，sqlite-python，pysqlite等。
- [MySQL](http://www.mysql.com/)————[MySQLdb包](http://www.djangoproject.com/r/python-mysql/)
或者python-mysql，python-mysqldb，mysql-python等。
- [Oracle](http://www.oracle.com/)————[cx_Oracle库](http://cx-oracle.sourceforge.net/)

【127.0.0.1/phpmyadmin图形化Appserv数据库】