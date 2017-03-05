# -*- coding: utf-8 -*-
# @Date:   2017-03-02 22:07:59
# @Last Modified time: 2017-03-05 16:03:11
"""
自定义加载器————写一个BaseLoader的子类，并覆盖get_source方法
get_source(environment, template)
load(environment, name, globals=None)
"""

# from jinja2 import FileSystemLoader, PackageLoader, DictLoader, FunctionLoader, PrefixLoader, ChoiceLoader
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
# 加载一个模板。此方法会在缓存中查找模板，如果缓存中不存在则调用get_source得到模板的内容，缓存后返回结果。
