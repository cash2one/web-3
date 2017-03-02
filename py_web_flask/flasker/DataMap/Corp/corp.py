# coding:utf-8
from peewee import *
from playhouse.read_slave import ReadSlaveModel
from DataConnect.DataSource import corp_database, corp_database_read_1

class BaseModel(ReadSlaveModel):
    class Meta:
        database = corp_database
        read_slaves = (corp_database_read_1,)



class DownloadCenter(BaseModel):
    id = PrimaryKeyField(db_column='id')
    file_name = CharField()
    file_type = CharField()
    upload_at = IntegerField()
    link = CharField()

    class Meta:
        db_table = 'downloadcenter'