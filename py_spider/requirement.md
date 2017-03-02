###Linux
#####安装pip
- yum -y install epel-release
- yum -y install python-pip

#####安装编译环境
- yum install gcc
- yum install g++
- yum install libxslt-devel
- yum install python-devel

#####安装python多版本
- (pyenv 安装教程)[http://www.cnblogs.com/MacoLee/p/5707546.html]
- pyenv 安装包国内代理，要不安装很慢 export PYTHON_BUILD_MIRROR_URL="http://pyenv.qiniudn.com/pythons/"
- pyenv install 2.7.6
- pyenv version
- pyenv local 2.7.6

#####安装爬虫需要的依赖
- pip install lxml
- pip install requests
- pip install redis
- pip install pymongo
- pip install parsel
- pip install simplejson
- pip install jsonpath_rw