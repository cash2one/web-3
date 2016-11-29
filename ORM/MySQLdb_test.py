#!/usr/bin/python
# coding:utf-8
import MySQLdb as sql
# help(sql)

print sql.version_info


class MySQL:

    # 创建连接对象
    def __init__(self):
        self.con = sql.connect(
            host='localhost',  # 主机名或者ip
            user='root',  # 用户名
            passwd='1234',  # 用户的密码
            db='test',  # 要使用的数据库的名字
            port=3306,  # 端口
            charset='utf8'  # 编码，必须是utf8，不能是utf-8
        )
        self.cur = self.con.cursor()  # 创建cursor['kɜːsə]——光标、指针；
        # 游标是用来存储python传递给mysql的命令和mysql传递给python的数据的

    def execute(self, sqls):
        return self.cur.execute(sqls), type(self.cur.execute(sqls))
        # execute['eksɪkjuːt]——执行，以长整型的形式，返回库、表个数

    def fetchone(self):
        return self.cur.fetchone(), type(self.cur.fetchone())  # 显示一个库、表名（元组）

    def fetchmany(self):
        return self.cur.fetchmany(3), type(self.cur.fetchmany())
        # 显示指定条数的库、表名（元组中套元组形式）

    def fetchall(self):
        # for i in cur.fetchall():
        # 	return i#显示所有数据库名称（以单个小元组的方式一一列出查询结果）
        return self.cur.fetchall()  # fetch——取来，以一个大元组包含小元组的方式返回所有查询结果

    def __del__(self):
        self.cur.close()  # 关闭游标
        self.con.commit()  # 提交数据
        # con.roolback() # 数据回滚
        self.con.close()  # 关闭数据库连接


if __name__ == '__main__':
    m = MySQL()
    while 1:
        sqls = raw_input('SQL:')
        print m.execute(sqls)
        print m.fetchone()
        print m.fetchmany()
        print m.fetchall()
