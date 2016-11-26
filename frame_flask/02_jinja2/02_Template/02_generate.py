# coding:utf-8
'''
<pre > generate(*args, **kwargs) < /pre >
此方法会一段一段的渲染模板，而不是一次性的将整个模板渲染成目标文本。这对产生非常大的模板时非常有用。调用此方法会返回一个产生器(generator)。
'''
from jinja2 import Template


template = Template('Hello {{ name }}')
print template.render(name = '123')
