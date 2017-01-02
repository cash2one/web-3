# -*- coding: utf-8 -*-
# @Date:   2016-12-22 21:14:08
# @Last Modified time: 2017-01-02 21:40:42
"""
WSGI config for cms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 设置项目使用的settings文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")

application = get_wsgi_application()
