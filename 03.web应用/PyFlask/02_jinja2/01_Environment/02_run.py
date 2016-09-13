# coding:utf-8
'''
Environment核心类
class Environment(block_start_string='{%', block_end_string='%}',
                  variable_start_string='{{', vari - able_end_string='}}',
                  comment_start_string='{#', comment_end_string='#}',
                  line_statement_preix=None,
                  trim_blocks=False,
                  extensions=(),
                  optimized=True,
                  undefined= < class 'Jinja2.runtime.Undefined' > ,
                  finalize=None,
                  autoescape=False,
                  auto_reload=True,
                  loader=None)

block_start_string 块开始标记符，缺省是 '{%'. 
block_end_string 块结束标记符，缺省是 '%}'. 
variable_start_string 变量开始标记符，缺省是 '{{'. 
variable_start_string 变量结束标记符，缺省是 '}}'. 
comment_start_string 注释开始标记符，缺省是 '{#'. 
comment_end_string 注释结束标记符，缺省是 '#}'. 
auto_reload如果设为True，Jinja会在使用Template时检查模板文件的状态，如果模板有修改， 则重新加载模板。如果对性能要求较高，可以将此值设为False。 
autoescape XML/HTML自动转义，缺省为false. 就是在渲染模板时自动把变量中的<>&等字符转换为&lt;&gt;&amp;。
cache_size
    缓存大小，缺省为50，即如果加载超过50个模板，那么则保留最近使用过多50个模板，其它会被删除。如果换成大小设为0，那么所有模板都会在使用时被重 编译。如果不希望清除缓存，可以将此值设为-1。
undefined Undefined或者其子类，用来表现模板中未定义的值。
line_statement_prefix 指定行级语句的前缀。
extensions Jinja的扩展的列表，可以为导入到路径字符串或者表达式类 。
'''

from jinja2 import Environment, PackageLoader
import sys
sys.path.append('.')

env = Environment(
    block_start_string="<#", block_end_string="#>",
    variable_start_string="${", variable_end_string="}",
    comment_start_string="<#--", comment_end_string="--#>",
    loader=PackageLoader('myapp', 'templates'))

template = env.get_template('mytemplate.html')

print template.render(the='variables', go='here')
