# coding:utf-8
'''
加载器负责从某些位置（比如本地文件系统）中查找并加载模板，并维护在内存中的被编译过的模块。
'''

'''
(1)文件系统加载器，它可以从本地文件系统中查找并加载模板:
class FileSystemLoader(searchpath, encoding='utf-8', cache_size=50, auto_reload=True)
第一个参数searchpath是查找路径，它可以是一个路径字符串，也可以是保护多个路径的sequence。
'''
from jinja2 import FileSystemLoader
# help(FileSystemLoader)
# loader = FileSystemLoader('/path/to/templates')
# loader = FileSystemLoader(['/path/to/templates', '/other/path'])

'''
(2)包加载器。它可以从python包中加载模板:
class PackageLoader(package_name, package_path='templates', encoding='utf-8', cache_size=50, auto_reload=True)
'''
from jinja2 import PackageLoader
# help(PackageLoader)
# loader = PackageLoader('mypackage', 'views')

'''
(3)字典加载器。在mapping参数中明确指定模板文件名的路径。它用来做单元测试比较有用:
class DictLoader(mapping, cache_size=50, auto_reload=False)
'''
from jinja2 import DictLoader
# help(DictLoader)
# loader = DictLoader({'index.html': 'source here'})

'''
(4)函数加载器。让指定的函数来返回模板文件的路径:
class FunctionLoader(load_func, cache_size=50, auto_reload=True)
'''
from jinja2 import FunctionLoader
# help(FunctionLoader)
# loader = FunctionLoader(load_template)

# def load_template(name):
#     if name == 'index.html':
#         return '...'

'''
(5)前缀加载。如果你的工程中包含很多应用，那么多应用之间模板名称就可能存在命名冲突的问题。使用前缀加载器可以有效的解决不同应用之间模板命名冲突问题:
class PrefixLoader(mapping, delimiter='/', cache_size=50, auto_reload=True)
'''
from jinja2 import PrefixLoader
# help(PrefixLoader)
# loader = PrefixLoader({
# 	'app1': PackageLoader('mypackage.app1'),
# 	'app2': PackageLoader('mypackage.app2')
# 	})

# 如此，如果要使用app1中的模板，可以get_template('app1/xxx.html'),
# 使用app2的模板，可以使用get_template('app2/xxx.html')。delimiter字符决定前缀和模板名称之间的分隔符，默认为'/'。

'''
(6)选择加载器，与PrefixLoader类似，可以组合多个加载器。当它在一个子加载器中查找不到模板时，它会在下一个子加载器中继续查找。如果你要用一个不同的位置覆盖内建模板时非常有用:
class ChoiceLoader(loaders, cache_size=50, auto_reload=True)
'''
from jinja2 import ChoiceLoader
# help(ChoiceLoader)
# loader = ChoiceLoader([
#     FileSystemLoader('/path/to/user/templates'),
#     PackageLoader('myapplication')
#     ])

'''
【注意】所有加载都继承自BaseLoader，如果你要实现一个自定义加载可以，可以写一个BaseLoader的子类，并覆盖get_source方法:
class BaseLoader(cache_size=50, auto_reload=True)
BaseLoader已经实现了load方法，它对模板的缓存进行了处理。如果你不需要自己维护缓存，则不必重写此方法。
'''

from jinja2 import BaseLoader, TemplateNotFound
from os.path import join, exists, getmtime


class MyLoader(BaseLoader):

    def __init__(self, path, cache_size=50, auto_reload=True):
        BaseLoader.__init__(self, cache_size, auto_reload)
        self.path = path

    def get_source(self, environment, template):
        path = join(self.path, template)
        if not exists(path):
            raise TemplateNotFound(template)
            mtime = getmtime(path)
            with file(path) as f:
                source = f.read().decode('utf-8')
                return source, path, lambda: mtime != getmtime(path)
'''
get_source(environment, template)
load(environment, name, globals=None)
'''
# 加载一个模板。此方法会在缓存中查找模板，如果缓存中不存在则调用get_source得到模板的内容，缓存后返回结果。
