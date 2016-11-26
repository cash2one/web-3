# -*- coding: utf-8 -*-
# @Date:   2016-10-10 11:47:51
# @Last Modified time: 2016-10-10 14:57:12
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

#
# 映射到静态文件的url
#
STATIC_URL = '/static/'
#
# 各个app的static目录及公共的static目录
#
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
#
# 总的static目录
# python manage.py collectstatic————自动收集static文件并复制到STATIC_ROOT
#
STATIC_ROOT = os.path.join(BASE_DIR, "static")
