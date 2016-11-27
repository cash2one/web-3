####DBS————Data Base System————数据库系统
- 由数据库及其管理软件组成
- 为适应数据处理的需要而发展起来的一种较为理想的数据处理系统
- 一个为实际可运行的存储、维护和应用系统提供数据的软件系统
- 是存储介质 、处理对象和管理系统的集合体
- 大型数据库系统————SQL Server、Oracle、DB2
- 中小型数据库系统————Foxpro、Access、MySQL

####数据库系统一般由4个部分组成
1. 数据库（database，DB）————按一定的数学模型组织、描述和存储数据
    + 较小的冗余
    + 较高的数据独立性和易扩展性
    + 可为各种用户共享
2. 硬件————构成计算机系统的各种物理设备，包括存储所需的外部设备
3. 软件————包括操作系统、各种宿主语言、数据库管理系统及应用程序
4. 人员：主要有4类。
    + 系统分析员和数据库设计人员
	+ 应用程序员，负责编写使用数据库的应用程序
	+ 最终用户
	+ 数据库管理员（data base administrator，DBA），负责数据库的总体信息控制

###sqlGUI
####mysql GUI
1. phpMyAdmin
2. MySQLDumper
3. Navicat for MySQL
4. MySQL GUI Tools
5. MySQL ODBC Connector
6. SQLyog

连接localhost或者127.0.0.1，端口3306，用户名、密码等

####sqlite GUI
1. SQLiteSpy  免费 单文件 保持更新
- http://www.yunqa.de/delphi/doku.php/products/sqlitespy/
- http://www.oschina.net/p/sqlitespy
- 支持 Unicode，视图编码为utf-8，对gbk2312显示乱码。
- 单文件，界面设计紧凑，较稳定、功能较少，创建表与添加数据均需sql语句，快捷键较方便，
- 能满足一般的应用，但没有导出数据表功能。
- 同时只能打开一个数据库文件。
- 不支持二进制字段编辑。

2、SQLiteStudio （推荐）开源 免费 单文件 
http://sqlitestudio.one.pl/
更新及时，功能完善的sqlite2和sqlite3工具，视图编码支持utf8。
支持导出数据格式：csv、html、plain、sql、xml。
可同时打开多个数据库文件。
支持查看和编辑二进制字段。

3、SQLiteExpert
http://www.sqliteexpert.com/
个人版免费，提供了大多数基本的管理功能。
可以让用户管理SQLite3数据库并支持在不同数据库间诸如复制、粘贴记录和表；完全支持Unicode ，编辑器支持皮肤。


4、SQLite Manager（Firefox插件）免费
https://addons.mozilla.org/zh-cn/firefox/addon/sqlite-manager/
能完成日常大多数管理工作。基本功能齐全，可以将数据表导出为sql数据格式。


【免费但可能已停止更新】
1、Sqlite3Explorer 免费  
http://www.singular.gr/sqlite/
win xp下只识别gbk2312编码，界面紧凑，功能全面。

2、SQLite Database Browser 免费  
http://sqlitebrowser.sourceforge.net/
http://www.oschina.net/p/sqlitebrowser
SQLite Database browser 是一个SQLite数据库的轻量级GUI客户端，基于Qt库开发，主要是为非技术用户创建、修改和编辑SQLite数据库的工具，使用向导方式实现。支持各种平台, 包括Windows/Linux/Mac OS。
简单易用，具有基本数据库管理查询功能，并且能够导入和导出数据表，支持sql文件和csv两种方式。

3、SQLite Administrator 免费
http://sqliteadmin.orbmu2k.de/
功能齐全，界面有多语言，带导出功能，很久未更新，只识别sqlite2，可用于sqlite2到sqlite3的转换，
win xp下视图的编码为gbk2312，对utf-8显示乱码。
很小巧。


【收费版，通常功能丰富，更新及时】
1、Sqlite.Developer 收费 ￥79元 有中文版
http://www.sqlitedeveloper.com

2、SQLite Code Factory 收费 非商业单用户 $49
http://www.sqlmaestro.com
同公司类似产品 SQLite Maestro 收费 非商业单用户 $79
该公司出品了很多数据库管理工具

3、SQLite Manager 收费 $49 需安装
http://www.sqlabs.com/sqlitemanager.php

 4、Navicat for SQLite
http://www.navicat.de/cn/products/navicat_sqlite/sqlite_overview.html
很好用，很强大，不过价格也同样强大，适合企业使用。