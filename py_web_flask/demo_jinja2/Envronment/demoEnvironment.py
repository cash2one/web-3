# -*- coding: utf-8 -*-
# @Date:   2017-03-02 22:07:59
# @Last Modified time: 2017-03-05 08:37:51
from jinja2 import Environment, PackageLoader
import sys
sys.path.append('.')

'''
使用缺省配置创建一个Environment实例
指定PackageLoader作为模板加载器
PackageLoader可以从python应用程序的包中读取并加载模板
'''
env = Environment(loader=PackageLoader('app', 'templates'))

env1 = Environment(
    block_start_string="<#", block_end_string="#>",
    variable_start_string="${", variable_end_string="}",
    comment_start_string="<#--", comment_end_string="--#>",
    loader=PackageLoader('app', 'templates'))

"""
调用get_template()方法从环境中加载模板，并会返回已加载的Template
"""
template = env.get_template('demo.html')
template1 = env1.get_template('demo.html')

"""
用render方法来渲染模板
"""
print template.render(the='variables', go='here')
print("-" * 20)
print template1.render(the='variables', go='here')
