###ulimit -a
查看当前系统的所有限制值
###ulimit -n [***]
查看/修改（重启失效）当前的最大打开文件数

1. 在/etc/rc.local 中增加一行 ulimit -shn 65535
2. 在/etc/profile 中增加一行 ulimit -shn 65535
3. 在/etc/security/limits.conf 最后增加如下两行记录
    - soft nofile 65535
    - hard nofile 65535

在centos中使用第1种方式无效果，使用第3种方式有效果
在debian中使用第2种有效果