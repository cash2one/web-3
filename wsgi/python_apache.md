###[下载mod_wsgi](http://www.lfd.uci.edu/~gohlke/pythonlibs/#mod_wsgi)
解压（.whl包），把里面的mod_wsgi.so拷贝到Apache路径\modules下。

或者

###[下载源代码](https://github.com/GrahamDumpleton/mod_wsgi/releases)自己编译
下载解压后，在win32目录下找到与自己的python和apache服务器版本对应（或相近）的.mk文件，用记事本打开，将其中的APACHE_ROOTDIR和PYTHON_ROOTDIR修改为自己的apache和python的根目录。

###设置环境变量（path、include、lib）
在cmd窗口中输入:
```
set path =
	C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\bin;
	C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin;
	C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7;
set include = C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include;
set lib = C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\lib;
```
设置好环境变量，然后输入：nmake -f ap24py34-win32-VC10.mk install，就开始进行编译了。

*include <C:\Python27\include\Python.h>*
