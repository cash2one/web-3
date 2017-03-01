（一）fiddler简介：
Edit，复制信息，移除捕获（Del、Ctrl+X），标识颜色，解除编辑锁定(F2)，查找会话
Rules，隐藏捕获，为所有Request/Response加断点，编辑规则(CustomRules.js)，取消编码
Tool，设置，清缓存，编码工具(TextWizard)
View：界面视图切换

监听开关 -- 左下角capturing（表示捕捉状态，快捷键F12），用的时候就开着，不用就让丫休息。
监听类型 -- 四种状态：
	监听所有请求（All Processes）；
	监听浏览器请求（Web Brosers）；
	监听非浏览器请求（Nob-Broser）；
	全部隐藏(Hide All)；

命令行 -- 监听开关上方
help：打开官方的使用介绍页面，所有的命令都会列出来；
cls：(=ctrl+x=清屏)；
select：选择会话；
?.js：用来选择js文件；
bpu：暂停指定的request(bpu www.kk.com/action/add, bpu无参时取消断点)
bpafter：暂停指定的response(bpafter www.kk.com/action/add, bpafter无参时取消断点)

请求列表（左边栏）包含的信息：
	结果（Result），协议（Protocol），主机名（Host），
	网页地址（URL），内容大小（Body），缓存（Caching），
	响应的HTTP内容类型（Content-Type），
	请求所运行的程序（Process），注释（Comments），自定义（Custom），

请求相关信息（右边这一大片）
数据流的相关信息的查看器，这些查看器提供很多查看形式，可以查看数据流的内容。
	统计选中的一个或多个请求相关数据，大小、耗时（Statistics）
	强大的检查器，多种方式查看Request或者Response的详细消息（Inspectors）
	自动回复器，设置一些规则将符合规则的请求指向本地（AutoResponder）
	创建发送HTTP请求（Composer）
	日志信息（log）
	设置会话过滤规则（Filters）
	网络请求时间轴（Timeline）

【注意】某些土鳖中文网站没有在 HEADER 中指定字符集，POST请求中的中文参数不能被Fiddler正确处理。
具体表现是：
这些网站是用GB2312/GBK/GB18030编码的，在Fiddler Inspector的TextView 中显示为“����”，到了WebForms中就显示为乱码了，因为Fiddler把它们按照UTF-8解码。反过来，在WebForms中将参数设置为中文值，会被Fiddler用UTF-8编码发送出去导致错误。
【解决】打开注册表编辑器，找到HKCU\Software\Microsoft\Fiddler2\，在里面添加一个字符串值，名叫HeaderEncoding，值设置为默认编码，建议设成GB18030。重启Fiddler。

（1）打开Fiddler 捕捉一个博客园登录的Request 然后分析下它的结构, 在Inspectors tab下以Raw的方式可以看到完整的Request的消息，


（2）我们用Fiddler 捕捉一个博客园首页的Response然后分析下它的结构, 在Inspectors tab下以Raw的方式可以看到完整的Response的消息
