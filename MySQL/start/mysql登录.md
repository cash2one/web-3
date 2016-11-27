###windows
*mysql免安装最新版，没有data目录，没有用户、权限、密码等配置*

|      mysqld命令（data为空）      |             含义             |
|----------------------------------|------------------------------|
| mysqld --initialize-insecure     | 自动生成无密码的root用户，   |
| mysqld --initialize              | 自动生成带随机密码的root用户 |
| mysqld (-nt) --skip-grant-tables | 关闭mysql权限的检查          |

net start mysql
mysql -uroot -p，回车进入。（默认是没有密码的，有密码的话输入密码。）

###CMD连接MySQL
| 提示符 |                         命令                         |    含义    |
|--------|------------------------------------------------------|------------|
| shell> | mysql -h 主机地址 -u 用户名 -p密码                   | 连接mysql  |
| shell> | mysql -h 主机地址 -u 用户名 -p 库名-->回车，输入密码 | 连接单个库 |
| mysql> | EXIT                                                 | 退出mysql  |

*-h、-u后面的空格可有可无，-p若有空格，则识别为数据库名*
*直接关闭cmd窗口是没有退出的，要输入exit才会退出*

---
###修改密码
| 提示符 |                            命令                            |      含义      |
|--------|------------------------------------------------------------|----------------|
| shell> | mysqladmin -u用户名 [flush-privileges] -password 新密码    | 添加密码       |
| shell> | mysqladmin -u用户名 -p旧密码 password                      | 回车，修改密码 |
|        | root用户首次设置密码不要-p                                 |                |
|--------|------------------------------------------------------------|----------------|
| mysql> | SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpass'); | 修改密码       |
|--------|------------------------------------------------------------|----------------|
| mysql> | UPDATE user                                                | 编辑user表     |
|        | SET PASSWORD=PASSWORD("")                                  |                |
|        | WHERE user='root';                                         |                |

*mysql命令不区分大小写，所以后面都带一个";"作为命令结束符*

###修改权限
提示符：`mysql>`

|                 命令                 |                      含义                     |
|--------------------------------------|-----------------------------------------------|
| SHOW GRANTS;                         | 查看当前用户权限                              |
| SHOW GRANTS FOR 用户名@登录主机;     | 查看其他用户权限                              |
|--------------------------------------|-----------------------------------------------|
| GRANT                                | 给用户添加权限                                |
| [select[,insert[,delete[,file...]]]] | all privileges或者all，表示全部权限           |
| ON 库.表                             | *代表所有库或表                               |
| TO 用户名@登录主机                   | 主机可以是localhost、ip地址、机器名、域名     |
|                                      | 也可以用'%'表示从任何地址连接                 |
| IDENTIFIED BY \"密码\"               | \"\"代表没有密码                              |
| [WITH GRANT OPTION]                  | 让授权的用户，也可以将这些权限grant给其他用户 |
| [FLUSH PRIVILEGES]                   | 立即刷新生效                                  |
| ;                                    |                                               |
|--------------------------------------|-----------------------------------------------|
| UPDATE user                          | 使用update语句修改user表                      |
| SET HOST='登录主机'                  | 只允许用户在本机登录，"%"允许用户远程访问     |
| WHERE USER='username';               |                                               |
|--------------------------------------|-----------------------------------------------|
| RECOKE                               | 删除授权                                      |
| [select[,insert[,delete[,file...]]]] |                                               |
| ON 表.*库                            |                                               |
| FROM 用户名@登录主机;                |                                               |
|--------------------------------------|-----------------------------------------------|
| DELETE FROM user                     | 使用delete语句修改user表                      |
| WHERE                                |                                               |
| USER='username'                      |                                               |
| and HOST='登录主机';                 |                                               |

###允许远程登录
- 开启端口————firewall-cmd --zone=public --add-port=3306/tcp --permanent
    + unix系统上，mysql的登陆方式有两种，分别是socket和tcp/ip方式登陆
    + 指定参数-h，会使用tcp/ip的方式连接
    + 远程使用tcp
- 授权————GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'IDENTIFIED BY '123456' WITH GRANT OPTION;
- 刷新————flush privileges;


###权限生效
######重启mysql
```
shell> net stop mysql
shell> net start mysql
```
grant, revoke用户权限后，该用户只有重新连接MySQL数据库，权限才能生效。
######刷新数据库
```
shell> mysqladmin flush-privileges
或者
mysql> FLUSH PRIVILEGES;
```