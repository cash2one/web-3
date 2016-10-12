####安装 NodeJS环境
1. [NodeJS官网](http://www.nodejs.org/)下载；
2. 安装，设置环境变量（安装程序会自动设置）
3. node -v返回node版本号，检验安装是否正常；

####下载并安装LivePool
*LivePool 基于 NodeJS，类似 Fiddler 支持抓包和本地替换的 Web 开发调试工具*
[LivePool项目Git地址](https://github.com/rehorn/livepool)
[Zip格式下载地址](https://github.com/rehorn/livepool/zipball/master)

将Zip文件解压到任意目录，使用快捷键Ctrl+Shift+鼠标右键该目录下空白处，在弹出的菜单中在此处打开命令窗口，键入命令：npm install livepool -g
此时开始livepool的全局安装。

3、livepool安装结束后，在命令窗口下键入：livepool
回车后运行livepool
运行livepool成功后会给出两个端口号：
       上面的8090是一个代理端口号，下面的8002是一个livepool WEB UI 界面端口两个访问地址都是127.0.0.1或者输入localhost也可以。