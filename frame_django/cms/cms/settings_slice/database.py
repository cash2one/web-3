# -*- coding: utf-8 -*-
# @Date:   2016-12-22 21:14:08
# @Last Modified time: 2017-01-02 19:36:18
#
# 数据库配置
import platform

# MIGRATION_MODULES = {}

host = '127.0.0.1'
if platform.system() == "Windows":
    host = "vm.test.com"


'''
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
DATABASES = {
    # django自带的站点管理默认使用default
    # manage.py不加参数生成default数据库的表
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
'''
init_command————是否启用严格模式

STRICT_ALL_TABLES————MySQL返回错误并忽视剩余的行
在这种情况下，前面的行已经被插入或更新————部分更新

STRICT_TRANS_TABLES————将非法值转换为最接近该列的合法值并插入调整后的值
如果值丢失，插入默认值
在任何情况下，MySQL都会生成警告而不是给出错误并继续执行语句
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'manage',
        'USER': 'root',
        'PASSWORD': 'zdd12315',
        'HOST': host,
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    },
    'system': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'system',
        'USER': 'root',
        'PASSWORD': 'zdd12315',
        'HOST': host,
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    },
    # 从数据库
    # 'system_slave': {
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
DATABASE_ROUTERS = ['cms.database_router.DatabaseAppsRouter']
