###版本
1. MySQL Community Server————社区版本，开源免费，但不提供官方技术支持；
2. MySQL Enterprise Edition————企业版本，需付费，可以试用30天；
3. MySQL Cluster————集群版，开源免费。可将几个MySQL Server封装成一个Server；
4. MySQL Cluster CGE————高级集群版，需付费；
5. MySQL Workbench（GUI TOOL————专为MySQL设计的ER/数据库建模工具————DBDesigner4的继任者；
    + MySQL Workbench又分为两个版本————社区版（MySQL Workbench OSS）、商用版（MySQL Workbench SE）；

MySQL Community Server 是开源免费的，这也是我们通常用的MySQL的版本。看清楚了64bit ZIP Archive ，点击Download。（Installer安装程序只有32位，也可以用）

*MySQL 是开源（open source）数据库，可以查看源代码。mysql解压包里面的源文件和debug等文件都没有删掉，这些文件其实没有什么用的。dubug文件和.pdf文件可以删。*

###安装
- windows————ZIP Archive版是免安装的；
    + 解压到想安装的地方；
    + 以管理员身份打开cmd窗口，cd ${mysql}\bin；
    + mysqld --install————安装服务；
    + mysqld --remove ————删除服务；
    + mysqld --console————输出错误信息；
    + PATH:${mysql}\bin————配置环境变量；
- linux
    + centOS6
        * yum list | grep mysql————查看mysql安装包；
        * yum install -y mysql-server mysql mysql-devel
        * rpm -qi mysql-server————查看mysql-server版本
    + centOS7————默认mysql-server换成了mariadb
        * yum install -y mariadb-server mariadb
            - systemctl start mariadb————启动MariaDB
            - systemctl stop mariadb————停止MariaDB
            - systemctl restart mariadb————重启MariaDB
            - systemctl enable mariadb————设置开机启动
        * wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
        * rpm -ivh mysql-community-release-el7-5.noarch.rpm
        * yum install mysql-community-server

##卸载mysql
1. 通过程序自带的卸载程序或者在控制面板卸载
2. 删除所有mysql相关目录和文件：
    + C:\ProgramData\MySQL（默认是隐藏），如果删除不了则用360粉碎掉即可；
3. 删除mysql相关注册表，包括：
    + HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Application\MySQL文件；
    + HKEY_LOCAL_MACHINE\SYSTEM\ControlSet002\Services\Eventlog\Application\MySQL文件夹；
    + HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Eventlog\Application\MySQL的文件夹；