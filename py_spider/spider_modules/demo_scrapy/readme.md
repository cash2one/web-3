- easy_install lxml-2.3-py2.7-win-amd64.egg
    + (下载)[https://pypi.python.org/pypi/lxml/3.2.3#downloads]
    + (下载)[https://pypi.python.org/pypi/lxml/2.3/]
- pip install twisted；
- pip install pyopenssl；
- (安装 pywin32)[https://sourceforge.net/projects/pywin32/files/pywin32/]
- (下载ActivePerl)[http://www.activestate.com/activeperl/]
- 安装openssl
    + git clone git://git.openssl.org/openssl.git
    + cd c:/openssl-***
    + perl Configure VC-WIN32
- pip install scrapy==1.0

###scrapy
- 进入任意目录，执行：scrapy startproject demo_scrapy
- 创建目录结构如下：
    + demo_scrapy/
        * scrapy.cfg——————————————————————————————项目的配置文件
        * demo_scrapy/————————————————————————————项目的Python目录
            - __init__.py
            - items.py——————————————————定义抓取的数据结构的容器（类字典对象）
            - pipelines.py——————————————对items里面提取的数据做进一步处理（入库、保存等）
            - settings.py———————————————爬虫设置文件
            - spiders/——————————爬虫程序的目录
                + __init__.py


#####scrapy.spiders.Spider
- class Spider(scrapy.utils.trackref.object_ref)
    + __init__(self, name=None, **kwargs)
    + __repr__ = __str__(self)
    + __str__(self)
    + log(self, message, level=10, **kw)
        * Spider.logger.info('msg')
    + make_requests_from_url(self, url)
    + parse(self, response)————默认回调函数（解析url的方法）
        * 为 start_urls 中的每个URL创建了一个 scrapy.http.Request 对象
        * 接收每个Request返回的 scrapy.http.Response 对象作为唯一参数
        * 负责解析response data（response.body————页面内容）
        * 提取数据————生成item
        * 生成需要进一步处理的URL的 Request 对象
    + set_crawler(self, crawler)
    + start_requests(self)
    + Class methods
        * from_crawler(cls, crawler, *args, **kwargs) from __builtin__.type
        * handles_request(cls, request) from __builtin__.type
        * update_settings(cls, settings) from __builtin__.type
    + Static methods
        * close(spider, reason)
    + Data descriptors
        * __dict__
        * __weakref__
        * logger
    + Data and other attributes
        * custom_settings = None
        * name = None
scrapy.selector import Selector