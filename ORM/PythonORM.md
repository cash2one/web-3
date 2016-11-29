###Python有很多ORM库

######SQLObject
```
一个介于SQL数据库和Python之间映射对象的Python ORM。
表映射成类，行作为实例而字段作为属性。它同时提供一种基于Python对象的查询语言，这使得SQL更加抽象，从而为应用提供了数据库不可知性（应用和数据库分离）。
```

##Storm
一个介于 单个或多个数据库与Python之间 映射对象的Python ORM 。为了支持动态存储和取回对象信息，它允许开发者构建跨数据表的复杂查询。像 SQLAlchemy 和 SQLObject 那样， Storm 也映射表到类，行到实例和字段到属性。相对另外2个库， Stom中table class 不需要是框架特定基类 的子类 。在 SQLAlchemy中，每个 table class 是 sqlalchemy.ext.declarative.declarative_bas 的一个子类。 而在SQLOjbect中，每个table class是 sqlobject.SQLObject 的子类。

类似于 SQLAlchemy, Storm 的 Store 对象对于后端数据库就像一个代理人，所有的操作缓存在内存，一旦提交方法在store上被调用就提交到数据库。每个 store 持有自己的Python数据库对象映射集合，就像一个 SQLAlchemy session 持有不同的 Python对象集合。

3）Django 是一个免费开源的紧嵌ORM到其系统的web应用框架。因为Django的ORM是紧嵌到web框架的，所以就算可以也不推荐在一个独立的非Django的Python项目中使用它的ORM。
相比 SQLAlchemy， Django的ORM更吻合于直接操作SQL对象，操作暴露了简单直接映射数据表和Python类的SQL对象。

4）peewee 是一个小的，表达式的ORM。相比其他的 ORM，peewee主要专注于极简主义，其API简单，并且其库容易使用和理解。从视图的对象创建这点来看，peewee类似于Django。

5）SQLAlchemy 是Python编程语言里，一个在MIT许可下发布的开源工具和SQL ORM。它提供了 “一个知名企业级的持久化模式的，专为高效率和高性能的数据库访问设计的，改编成一个简单的Python域语言的完整套件”。它采用了数据映射模式（像Java中的Hibernate）而不是Active Record模式（像Ruby on Rails的ORM）。
SQLAlchemy 的工作单元主要使得有必要限制所有的数据库操作代码到一个特定的数据库session，在该session中控制每个对象的生命周期。

Python ORM 之间对比：
SQLObject
优点：
采用了易懂的ActiveRecord 模式
一个相对较小的代码库
缺点：
方法和类的命名遵循了Java 的小驼峰风格
不支持数据库session隔离工作单元

Storm
优点：
清爽轻量的API，短学习曲线和长期可维护性
不需要特殊的类构造函数，也没有必要的基类
缺点：
迫使程序员手工写表格创建的DDL语句，而不是从模型类自动派生
Storm的贡献者必须把他们的贡献的版权给Canonical公司

Django's ORM
优点：
易用，学习曲线短
和Django紧密集合，用Django时使用约定俗成的方法去操作数据库
缺点：
不好处理复杂的查询，强制开发者回到原生SQL
紧密和Django集成，使得在Django环境外很难使用

peewee
优点：
Django式的API，使其易用
轻量实现，很容易和任意web框架集成
缺点：
不支持自动化 schema 迁移
多对多查询写起来不直观

SQLAlchemy
优点：
企业级 API，使得代码有健壮性和适应性
灵活的设计，使得能轻松写复杂查询
缺点：
工作单元概念不常见
重量级 API，导致长学习曲线