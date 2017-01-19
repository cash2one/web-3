# coding:utf-8
#
# 缓存API
# 访问一个网址时, 尝试从 cache 中找有没有缓存内容
# 如果网页在缓存中显示缓存内容，否则生成访问的页面，保存在缓存中以便下次使用，显示缓存的页面
#
import json
from django.core.cache import cache
from cms import settings

# @cache_page(60 * 15)
# 视图级缓存，设置缓存时间，当超过这个时间，请求会从views里取数据
#
# @vary_on_headers('User‐Agent')
# 根据user-agent的不同缓存页面
#
# @vary_on_cookie==@vary_on_headers('Cookie')
# 根据cookie的不同缓存页面
#
# @cache_control(private=True)
# 控制缓存
#
# 模板碎片缓存
# {% load cache %}{% cache 500 sidebar *args %}...{% endcache %}
# 在给定的时间内缓存了块的内容————参数: 缓存超时时间（s） 缓存片段名称  额外参数
# 缓存超时时间可以作为模板变量


# 获取缓存数据，key唯一
def read_from_cache(key):
    key = key
    value = cache.get(key, None)
    if value is None:
        data = None
    else:
        data = json.loads(value)
    return data


# 存储缓存数据，key唯一，data为存储的数据，60*15为缓存时间，会更新已经存在的键值
def write_to_cache(key, data):
    # key = 'user_id_of_' + user_id
    key = key
    cache.set(key, json.dumps(data), settings.NEVER_REDIS_TIMEOUT)

# cache.add(key, data, timeout)————新增键值对，不会更新已经存在的键值
# cache.delete(key)
# cache.incr()/cache.decr()————增加、减少已经存在的键值，默认情况下，增加或减少的值是1
# cache.get_many(['a', 'b', 'c'])————获取多个（未超时的）缓存数据
