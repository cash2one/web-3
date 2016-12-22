# -*- coding: utf-8 -*-
# @Date:   2016-12-01 09:29:01
# @Last Modified time: 2016-12-07 15:26:17
#
DATABASE_APPS_MAPPING = {
    'default': 'manage',
    'login': 'login',
}


class DatabaseAppsRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label in DATABASE_APPS_MAPPING:
            return DATABASE_APPS_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in DATABASE_APPS_MAPPING:
            return DATABASE_APPS_MAPPING[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        db_obj1 = DATABASE_APPS_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_APPS_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    def allow_migrate(self, db, app_label, **hints):
        if db in DATABASE_APPS_MAPPING.values():
            return db == DATABASE_APPS_MAPPING.get(app_label)
        elif app_label in DATABASE_APPS_MAPPING:
            return False
        return None
