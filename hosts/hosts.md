###网址与IP
每一个网站都有一个网址，每一个网址都对应着一个IP地址。IP地址才是网站的真正地址，我们访问一个网站，必须知道它的IP地址才行。

###DNS解析
我们输入网址以后，并不是直接通过网址去连你的网站，而是通过`DNS服务器（domain name server）`，将网址还原成真实的IP地址，再通过IP地址，去连接你要访问的网站。

*著名的DNS服务器有Google Public DNS和OpenDNS。*

###DNS劫持和DNS污染
`网址与IP地址`的对应方式一旦改变了，或者被某种方式切断了，我们就无法通过网址得到真实的IP从而访问网站。

这是某些网站上不了的原因之一，专业术语叫做DNS劫持和DNS污染。这个时候，我们就要人为地去建立这种对应关系。

###hosts文件————一个记录`网址与IP地址`对应关系的文件
优先使用hosts文件中记录的对应关系，如果hosts没有，才去寻找DNS服务器。
当你要上某个网站，如twitter的时候，系统会先查hosts文件，如果里面有twitter对应的IP地址，它则会主动去连这个IP，这个时候，不管是DNS劫持和DNS污染，对你上网都是没有影响的。

所以，我们只要能在hosts里面，建立起这种正确的对应关系，就可以避开DNS引起的问题。

###修改hosts文件

|    系统   |             hosts文件位置             |            修改后生效的方法           |
|-----------|---------------------------------------|---------------------------------------|
| Windows   | C:\Windows\System32\drivers\etc\hosts | ipconfig /flushdns                    |
| Android   | /system/etc/hosts                     | 开启飞行模式 -> 关闭飞行模式          |
| Mac & iOS | /etc/hosts                            | sudo killall -HUP mDNSResponder       |
| Linux     | /etc/hosts                            | sudo rcnscd restart                   |
|           | systemd发行版                         | sudo systemctl restart NetworkManager |

通用生效方法：拔网线(断网) -> 插网线(重新连接网络)

[老D博客永久更新地址](http://laod.cn/hosts/2016-google-hosts.html)