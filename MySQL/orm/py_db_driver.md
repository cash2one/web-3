###SQLITE数据库
- 小巧的嵌入式开源数据库软件，没有独立的维护进程，所有的维护都来自于程序本身；
- 使用一个文件存储整个数据库，操作十分方便，功能稍差；
- 性能不错，实现了多数 sql-92 的标准，比如说 transaction 、 trigger 和复杂的查询等；

```
import sqlite3
cx = sqlite3.connect("E:/test.db")
```

#####python的数据库模块接口标准
1. db.connect(host,user,passwd,db,port,charset)————创建数据库连接对象————conn；
    + mysql————connect(host, user, passwd, db, port, charset)；
        * host————数据库主机名/ip，默认是用本地主机；
        * user————数据库登陆名，默认是当前用户；
        * passwd————数据库登陆秘密，默认为空；
        * db————要使用的数据库名，没有默认值；
        * port————MySQL服务使用的TCP端口，默认是3306；
        * charset————数据库编码（'utf8'）；
    + sqlite3————connect(database[, timeout, isolation_level, detect_types, factory])
2. 操作数据库
    + 不需要返回结果
        * conn.query()；
    + 返回查询结果
        * conn.cursor()————创建游标对象————cur；
        * 用来存储python传递给mysql的命令和mysql传递给python的数据；
            - 提供了一种对从表中检索出的数据进行操作的灵活手段；
            - 一种能从包括多条数据记录的结果集中每次提取一条记录的机制；
            - 总是与一条SQL选择语句相关联；
            - 当决定对结果集进行处理时，必须声明一个指向该结果集的游标；
                + 由结果集（由相关的选择语句检索出的0~多条记录）和结果集中指向特定记录的游标位置组成；
            - 就像打开文件所得到的文件句柄一样，只要文件打开成功，句柄就可代表该文件；
                + 能够实现按与传统程序读取平面文件类似的方式处理来自基础表的结果集；
                + 从而把表中数据以平面文件的形式呈现给程序；
            - 必须借助于游标来进行面向单条记录的数据处理；
            - 允许应用程序对查询语句select返回的行结果集中每一行进行相同或不同的操作，而不是一次对整个结果集进行同一种操作；
            - 提供对基于游标位置而对表中数据进行删除或更新的能；
            - 把作为面向集合的数据库管理系统和面向行的程序设计两者联系起来，使两个数据处理方式能够进行沟通；
        * cur.callproc(self, procname, args)————执行存储过程，返回受影响的行数；
            - procname————存储过程名；
            - args————参数列表；
        * 执行1~多条sql，返回受影响行数————long；
            - cur.execute(query, args=None)
            - cur.executemany(query, args)
                + query————sql语句；
                + args————参数列表；
        * 移动到下一个结果集————cur.nextset(self)；
        * 返回（1~多条）查询结果————查询结果是一次性消耗品；
            - cur.fetchone()————(result,...)————迭代器；
            - cur.fetchall()————((result,...),...)；
            - cur.fetchmany(size=None)————((result,...),...)；
                + size > 结果行数，返回cursor.arraysize条数据；
        * 游标滚动————cur.scroll(value, mode='relative')；
            - mode='relative'————从当前所在行移动value条；
            - mode='absolute'————从结果集的第一行移动value条；
        * cur.close()————关闭游标；
        * cur.rowcount————只读属性，返回执行execute()方法后影响的行数；
3. conn.commit()————事务提交（修改数据库）；
    + 如果数据库不支持事务，它就没有任何作用；
4. conn.rollback()————事务回滚————“撤销”所有未提交的事务；
    + 不支持事务（事务是一系列动作）的数据库，方法不可用；
5. conn.close()————关闭conn；
