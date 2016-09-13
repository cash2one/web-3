# coding:utf-8
'''
<pre > stream(*args, **kwargs) < /pre >
与generate功能类似，只不过此方法返回一个TemplateStream module
此方法用来在模板运行时导入, 也可以用来在python代码中访问导出的模板变量。
'''
from jinja2 import Template

t = Template('{% macro foo() %}42{% endmacro %}23')

print unicode(t.module)

print t.module.foo()
