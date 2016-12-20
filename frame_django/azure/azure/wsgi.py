# -*- coding: utf-8 -*-
# @Date:   2016-11-28 11:03:52
# @Last Modified time: 2016-11-29 11:35:24
"""
WSGI config for azure project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 设置项目使用的settings文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "azure.settings")

application = get_wsgi_application()
