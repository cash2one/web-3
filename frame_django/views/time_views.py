# -*- coding: utf-8 -*-
# @Date:   2016-10-12 11:52:08
# @Last Modified time: 2016-11-29 14:00:47

# django中获取当前时间不要用datetime.today()，要用timezone.now()
from django.utils import timezone
# print timezone.localtime(timezone)


def month_archive(request, year='2006', month='03'):
    return 'success'
