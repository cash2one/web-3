# -*- coding: utf-8 -*-
# @Date:   2016-11-28 09:23:51
# @Last Modified time: 2017-03-06 11:42:08
import Cookie
# SimpleCookie(BaseCookie(dict))
c = Cookie.SimpleCookie()
c['key1'] = 'value1'
print c
