# coding:utf-8
from peewee import *
from ConfigTool import getConnString

corp = getConnString('DataBase.corp')
corp_database = MySQLDatabase('corp',
                              # max_connections=8, stale_timeout=300,
                              threadlocals=True,
                              **{'host': corp.host,
                                 'password': corp.passwd,
                                 'port': corp.port,
                                 'user': corp.user,
                                 'charset': corp.charset})

corp_read_1 = getConnString('DataBase.corp.read.1')
corp_database_read_1 = MySQLDatabase('corp',
                                     # max_connections=8, stale_timeout=300,
                                     threadlocals=True,
                                     **{'host': corp_read_1.host,
                                        'password': corp_read_1.passwd,
                                        'port': corp_read_1.port,
                                        'user': corp_read_1.user,
                                        'charset': corp_read_1.charset})