# -*- coding: utf-8 -*-
# @Date:   2016-12-01 09:29:01
# @Last Modified time: 2016-12-07 15:26:17

DATABASE_APPS_MAPPING = {
    #'app_name':'database_name',
    'default': 'manage',
    'base': 'base',
    'forward': 'forward',
}


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
        if hasattr(model, '_database'):
            model_db = model._database
        else:
            model_db = 'default'

        if db == model_db:
            return True
        else:
            return False


DATABASE_MAPPING = DATABASE_APPS_MAPPING


class DatabaseAppsRouter(object):
    '''
    通过DATABASE_MAPPING字典里的键值对判断使用哪个库
    可以通过指定不同的读写库，实现读写分离
    '''
    '''参考————${django}\db\utils.py'''

    def db_for_read(self, model, **hints):
        """"Point all read operations to the specific database."""
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation between apps that use the same database."""
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    # allow_syncdb(self, db, model)————旧版
    # 在同步数据库时调用
    # db就是参数 --database="db"
    # model就是要同步的模型，返回True就是可以，False就是拒绝，None是不管
    def allow_migrate(self, db, app_label, **hints):
        """Make sure that apps only appear in the related database."""

        if db in DATABASE_MAPPING.values():
            return db == DATABASE_MAPPING.get(app_label)
        elif app_label in DATABASE_MAPPING:
            return False
        return None
