####开启django项目（cmd/terminal下）
cmd> python                     打开python交互式shell；
cmd> python managr.py shell     打开django交互式shell（测试Django代码）；
*exit()，cmd下退出程序。*

#####1. 创建项目
- cd (project_dir)
- windows————python ${django-admin.py} startproject ***
    + ${python}/Scripts/django-admin.py，可复制到任何方便的路径
- linux————django-admin startproject ***

#####2. 创建App
- cd (app_dir)
- python ${manage.py} startapp (app_name)

#####3. 后台管理————图形化操作数据库
#####4. 运行django服务器————启动Project
django可以和市面上主流的http服务器契合使用，开发过程中可以使用django自带的轻量级服务器；

*在1.7.1之后版本，django在运行之后会自动生成sqlite3数据库。*

*python文件名不能与python安装文件目录下的libs下的.lib模块重名。*

如果想从south升级到最新的django migration, 可以按以下步骤实现：

- 确保south中的migration全部被应用了；
- 从 INSTALLED_APPS中移除south；
- 删除每个app下migration目录中的所有文件, 除了__init__.py；
- 运行python manager.py makemigrations, Django会初始化migration；
- 运行python manager.py migrate, django会发现数据库和初始化的migration相同, 从而将他们标记为已应用。