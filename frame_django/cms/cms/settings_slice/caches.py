# -*- coding: utf-8 -*-
# @Date:   2016-12-25 23:03:33
# @Last Modified time: 2016-12-25 23:06:27
#
# 使用redis缓存服务器
# pip install django-redis
import platform
# The cache backends to use.
location = '127.0.0.1:6379'
if platform.system() == "Windows":
    location = 'vm.test.com:6379'
CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    # }
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
        },
    },
}
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_ALIAS = 'default'

REDIS_TIMEOUT = 7 * 24 * 60 * 60
CUBES_REDIS_TIMEOUT = 60 * 60
NEVER_REDIS_TIMEOUT = 365 * 24 * 60 * 60
