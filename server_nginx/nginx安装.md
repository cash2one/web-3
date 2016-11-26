###Nginx
俄罗斯的程序设计师Igor Sysoev设计
俄国大型的入口网站及搜索引擎Rambler（Рамблер）使用
在BSD-like 协议下发行

- 轻量级
- Web 服务器/反向代理服务器/电子邮件（IMAP/POP3）代理服务器
- 占有内存少
- 并发能力强————在同类型的网页服务器中表现较好

###nginx作为HTTP服务器，有以下几项基本特性：
- 处理静态文件，索引文件以及自动索引；打开文件描述符缓冲．
- 无缓存的反向代理加速，简单的负载均衡和容错．
- FastCGI，简单的负载均衡和容错．
- 模块化的结构，包括gzipping，byte ranges，chunked responses以及 SSI-filter等filter。
- 如果由FastCGI或其它代理服务器处理单页中存在的多个SSI，则这项处理可以并行运行，而不需要相互等待。

Nginx以事件驱动的方式编写，专为性能优化而开发，常注重效率，有非常好的性能。它支持内核Poll模型，能经受高负载的考验，有报告表明能支持高达 `50,000` 个并发连接数。

Nginx是一个非常高效的反向代理、负载平衡。其拥有匹配 Lighttpd的性能，同时还没有Lighttpd的内存泄漏问题，而且Lighttpd的mod_proxy也有一些问题并且很久没有更新。但是Nginx并不支持cgi方式运行，原因是可以减少因此带来的一些程序上的漏洞。所以必须使用FastCGI方式来执行程序。

Nginx具有很高的稳定性。其它HTTP服务器，当遇到访问的峰值，或者有人恶意发起慢速连接时，很可能会导致服务器物理内存耗尽频繁交换，失去响应，只能重启服务器。Apache在处理流量爆发（爬虫或者Digg效应）的时候很容易过载，例如apache一旦上到200个以上进程，web响应速度就明显非常缓慢了。而Nginx采取了分阶段资源分配技术，使得它的CPU与内存占用率非常低。nginx官方表示保持10,000个没有活动的连接，它只占2.5M内存，所以类似DOS这样的攻击对nginx来说基本上是毫无用处的。就稳定性而言，nginx比lighthttpd更胜一筹。

Nginx支持热部署。它的启动特别容易，并且几乎可以做到7*24不间断运行，即使运行数个月也不需要重新启动。还能够在不间断服务的情况下，对软件版本进行进行升级。在相对比较大的网站，节约下来的服务器成本无疑是客观的。

###windows
1. 下载Nginx稳定版;
2. 解压到相应的目录，修改目录名字为nginx;
3. 进入nginx目录,双击nginx.exe启动nginx;
4. 直接在浏览器地址栏输入：localhost，便能看到欢迎页面；
5. 修改..\nginx\conf\nginx.conf；

###Linux（默认路径————/usr/local/nginx-***/sbin/nginx）
- yum -y install pcre*————安装prce（重定向支持）
- yum -y install openssl*————安装openssl（https支持，如果不需要https可以不安装）
- wget http://nginx.org/download/nginx-***.tar.gz
- tar -zxvf nginx-***.tar.gz
- 编译安装
    + cd nginx-***
    + ./configure
        * --prefix=/usr/local/nginx————可选，指定安装目录
        * --with-http_stub_status_module————启用ngx_http_stub_status_module（获取nginx自上次启动以来的工作状态）
    + make
    + make install

#####重启或关闭进程
- /usr/local/nginx-***/sbin/nginx -s reload
- /usr/local/nginx-***/sbin/nginx -s stop
- 关闭防火墙，或者添加防火墙规则————允许外部服务

丢失nginx.pid————/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf————验证配置文件

查看已安装的nginx 是否包含 stub_status 模块————/usr/local/nginx/sbin/nginx -V

#####文件目录权限
chown -R nginx用户 网站目录（相对路径）
chmod -R 755 网站目录（相对路径）
chmod 755 网站父目录（绝对路径）