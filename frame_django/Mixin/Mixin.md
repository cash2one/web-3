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

#####主要的Mixin
- View————视图基础类
- SingleObjectMixin————单对象类
- MultipleObjectMixin————多对象类
- TemplateResponseMixin————模板响应类
- FormMixin————表单类
- YearMixin, MonthMixin, DayMixin, WeekMixin, DateMixin————基于时间关系的类

其他的所有内置class-based-view都是把以上几个基础类组合，重写方法以达到预期的结果，比如DetailView这个类就组合了SingleObjectTemplateResponseMixin和BaseDetailView.

子类化一个类视图时，可以在子类中重写一些属性（比如template_name）或者方法（比如get_context_data）来提供一些新的属性或者方法。

Mixin和View的职能区分为：Mixin提供数据，View提供模板和渲染。所以一般get_context_data在Mixin中，get(),post(),head()在View中。Mixin和View不是能随意组合的，必须要注意他们之间的方法的解析顺序，也就是MRO(method resolution order)。

Django中Mixin和View把原来的视图函数中的三个东西分开了，模板（TemplateResponseMixin），上下文数据（ContextMixin），负责将这些联系起来的一个东西（胶水View）。

ContextMixin：就是一个get_context_data，用于返回context数据。

View：会调用所有的get、post方法['get', 'post', 'put', 'delete', 'head', 'options', 'trace']，View中是没有返回一个response的，所以光继承View的话，必须要重写get等，以返回一个response。

TemplateResponseMixin：故名思议，这个Mixin会加入Template的基本信息，也就是template的名字。
但是光有Template信息是没有用的，因为她没有跟View联系起来，如果想要跟View联系起来的话必须想办法把render_to_response插进MRO的调用顺序，而且TemplateResponseMixin是没有context的信息的。有一个可以借鉴的方法就是TemplateView的做法：


SingleObjectMixin继承自ContextMixin，也就是说他存在返回上下文数据这个东西了，然后对其进行稍微的包装，也就是说，在上下文数据中加入了object的信息。如何获取这些信息呢，当然可以通过model，manager等等方法。如何加入object的信息呢，这里使用的是get_object方法。然后根据slug_url_kwarg和pk_url_kwarg去检索数据。具体的过程可以去参考django的官方文档，我这里是直接从源代码的角度去看的。具体的就是一个filter语句。这个SingleObjectMixin目的在于限制context数据的东西。