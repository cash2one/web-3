###vm.test.com————配置hosts

###(python redis)[http://www.cnblogs.com/wangtp/p/5636872.html]
- class StrictRedis————实现大部分官方的命令，并使用官方的语法和命令；
    + __init__(self, host='localhost', port=6379, db=0, password=None, ***)
    + get(self, name)————Return the value at key ``name``, or None
    + set(self, name, value, ex=None, px=None, nx=False, xx=False)————将键值对存入redis缓存
        * ex————过期时间（秒）
        * px————过期时间（毫秒）
        * nx————如果设置为True，则只有name不存在时，当前set操作才执行
        * xx————如果设置为True，则只有name存在时，当前set操作才执行
    + setnx(self, name, value)————name不存在时，当前set操作才执行
    + setex(self, name, value, time)————time，过期时间（秒）
    + psetex(self, name, time_ms, value)————time_ms，过期时间（毫秒）
    + getset(self, name, value)————设置新值并获取原来的值
    + getrange(self, key, start, end)————获取子序列（根据字节获取，非字符）
    + setrange(self, name, offset, value)
    + lpop(self, name)————在name对应列表的左侧获取第一个元素并移除，返回第一个元素
    + rpop(self, name)
    + lpush(self, name, *values)———在name对应的list中添加元素到列表的最左边
    + rpush(self, name, *values)
    + sismember(self, name, value)————检查value是否是name对应的集合的成员
    + hset(self, name, key, value)————单个增加或修改hash
- class Redis————StrictRedis的子类，用于向后兼容旧版本的redis-py；
- 连接池————管理对一个redis server的所有连接，避免每次建立、释放连接的开销
    + pool = redis.ConnectionPool(host='***', port=6379)
    + r = redis.Redis(connection_pool=pool)

###pymongo
- class MongoClient————建立连接（client）
    + __init__(self, host=None, port=None, document_class=dict, tz_aware=None, connect=None, **kwargs)
- MongoClient('mongodb://***:27017') 或者 MongoClient('***', 27017)
    + db = client[dbName] 或者 db = client.dbName
        * colls = db.collection_names()
        * coll = db[collectionName]
            - 查询
                + coll.find_one()———————————————————————————————————查询第一条/None
                + coll.find_one({...})——————————————————————————————查询一条/None
            - 更新
                + coll.update_one(filter, update, upsert=False)—————只更新第一个（不能更新_id）
                    * upsert=True————找不到就创建
                + coll.update_many(filter, update, upsert=False)————更新所有
                + replace_one(filter, replacement, upsert=False)
                + find_one_and_update(filter, update, ...)————返回更新前的文档
            - 删除
                + coll.remove()—————————————————————————————————————清空一个集合
                + coll.delete_one(filter)
                + coll.delete_many(filter)
                + coll.drop()
                + coll.find_one_and_delete(filter, projection=None, sort=None, kwargs)
                + coll.find_one_and_replace(filter,...)
            - 插入
                + coll.insert(list)—————————————————————————————————插入
