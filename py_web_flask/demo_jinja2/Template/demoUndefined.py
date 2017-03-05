# -*- coding: utf-8 -*-
# @Date:   2017-03-02 22:07:59
# @Last Modified time: 2017-03-05 14:44:48
'''
class Environment
__init__(self, ... undefined=<class 'jinja2.runtime.Undefined'>, ...)
Environment的构建器指定undefined参数（undefined types中的任意一个，或者Undeﬁned及其子类）
当模板引擎无法找到一个名称或者属性时，undefined会决定哪些操作可以正常进行，哪些不可以。
'''
from jinja2 import Undefined, DebugUndefined, StrictUndefined
from jinja2.exceptions import UndefinedError
'''
class Undefined(hint=None, obj=None, name=None)————缺省undefined类型
可以打印或者作为sequence迭代，但是不能做其它操作，否则会抛出UndefinedError。
'''
foo = Undefined(name='foo')
print str(foo)
print not foo
try:
    print foo + 'test'
except UndefinedError as e:
    print e
print("-" * 20)
'''
class DebugUndefined(hint=None, obj=None, name=None)
'''
foo = DebugUndefined(name='foo')
print str(foo)
print not foo
try:
    print foo + 'test'
except UndefinedError as e:
    print e
print("-" * 20)
'''
class StrictUndefined(hint=None, obj=None, name=None)
'''
foo = StrictUndefined(name='foo')
try:
    print str(foo)
    # print not foo
    # print foo + 'test'
except UndefinedError as e:
    print e
