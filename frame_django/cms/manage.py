#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date:   2016-12-22 21:14:08
# @Last Modified time: 2017-01-02 21:42:08
import os
import sys

if __name__ == "__main__":
    # 设置项目使用的settings文件
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
