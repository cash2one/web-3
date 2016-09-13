# coding:utf-8
'''
Environment是Jinja2中的一个核心类，它的实例用来保存配置、全局对象，以及从本地文件系统或其它位置加载模板。
多数应用会在初始化时创建Environment实例，然后用它来加载模板。当然，如果系统有必要使用不同的配置，也可以创建多个 Environment实例一起使用。
'''

# 配置Jinja2为你的应用加载模板的最简单的方式：

from jinja2 import Environment, PackageLoader
import sys
sys.path.append('.')

env = Environment(loader=PackageLoader('myapp', 'templates'))  # loader模板加载器

'''
上述代码使用缺省配置创建了一个Environment实例，并指定PackageLoader作为模板加载器。PackageLoader可以 从你的python应用程序的包中读取并加载模板。
'''

# 调用get_template()方法从这个环境中加载模板，并会返回已加载的Template：
template = env.get_template('mytemplate.html')

# 用render方法来渲染模板:
print template.render(the='variables', go='here')
