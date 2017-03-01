# -*- coding: utf-8 -*-
# @Date:   2017-02-27 09:09:48
# @Last Modified time: 2017-02-27 09:10:26
#
"""
保存数据的管道
PyMongo的client是一个默认连接池，会在一个socket使用结束后，自动回收这个连接
"""
import time
import pymongo


class Pipline(object):

    def __init__(self, job):
        self.job_id = job.get_job_id()
        self.instance_id = job.get_instance_id()

    def save(self, result):
        pass


class DebugPipline(Pipline):

    def save(self, result):
        """
        save方法的keyid不会被其它方法调用，可以不写self
        :param result:
        :return:
        """
        keyid = result.get("keyid", None)
        if keyid:
            print(result)
        else:
            raise Exception("keyid is needed when p.put({'keyid':'xxx' ......})")


class MongodbPipline(Pipline):
    client = pymongo.MongoClient('mongodb://vm.test.com:27017')
    db = client['results']

    def save(self, result):
        keyid = result.get("keyid", None)
        if keyid:
            result["__timer__"] = int(time.time())
            MongodbPipline.db[self.job_id].update_one(
                {"keyid": keyid},
                {"$set": result},
                upsert=True
            )
