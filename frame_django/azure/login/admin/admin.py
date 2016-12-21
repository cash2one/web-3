# -*- coding: utf-8 -*-
# @Date:   2016-12-10 22:05:10
# @Last Modified time: 2016-12-10 22:05:30

from django.contrib import admin


from login.models.models import *


class UserAdmin(admin.ModelAdmin):
    # 以表格显示出字段（覆盖__unicode__）
    list_display = ('id', 'name', 'phone', 'sex', 'email', 'create_at')
    # 添加一个快速查询栏
    search_fields = ('id', 'name')
    # 用字段元组创建过滤器————为日期型字段提供了快捷过滤方式————今天、过往七天、本月和今年
    list_filter = ('create_at',)
    pass
# 将模块注册到管理工具中————第二个参数有默认选项————可以不指定
admin.site.register(SimpleUser, UserAdmin)


class UserLoginLogAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserLoginLog, UserLoginLogAdmin)


class DownLoadAdmin(admin.ModelAdmin):
    pass
admin.site.register(DownLoad, DownLoadAdmin)
