##### 安装
控制面板-->程序-->打开或关闭Windows服务-->“Internet信息服务”-->选中下面所有选项-->点击确定后，开始更新服务。

更新完成后，打开浏览器，输入[http://localhost](http://localhost/)（127.0.0.1:80）回车，如果此时出现IIS界面，说明Web服务器已经搭建成功。如果没有成功，重启计算机。

##### 使用
当web服务器搭建成功后，我们下一步所要做的就是把我们开发的网站安装到Web服务器的目录中。一般情况下，当Web服务器安装完成后，会创建路径“%系统根目录%inetpub/wwwroot”，将我们开发的网站COPY到该路径下。即可实现本地访问该网站。

控制面板-->管理工具-->Internet 信息服务（IIS）管理器-->右键点击网站-->添加网站-->输入网站名称。


##### 访问
控制面板-->系统和安全-->允许程序通过Windows防火墙-->勾选“万维网服务HTTP”右侧的复选框-->点击确定退出。

在局域网中其它计算机上，打开浏览器，输入 “http://Web服务器的IP地址/”按回车键，就可以访问服务器上的资源。


家里面个人电脑上网用的IP都不是静态的，只要我们重新启动“猫”或者路由器我们的IP就会改变。

动态域名解析器，能获取我们当前电脑的外部IP并把我们设置的域名自动的绑定到这个IP上，无论IP怎样变化，我们的域名都能随时的解析。这样我们就能用我们自己的电脑发布网站了。
