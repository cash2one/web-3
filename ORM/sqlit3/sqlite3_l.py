#encoding:utf-8
'''
Python SQLITE数据库是一款非常小巧的嵌入式开源数据库软件，也就是说没有独立的维护进程，
所有的维护都来自于程序本身。它使用一个文件存储整个数据库，操作十分方便。
它的最大优点是使用方便，功能相比于其它大型数据库来说，确实有些差距。
但是性能表现上，SQLITE并不逊色。麻雀虽小，五脏俱全， sqlite 实现了多数 sql-92 的标准，
比如说 transaction 、 trigger 和复杂的查询等。

python的数据库模块有统一的接口标准，所以数据库操作都有统一的模式，基本上都是下面几步
（假设数据库模块名为db）：

1. 用db.connect创建数据库连接，假设连接对象为conn
2. 如果该数据库操作不需要返回结果，就直接用conn.execute查询，根据数据库事务隔离级别的不同，
可能修改数据库需要conn.commit
3. 如果需要返回查询结果则用conn.cursor创建游标对象cur, 通过cur.execute查询数据库，
用cur.fetchall/cur.fetchone/cur.fetchmany返回查询结果。
根据数据库事 务隔离级别的不同，可能修改数据库需要conn.commit
4. 关闭cur, conn
'''
'''
一,Python SQLITE数据库导入模块：
'''
import sqlite3
'''
二,创建数据库连接对象
我们不需要显式的创建一个sqlite数据库，在调用connect函数的时候，指定库名称，
如果指定的数据库存在就直接打开这个数据库，如果不存在就新创建一个再打开。

打开数据库时返回的对象cx就是一个数据库连接对象，它可以有以下操作：
commit()--事务提交
rollback()--事务回滚
close()--关闭一个数据库连接
cursor()--创建一个游标
'''
cx=sqlite3.connect('D:/sqlite3_db/test.db')
'''
三,所有sql语句的执行都要在游标对象下进行。
首先，定义一个游标：
'''
cu=cx.cursor()

'''
游标对象有以下的操作：
execute()--执行sql语句
executemany--执行多条sql语句
close()--关闭游标
fetchone()--从结果中取一条记录，并将游标指向下一条记录
fetchmany()--从结果中取多条记录
fetchall()--从结果中取出所有记录
scroll()--游标滚动 

使用Python SQLITE数据库中游标对我们上面建立的数据库作一些操作：
1,建表：
'''
#使用try语句防止多次运行时，数据库已经存在而报错
try:
	cu.execute('create table test(id integer auto_increment primary key not null,name varchar(15))')
except:
	pass
'''
2,插入数据:
'''
try:
	cu.execute("insert into test values (1,'aaa')")
	cu.execute("insert into test values (2,'bbb')")
except:
	pass

#简单的插入两行数据,不过需要提醒的是,只有提交了之后,才能生效.
#我们使用数据库连接对象cx来进行提交commit和回滚rollback操作.

cx.commit()
'''
3,查询:
'''
cu.execute('select * from test')
'''
要提取查询到的数据,使用游标的fetch***函数,如:
'''
print cu.fetchall()
'''
如果我们使用cu.fetchone(),则首先返回列表中的第一项,再次使用,则返回第二项,依次下去.

4,修改:
'''
cu.execute("update test set name='name2' where id = 1") 
cx.commit()#注意,修改数据以后提交
print cu.fetchall()
'''
5,删除:
'''
cu.execute("delete from test where id = 1")
cx.commit()
print cu.fetchall()
'''
以上简单的操作反应的Python SQLITE数据库操作的基本要点,这里点到为止.
然后,SQLite的强大,并不仅限于此,其对SQL高级特性的支持及其小巧灵活的特点,使得SQLite在众多领域受到开发者的青睐.
'''


'''
Python SQLITE数据库游标的使用：
游标提供了一种对从表中检索出的数据进行操作的灵活手段，
就本质而言，游标实际上是一种能从包括多条数据记录的结果集中每次提取一条记录的机制。
游标总是与一条SQL  选择语句相关联。
因为游标由结果集（可以是零条、一条或由相关的选择语句检索出的多条记录）和结果集中指向特定记录的游标位置组成。
当决定对结果集进行处理时，必须声明一个指向该结果集的游标。
如果曾经用 C 语言写过对文件进行处理的程序，那么游标就像您打开文件所得到的文件句柄一样，
只要文件打开成功， 该文件句柄就可代表该文件。对于游标而言，其道理是相同的。
可见游标能够实现按与传统程序读取平面文件类似的方式处理来自基础表的结果集，
从而把表中数据以平面文件的形式呈现给程序。
    
    我们知道关系数据库管理系统实质是面向集合的，在Sqlite中并没有一种描述表中单一记录的表达形式，
    除非使用where  子句来限制只有一条记录被选中。
    因此我们必须借助于游标来进行面向单条记录的数据处理。
    由此可见，游标允许应用程序对查询语句select  返回的行结果集中每一行进行相同或不同的操作，
    而不是一次对整个结果集进行同一种操作；它还提供对基于游标位置而对表中数据进行删除或更新的能力；
    正是游标把作为面向集合的数据库管理系统和面向行的程序设计两者联系起来，
    使两个数据处理方式能够进行沟通。

sqlite3教程
http://www.runoob.com/sqlite/sqlite-intro.html
'''