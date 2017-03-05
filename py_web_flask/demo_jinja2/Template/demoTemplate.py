# -*- coding: utf-8 -*-
# @Date:   2017-03-02 22:07:59
# @Last Modified time: 2017-03-05 08:50:13
from jinja2 import Template
template = Template('Hello {{ name }}!')
'''
render(*args, **kwargs)
接受dict或关键字参数，传递给模板，即模板“上下文”
'''
print template.render(name='World')
print template.render({'name': 'that say nih'})
print
'''
generate(*args, **kwargs)
返回一个生成器(generator)————一段一段地渲染模板，而不是一次性地渲染整个模板
这对产生非常大的模板时非常有用
'''
print template.generate(name='generate')
print
'''
stream(*args, **kwargs)
与generate功能类似，只不过此方法返回一个TemplateStream module
此方法用来在模板运行时导入，也可以用来在python代码中访问导出的模板变量
'''
print template.stream(name='stream')
print

t = Template('{% macro foo() %}42{% endmacro %}23')
print unicode(t.module)
print t.module.foo()
