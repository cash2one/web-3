# -*- coding: utf-8 -*-
# @Date:   2016-12-25 23:03:33
# @Last Modified time: 2016-12-25 23:06:27
#
import platform

location = '127.0.0.1:6379'
if platform.system() == "Windows":
    location = 'vm.test.com:6379'

BACKENDS = [
    'django.core.cache.backends.locmem.LocMemCache',        # 默认，本地内存缓存
    'django.core.cache.backends.memcached.MemcachedCache',  # Memcached缓存，LOCATION可指定[多个服务器]
    'django.core.cache.backends.db.DatabaseCache',          # 数据库缓存，LOCATION指定表名
    'django.core.cache.backends.filebased.FileBasedCache',  # 文件系统缓存，LOCATION指定文件名
    'django.core.cache.backends.dummy.DummyCache',          # 虚拟缓存，只是实现缓存的接口
    'django_redis.cache.RedisCache',                        # redis缓存，pip install django-redis
]

CACHES = {
    'default': {
        'BACKEND': BACKENDS[-1],
        # 'TIMEOUT': 60,
        'LOCATION': location,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}
CACHE_MIDDLEWARE_KEY_PREFIX = ''    # 当多个站点使用同一个配置的时候，避免发生冲突
CACHE_MIDDLEWARE_SECONDS = 600      # 每个页面应该被缓存的秒数
CACHE_MIDDLEWARE_ALIAS = 'default'  # 用来存储的缓存别名

REDIS_TIMEOUT = 7 * 24 * 60 * 60
CUBES_REDIS_TIMEOUT = 60 * 60
NEVER_REDIS_TIMEOUT = 365 * 24 * 60 * 60

"""
from django.conf import settings
from django.core.cache import cache
#read cache user id
def read_from_cache(self, user_name):
    key = 'user_id_of_'+user_name
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data = json.loads(value)
    return data
#write cache user id
def write_to_cache(self, user_name):
    key = 'user_id_of_'+user_name
    cache.set(key, json.dumps(user_name), settings.NEVER_REDIS_TIMEOUT)
"""