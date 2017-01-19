# -*- coding: utf-8 -*-
# @Date:   2016-12-25 23:03:33
# @Last Modified time: 2016-12-25 23:06:27
#
import platform
from django.contrib.sessions.backends import cached_db
from django_redis.cache import RedisCache

location = '127.0.0.1:6379'
if platform.system() == "Windows":
    location = 'vm.test.com:6379'

BACKENDS = [
    'django.core.cache.backends.locmem.LocMemCache',        # 默认，本地内存缓存        LOCATION: 'locmem:///'
    'django.core.cache.backends.memcached.MemcachedCache',  # Memcached缓存           LOCATION: [（多个）服务器]
    'django.core.cache.backends.db.DatabaseCache',          # 数据库缓存               LOCATION: 'db://cache_table'
                                                            # python manage.py createcachetable [cache_table_name]
    'django.core.cache.backends.filebased.FileBasedCache',  # 文件缓存                 LOCATION: 'file://../.../cache_file'
    'django.core.cache.backends.dummy.DummyCache',          # 虚拟缓存（实现缓存的接口） LOCATION: 'dummy:///'
    'django_redis.cache.RedisCache',                        # redis缓存 pip install django-redis
]

CACHES = {
    'default': {
        'BACKEND': BACKENDS[-1],                                           # 缓存后端类（可以自己实现）
        'TIMEOUT': 600,                                                    # 缓存过期时间（s），None永不过期，0立即过期，默认300
        'MAX_ENTRIES': 300,                                                # 内存、文件、数据缓存最大条数，超出将删除旧值，默认300
        'LOCATION': location,
        # 达到MAX_ENTRIES时，被删除的条目比率（1/cull_percentage）
        # 设为2，删除一半
        # 设为0，清空缓存————以丢失大量缓存为代价，大大提高访问速度
        # 'CULL_PERCENTAGE': 1,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "PICKLE_VERSION": -1,                                        # pickle版本，默认使用最新的
            "SOCKET_CONNECT_TIMEOUT": 5,                                   # socket 建立连接超时设置
            "SOCKET_TIMEOUT": 5,                                           # 连接建立后的读写操作超时设置
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",  # 支持压缩, 默认关闭
            "IGNORE_EXCEPTIONS": True,                                     # 关闭时，忽略连接异常
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},            # 连接池的最大连接数量
        },
    },
}
CACHE_MIDDLEWARE_KEY_PREFIX = ''    # 当多个站点使用同一个配置的时候，避免发生冲突
CACHE_MIDDLEWARE_SECONDS = 600      # 每个页面应该被缓存的秒数
CACHE_MIDDLEWARE_ALIAS = 'default'  # 用来存储的缓存别名

REDIS_TIMEOUT = 7 * 24 * 60 * 60
CUBES_REDIS_TIMEOUT = 60 * 60
NEVER_REDIS_TIMEOUT = 365 * 24 * 60 * 60

#
# session————会话
#
SESSION_ENGINES = [
    'django.contrib.sessions.backends.cached_db',      # 数据库+缓存
    'django.contrib.sessions.backends.cache',          # 使用缓存
    'django.contrib.sessions.backends.db',             # 默认使用数据库
                                                       # django.contrib.sessions.models，一个标准模型
                                                       # 通过migrate建表————django_session，在需要的时候才会读取
                                                       # 可以使用Django数据库API来存取session
    'django.contrib.sessions.backends.file',           # 文件
    'django.contrib.sessions.backends.signed_cookies'  # 基于Cookie的会话(数据存储使用Django加密签名工具和SECRET_KEY设置)
]
SESSION_ENGINE = SESSION_ENGINES[0]          # session后端存储方式
SESSION_CACHE_ALIAS = 'default'              # 缓存别名
SESSION_EXPIRE_AT_BROWSER_CLOSE = True       # cookie超时设置（默认False，使用SESSION_COOKIE_AGE设置；True，浏览器关闭时，使cookie失效
SESSION_COOKIE_DOMAIN = None                 # 使用session cookies的站点（默认None，用于单个站点）
                                             # 设成字符串（".example.com"）————用于跨站（cross-domain）的cookie
SESSION_COOKIE_NAME = "personal_session_id"  # 会话的cookie名，客户端用来识别session，服务器端的session_key，django_session表的主键
SESSION_COOKIE_SECURE = False                # 是否在session中使用安全cookie（只通过HTTPS来安全传输）
SESSION_FILE_PATH = None                     # session存储文件路径
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2    # session cookie在用户浏览器中保持时间————默认两周
SESSION_SAVE_EVERY_REQUEST = False           # 是否每次请求都保存session，默认为False（需要的时候才送出cookie）
#
# session的序列化（默认使用pickle内建模块）————Session字典接受任何支持序列化的Python对象
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
'''
每个session都由一个随机的32字节哈希串来标识，并存储于cookie中

cookie数据存放在客户的浏览器上，不安全
session数据放在服务器上，当访问增多，会比较占用服务器的性能

单个cookie保存的数据不能超过4K，很多浏览器都限制一个站点最多保存20个cookie

通过 Referer header进行session ID窃听（URL中的会话ID编码）可以实施对网站攻击

Django session 框架完全而且只能基于cookie————自动生成一段字符串（cookie）发送到客户端的浏览器，同时把字符串当做key放在session里，在对应的value里设置任意值
'''
#
# 密码哈希算法种子————一个随机字符串，越长越好
SECRET_KEY = '6a8w1=^^n-sj0=n$%gsj@=kk%#bg(943vnt1_vq3@ylhofrp%^'
