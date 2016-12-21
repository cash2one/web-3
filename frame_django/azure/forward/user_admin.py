# -*- coding: utf-8 -*-
# @Date:   2016-12-12 10:23:14
# @Last Modified time: 2016-12-12 10:23:47
#
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from model import UserProfile
from django.contrib.auth.models import User


class UserProfileLine(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfileLine'


class UserAdmin(UserAdmin):
    inlines = (UserProfileLine, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)