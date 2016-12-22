# -*- coding: utf-8 -*-
# @Date:   2016-11-29 10:59:22
# @Last Modified time: 2016-12-09 11:09:32
#
import os
import platform
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
# MIGRATION_MODULES = {}
#
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# 数据库配置
host = '127.0.0.1'
if platform.system() == "Windows":
    host = "vm.test.com"

DATABASES = {
    # django自带的站点管理默认使用default
    # manage.py不加参数生成default数据库的表
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
    # app名称
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'manage',  # 数据库名称
        'USER': 'root',
        'PASSWORD': 'zdd12315',
        'HOST': host,
        'PORT': '3306',
        'OPTIONS': {
            # 是否启用严格模式
            #
            # STRICT_ALL_TABLES
            # MySQL返回错误并忽视剩余的行
            # 在这种情况下，前面的行已经被插入或更新————部分更新
            #
            # STRICT_TRANS_TABLES
            # 将非法值转换为最接近该列的合法值并插入调整后的值
            # 如果值丢失，插入默认值
            # 在任何情况下，MySQL都会生成警告而不是给出错误并继续执行语句
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    },
    'base': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'base',
        'USER': 'root',
        'PASSWORD': 'zdd12315',
        'HOST': host,
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    },
    # 主数据库
    'forward': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'forward',
        'USER': 'root',
        'PASSWORD': 'zdd12315',
        'HOST': host,
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    },
    # 从数据库
    # 'forward_slave': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'forward_slave',
    #     'USER': 'root',
    #     'PASSWORD': 'zdd12315',
    #     'HOST': host, # 另一个地址
    #     'PORT': '3306',
    #     'OPTIONS': {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    #     }
    # }
}


# 指定要使用的路由，可以多个，依次查找
DATABASE_ROUTERS = ['azure.database_router.DatabaseAppsRouter']
