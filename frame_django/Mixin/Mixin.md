###generic view————通用视图
- function-based-view（fbv）————基于函数的视图（django1.3之前）
- class-based-view（cbv）————基于类的视图

###django类视图
- 更能体现python的面向对象
- class更能利用多态，更容易从宏观上将项目内通用的功能抽象出来
- 基于类的通用视图（以及任何继承了Django提供的基础类的基于类的视图）都能够以下面两种方式被配置：
    + 子类化
    + 直接通过URLconf来传递参数

#####利用多态
cbv里引入了mixin的概念。Mixin就是写好了的一些基础类，然后通过不同的Mixin组合成为最终想要的类。

Django把基本的http请求和响应抽象出来，封装成各自的类。cbv的实现原理，大体就是由url路由到这个cbv之后，通过cbv内部的dispatch方法进行分发，将get请求分发给cbv.get方法处理，将post请求分发给cbv.post方法处理，其他方法类似。

在使用过程中只需把各个基类聚合到一起使用, 并按照自己的要求重写自己需要的方法就可以了，这些基类叫Mixin。

#####Mixin————提供数据、加载模板
|          类名         |                        功能                        |
|-----------------------|----------------------------------------------------|
| TemplateResponseMixin | 模板响应类，加入Template的基本信息（名字）         |
|                       | 没有context的信息                                  |
|                       | 只有Template信息是没有用的，因为没有跟View联系起来 |
|                       | 跟View联系：把render_to_response插进MRO的调用顺序  |
|                       | 可以借鉴TemplateView                               |
| ContextMixin          | 就是一个get_context_data，用于返回context数据      |
| SingleObjectMixin     | 单对象类                                           |
|                       | 继承自ContextMixin，可以返回上下文数据             |
|                       | 在上下文数据中加入了object（get_object方法）的信息 |
|                       | 可以通过model，manager等方法获取数据               |
|                       | 根据slug_url_kwarg和pk_url_kwarg去检索数据         |
|                       | 具体的就是一个filter语句                           |
|                       | SingleObjectMixin目的在于限制context数据的东西     |
| MultipleObjectMixin   | 多对象类                                           |
| FormMixin             | 表单类                                             |
| YearMixin             | 基于时间关系的类                                   |
| MonthMixin            |                                                    |
| DayMixin              |                                                    |
| WeekMixin             |                                                    |
| DateMixin             |                                                    |


其他的所有内置class-based-view都是把以上几个基础类组合，重写方法以达到预期的结果。

#####View————提供模板和渲染
|        类名        |                        功能                       |
|--------------------|---------------------------------------------------|
| View               | 视图基础类，可以在任何时候使用                    |
|                    | get,post,put,delete,head,options,trace            |
|                    | View中是没有返回一个response的                    |
|                    | 只继承View，必须要重写get等，以返回一个response   |
| RedirectView       | 重新定向到其他URL                                 |
| TemplateView       | 显示HTML template                                 |
| ListView           | 显示对象列表                                      |
| DetailView         | 显示对象详情                                      |
|                    | SingleObjectTemplateResponseMixin、BaseDetailView |
| FormView           | From提交                                          |
| CreateView         | 创建对象                                          |
| UpdateView         | 更新对象                                          |
| DeleteView         | 删除对象                                          |
| Generic date views | 显示一段时间内的对象                              |


子类化一个类视图时，可以在子类中重写一些属性（比如template_name）或者方法（比如get_context_data）来提供一些新的属性或者方法。

Mixin和View不能随意组合，必须要注意他们之间的方法的解析顺序，也就是MRO(method resolution order)。

Django中Mixin和View把原来的视图函数中的三个东西分开了，模板（TemplateResponseMixin），上下文数据（ContextMixin），负责将这些联系起来的一个东西（胶水View）。