###Bootstrap
- Bootstrap 是一个用于快速开发 Web 应用程序和网站的前端框架。
- 基于 HTML、CSS、JAVASCRIPT。
- 由 Twitter 的 Mark Otto 和 Jacob Thornton 开发，2011 年八月在 GitHub 上发布的开源产品。

######为什么使用 Bootstrap？
- 移动设备优先：自 Bootstrap 3 起，框架包含了贯穿于整个库的移动设备优先的样式。
- 浏览器支持：所有的主流浏览器都支持 Bootstrap。
- 容易上手；
- 响应式设计：Bootstrap的响应式CSS能够自适应于台式机、平板电脑和手机。

- 它为开发人员创建接口提供了一个简洁统一的解决方案。
- 它包含了功能强大的内置组件，易于定制。
- 它还提供了基于 Web 的定制。
- 它是开源的。

###Bootstrap 包的内容
- 基本结构：Bootstrap 提供了一个带有网格系统、链接样式、背景的基本结构。
- CSS：全局的CSS设置、定义基本的HTML元素样式、可扩展的class，以及一个先进的网格系统。
- 组件：十几个可重用的组件，用于创建图像、下拉菜单、导航、警告框、弹出框等等。
- JavaScript 插件：十几个自定义的jQuery插件。您可以直接包含所有的插件，也可以逐个包含这些插件。
- 定制：您可以定制 Bootstrap 的组件、LESS 变量和 jQuery 插件来得到您自己的版本。

###下载安装
- Download Bootstrap：Bootstrap CSS、JavaScript 和字体的预编译的压缩版本，不包含文档和最初的源代码文件。
- Download Source：Bootstrap LESS 和 JavaScript 源代码。

预编译文件可以直接使用到任何 web 项目中。

请注意，Bootstrap 的所有 JavaScript 插件都依赖 jQuery，因此 jQuery 必须在 Bootstrap 之前引入，就像在基本模版中所展示的一样。在 bower.json 文件中 列出了 Bootstrap 所支持的 jQuery 版本。

###引入
- 百度静态资源库(http://cdn.code.baidu.com/)上有Bootstrap资源。
- 使用 Bootstrap 中文网提供的免费 CDN 加速服务
<!-- 最新的Bootstrap CSS 文件 -->
<link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css">
<!-- Bootstrap主题文件（一般不用引入） -->
<link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
<!-- jQuery，务必在bootstrap.min.js 之前引入 -->
<script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
<!-- 最新的Bootstrap js 文件 -->
<script src="//cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

bootstrap.min.css  是经过压缩后的bootstrap样式表，内容和bootstrap.css完全一样，但是把中间不必要的空格之类的东西都删掉了，所以文件大小会比bootstrap.css小，可以在部署网站的时候引用。bootstrap.css适合在开发的时候引用。

####bootstrap

Bootstrap 模态框（Modal）
Bootstrap Typeahead


因为bootstrap是用less写的，less会编译成css显示在页面上。
但有个麻烦，浏览器里看的都是css第几排，而你编辑的又是less文件，很难对上。
这个时候有了source map，浏览器里直接显示less，非常方便。

####响应式导航条
默认的.navbar-default, 效果是:白色的背景黑色的字；
.navbar-inverse, 效果是:黑色的背景加上白色的字。
如果想要这两种默认的其他效果, 就需要自己去实现样式, 可以查看css的源代码, 然后去看.navbar-inverse怎么实现。

固定顶端的样式.navbar-fixed-top
固定底端的样式.navbar-fixed-bottom