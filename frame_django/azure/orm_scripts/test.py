# -*- coding: utf-8 -*-
# @Date:   2016-12-11 22:27:00
# @Last Modified time: 2016-12-11 23:01:02

import os
import sys
import django

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 把manage.py所在目录添加到系统目录
sys.path.append(BASE_DIR)
# 指定settings————参考manage.py
# 不在django标准目录里，没有经过manage.py启动的文件，无法自动使用settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "azure.settings")
# 启动django
django.setup()

from base.models import DownLoad

d = DownLoad.objects.all()
for i in d:
    print i.file_name
