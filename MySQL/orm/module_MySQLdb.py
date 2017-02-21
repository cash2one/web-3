#!/usr/bin/python
# coding:utf-8
import MySQLdb
#
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# help(MySQLdb)
# print MySQLdb.version_info

"""
上下文管理器的任务————代码块执行前准备，代码块执行后收拾
with所求值的对象（类）必须有__enter__()和__exit__()函数
as可省略
"""


class WithMySQL:

    def __enter__(self):
        """
        __enter__
        在进入代码块前被with调用
        （必须）返回一个可供上下文使用的对象，赋值给as后面的变量
        """
        self.con = MySQLdb.connect(
            host='vm.test.com',
            user='root',
            passwd='zdd12315',
            db='system',
            port=3306,
            charset='utf8'
        )
        self.cur = self.con.cursor()
        return self.cur

    def __exit__(self, type, value, trace):
        """
        __exit__(异常类型,异常值,异常追踪信息)
        在离开代码块之后（异常、退出）被调用，并清理被使用的资源
        异常抛出时，与之关联的异常信息传给__exit__()方法
        清理资源，关闭文件等等操作
        """
        self.cur.close()
        self.con.commit()
        self.con.close()
        '''打印异常信息'''
        print type, value, trace

'''
if __name__ == '__main__':
    try:
        """
        try语句尝试连接
        """
        with WithMySQL() as m:
            while 1:
                sqls = raw_input('SQL:')
                print m.execute(sqls)
                print m.fetchall()
    except Exception as e:
        print e
'''


class MySQL:

    def __init__(self):
        try:
            self.con = MySQLdb.connect(
                host='vm.test.com',
                user='root',
                passwd='zdd12315',
                db='system',
                port=3306,
                charset='utf8'
            )
        except Exception as e:
            print e
        else:
            self.cur = self.con.cursor()

    def execute(self, args):
        self.cur.execute(args)

    def fetchall(self):
        return self.cur.fetchall()

    def __del__(self):
        """
        回收实例对象时执行
        """
        self.cur.close()
        self.con.commit()
        self.con.close()


if __name__ == '__main__':
    m = MySQL()
    while 1:
        sqls = raw_input('SQL:')
        if not sqls:
            break
        print m.execute(sqls)
        print m.fetchall()
