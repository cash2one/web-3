# -*- coding: utf-8 -*-
# @Date:   2016-10-11 15:12:24
# @Last Modified time: 2016-11-29 09:53:33
# django中获取当前时间不要用datetime.today()，要用timezone.now()
from django.utils import timezone
# print timezone.localtime(timezone)
