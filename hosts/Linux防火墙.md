###iptables
- 关闭防火墙————service iptables stop
- 添加一条开放端口的规则————允许外部访问
    * vim /etc/sysconfig/iptables-config
        - -A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT
- 重启服务：service iptables restart
- 修改客户机hosts或者直接打ip访问

###firewall————centos 7默认防火墙
- 查看防火墙状态————systemctl status firewalld.service
- 启动firewall————systemctl [start]mask firewalld.service
- 停止firewall————systemctl stop firewalld.service
- 禁止firewall开机启动————systemctl disable firewalld.service
- 改成iptables————systemctl start iptables.service
- 查看防火墙信息————firewall-cmd --list-all
- 开启端口————firewall-cmd --zone=public --add-port=10086/tcp --permanent
    + --zone————作用域
    + --add-port=10086/tcp————添加端口————端口/通讯协议
    + --permanent————永久生效，没有此参数重启后失效
- 关闭端口————firewall-cmd --zone= public --remove-port=8001/tcp --permanent
- 重启防火墙————firewall-cmd --reload

数据包要进入到内核必须要通过firewall的zone中的一个，而不同的zone里定义的规则不一样（即信任度不一样，过滤的强度也不一样）

#####zone
- 信任域————trusted————所有的网络连接都可以接受；
- 阻塞域————block————任何传入的网络数据包都将被阻止；
- 丢弃域————drop————任何传入的网络连接都被拒绝；
- 工作域————work————用在工作网络，只允许选中的服务通过————信任；
- 家庭域————home————用在家庭网络，只允许选中的服务通过————信任；
- 内部域————internal———— 用在内部网络，只允许选中的服务通过————信任；
- 外部域————external————用在路由器等启用伪装的外部网络，只允许选中的服务通过————不信任；
- 公共域————public————用以可以公开的部分，只允许选中的服务通过————不信任；
- 隔离域————DMZ————非军事区域，内外网络之间增加的一层网络，起到缓冲作用，只允许选中的服务通过————不信任；


###列出端口占用情况————netstat -lpnt
- 0.0.0.0————本机所有IP
- 127.0.0.1————本机的loopback地址，只能本机访问，无法通过本IP对外提供服务