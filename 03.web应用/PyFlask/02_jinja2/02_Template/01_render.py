# encoding:utf-8
'''
Template类可以被看作是一个编译过的模板文件，被用来产生目标文本.

Template类的构建器参数和Environment类基本相同, 区别是，创建Template实例需要一个模板文本参数，另外它不需要loader参数。
Template实例是一个不可变对象，即你不能修改Template实例的属性。

一般情况下，我们会使用Environment实例来创建Template，但也可以直接使用Template构建器来创建。如果要用构建器来创 建Template实例，那么Jinja会根据构建器参数自动为此Template创建/指派一个内部Environment实例，凡是使用相同构建器参 数(不包括模板文本串参数)创建的Template实例都会共享同一个内部Environment实例。 
'''

from jinja2 import Template

'''
方法：<pre>render(*args, **kwargs)</pre> 
此方法接受与“dict”相同的构建器参数：一个dict的子类，或者一些关键字参数。
'''

template = Template('Hello {{ name }}!')
print template.render(name='World')
template = Template('{{ knights }}!')
print template.render({'knights': 'that say nih'})
'''
通过创建一个Template的实例，你会得到一个新的模板对象，提供一个名为render()的方法，该方法在有字典或关键字参数时调用扩充模板。字典或关键字参数会被传递到模板，即模板“上下文”。
'''
