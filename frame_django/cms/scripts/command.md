###python manage.py命令

|               参数              |                         含义                         |
|---------------------------------|------------------------------------------------------|
| 无参数                          | 列出可用参数                                         |
| shell                           | Django项目环境终端                                   |
| dbshell                         | 数据库命令行，可以执行数据库的SQL语句                |
|---------------------------------|------------------------------------------------------|
| diffsettings                    | 显示当前settings文件与默认设置的不同                 |
| check                           | ==旧版validate————检查                               |
|---------------------------------|------------------------------------------------------|
| makemigrations [appName]        | 基于当前models在appName/migrations下生成本次迁移文件 |
| migrate [appName]               | ==旧版syncdb————执行迁移动作————操作数据库（建表）   |
| sqlmigrate [appName]            | ==旧版sqlall————显示迁移的SQL语句                    |
| sqlflush                        | ==旧版flush————清空数据库                            |
| dumpdata appName > appName.json | 导出数据                                             |
| loaddata appName.json           | 导入数据                                             |
|---------------------------------|------------------------------------------------------|
| runserver 0.0.0.0:9000          | 启动自带`轻量级`服务器（默认8000端口）               |
| collectstatic                   | 自动收集static文件并复制到STATIC_ROOT                |
|---------------------------------|------------------------------------------------------|
| createsuperuser                 | 创建超级管理员                                       |
| changepassword username         | 修改用户密码                                         |
|---------------------------------|------------------------------------------------------|
| inspectdb [> models.py]         | 反向生成models                                       |

yum install MySQL-python

###python manage.py migrate --database="db"————指定同步哪一个数据库（默认同步到Default）
###save(using='legacy_users')指定要操作的数据库
###删除数据库后如果要重新生成，需要删掉migrations下的迁移文件，并删除django_migrations里的建表记录