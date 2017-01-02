# -*- coding: utf-8 -*-
# @Date:   2016-12-01 09:29:01
# @Last Modified time: 2017-01-02 21:35:58
#
DATABASE_APPS_MAPPING = {
    'default': 'manage',
    'login': 'login',
}

'''
allow_migrate同步数据库时调用的方法
db————参数 --database="db"
model————要同步的模型
True————可以
False————拒绝
None————不管
'''


class DatabaseAppsRouterTest(object):
    '''通过models里的_database字段判断使用哪个库'''

    def db_for_read(self, model, **hints):
        if hasattr(model, '_database'):
            return model._database
        return 'default'

    def db_for_write(self, model, **hints):
        if hasattr(model, '_database'):
            return model._database
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_syncdb(self, db, model):
        '''旧版'''
        if hasattr(model, '_database'):
            model_db = model._database
        else:
            model_db = 'default'

        if db == model_db:
            return True
        else:
            return False


class DatabaseAppsRouter(object):
    '''
    通过DATABASE_MAPPING字典里的键值对判断使用哪个库
    可以通过指定不同的读写库，实现读写分离
    参考————${django}\db\utils.py
    '''

    def db_for_read(self, model, **hints):
        """"Point all read operations to the specific database."""
        if model._meta.app_label in DATABASE_APPS_MAPPING:
            return DATABASE_APPS_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        if model._meta.app_label in DATABASE_APPS_MAPPING:
            return DATABASE_APPS_MAPPING[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation between apps that use the same database."""
        db_obj1 = DATABASE_APPS_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_APPS_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    def allow_migrate(self, db, app_label, **hints):
        """Make sure that apps only appear in the related database."""
        if db in DATABASE_APPS_MAPPING.values():
            return db == DATABASE_APPS_MAPPING.get(app_label)
        elif app_label in DATABASE_APPS_MAPPING:
            return False
        return None
