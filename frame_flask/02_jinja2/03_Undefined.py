# coding:utf-8
'''
Undeﬁned Types 未定义类型。
Undeﬁned及其子类类被用来作为未定义类型。
Environment的构建器可以指定undefined参数，它可以是undefined types中的任意一个，或者是Undefined的子类。当模板引擎无法找到一个名称或者一个属性时，使用的Undefined会决定哪些操作可以正常 进行，哪些不可以。

UndefinedError:
Traceback (most recent call last):
...
Jinja2.exceptions.UndefinedError: 'foo' is undefined 
'''
#(1)
from jinja2 import Undefined
'''
class Undefined(hint=None, obj=None, name=None)
缺省undefined类型。此未定义类型可以打印或者作为sequence迭代。但是不能做其它操作，否则会抛出UndefinedError。
'''
foo = Undefined(name='foo')
print str(foo)
print not foo
# print foo + 42  # UndefinedError
print
#(2)
from jinja2 import DebugUndefined
'''class DebugUndefined(hint=None, obj=None, name=None)'''
foo = DebugUndefined(name='foo')
print str(foo)
print not foo
# print foo + 42#UndefinedError
print
#(3)
from jinja2 import StrictUndefined
'''class StrictUndefined(hint=None, obj=None, name=None)'''
foo = StrictUndefined(name='foo')
# print str(foo) # UndefinedError
# print not foo # UndefinedError
# print foo + 42  # UndefinedError
