# encoding=utf-8
__author__ = ''
# import MySQLdb
import mysql.connector


class DataBase(object):
    def __init__(self, config):
        self.config = config
        self.conn = mysql.connector.connect(host=self.config.host,
                                            user=self.config.user,
                                            passwd=self.config.passwd,
                                            db=self.config.dbname,
                                            port=self.config.port,
                                            charset=self.config.charset,
                                            connect_timeout=60)

    def execute(self, sql, para=None):
        try:
            cur = self.conn.cursor()
            cur.execute(sql, para)
            cur.close()
            self.conn.commit()
        except (AttributeError, mysql.connector.OperationalError):
            self.conn = mysql.connector.connect(host=self.config.host,
                                                user=self.config.user,
                                                passwd=self.config.passwd,
                                                db=self.config.dbname,
                                                port=self.config.port,
                                                charset=self.config.charset,
                                                connect_timeout=60)
            cur = self.conn.cursor()
            cur.execute(sql, para)
            cur.close()
            self.conn.commit()

    def queryEntity(self, sql, para=None):
        try:
            cur = self.conn.cursor()
            cur.execute(sql, para)
            ret = cur.fetchall()
            description = [item[0] for item in cur.description]
            cur.close()
            entitys = []
            for item in ret:
                every = {}
                for i in range(len(item)):
                    every[description[i]] = item[i]
                entitys.append(every)
            return entitys
        except (AttributeError, mysql.connector.OperationalError):
            self.conn = mysql.connector.connect(host=self.config.host, user=self.config.user,
                                                passwd=self.config.passwd, db=self.config.dbname,
                                                port=self.config.port, charset=self.config.charset,
                                                connect_timeout=60)
            cur = self.conn.cursor()
            cur.execute(sql, para)
            ret = cur.fetchall()
            description = [item[0] for item in cur.description]
            cur.close()
            entitys = []
            for item in ret:
                every = {}
                for i in range(len(item)):
                    every[description[i]] = item[i]
                entitys.append(every)
            return entitys

    def close(self):
        self.conn.close()
