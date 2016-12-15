# -*- coding: utf-8 -*-
# @Date:   2016-12-12 23:22:19
# @Last Modified time: 2016-12-15 13:50:57


class A(object):
    a = 1
    b = 10

    def __init__(self):
        print self.a + self.b


class B(A):
    a = 3

b = B()

# Mixin原理————通过继承时修改默认参数，实现父类的功能
