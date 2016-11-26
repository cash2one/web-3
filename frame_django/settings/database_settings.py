# -*- coding: utf-8 -*-
# @Date:   2016-10-10 11:45:16
# @Last Modified time: 2016-10-10 12:04:24
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#
# 数据库配置
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'mysql': {
        'ENGINE': 'mysql',
        'NAME': 'projectforge',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
