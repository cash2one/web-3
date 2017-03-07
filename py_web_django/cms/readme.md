文件夹是个独立的django项目

属性访问————var.***（句点查找）————可以多级深度嵌套————可以用来引用对象的方法，可用于访问列表索引（不允许使用负索引）

假如，一个 BankAccount 对象有一个 delete() 方法。如果某个模板中包含了像 {{ account.delete }}这样的标签，其中`account`是BankAccount的一个实例，在这个模板载入时，account对象将被删除。
要防止这样的事情发生，必须设置该方法的 alters_data 函数属性：
```
def delete(self):
    # Delete the account
delete.alters_data = True
```
那么在模板载入时， delete()方法将不会被执行。 它将静静地错误退出。



###松耦合原则————保证互换性的软件开发方法
决定URL返回哪个视图函数和实现这个视图函数是在两个不同的地方，修改一块而不会影响另一块

###Django的设计哲学理念————业务逻辑与表现逻辑分离
- 将模板系统视为控制表现及表现相关逻辑的工具，不应提供超出此基本目标的功能；
- 在模板中不能直接调用 Python 代码；
- 语法不应受到 HTML/XML 的束缚；


###静态文件

```
Question的超链接变成了绿色（Django的风格！）
css
li a {
    color: green;
}
body {
    background: white url("images/background.gif") no-repeat right bottom;
}

只能用于DEBUG，只能使用相对路径，只查找STATIC_ROOT
urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```