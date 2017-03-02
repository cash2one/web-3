# -*- coding: utf-8 -*-
# @Date:   2017-02-27 09:29:16
# @Last Modified time: 2017-02-27 09:30:15
import hashlib
from Queue import Queue
import redis
from core.kit.utils import get_mashine_ip, get_process_id, correct


class BaseJob(object):
    """
    往队列里存取数据
    已爬队列使用set（自动去重）
    未爬队列使用list
    """

    def __init__(self, job_id, instance_id, redis_pool=None):
        self.redis_pool = redis_pool
        self._instance_id = instance_id
        self._job_id = job_id

    def get_job_id(self):
        """
        获取job_id
        :return:
        """
        return self._job_id

    def get_instance_id(self):
        """
        获取job的instance_id
        :return:
        """
        return self._instance_id

    def get_job_status(self):
        """
        获取当前instance的状态
        :return:
        """
        pass

    def get_item(self):
        pass

    def push_item(self, req, is_retry=False):
        """
        向待执行url队列里添加新url
        :param is_retry:
        :param req:
        :return:
        """
        pass

    def duplicate(self, url_str):
        pass


class RedisJob(BaseJob):

    def __init__(self, job_id, instance_id, redis_pool=None):
        self.redis = redis.StrictRedis(connection_pool=redis_pool)
        self._instance_id = instance_id
        self._job_id = job_id
        self._mashine_ip = get_mashine_ip()
        self._pid = get_process_id()

    def get_job_status(self):
        expect_instance_id = self.redis.get("spider_" + self.get_job_id())
        if expect_instance_id and expect_instance_id == self.get_instance_id():
            return True
        return False

    def get_item(self):
        return self.redis.rpop("spider-item_" + self.get_job_id() + "_" + self.get_instance_id())

    def push_item(self, req, is_retry=False):
        req._url = correct(req.get_url())
        if (not self.duplicate(req.get_url())) or is_retry:
            self.redis.lpush("spider-item_" + self.get_job_id() + "_" + self.get_instance_id(), req.dumpJson())

    def duplicate(self, url_str):
        is_dup = self.redis.sismember("spider-dup_" + self.get_job_id() + "_" + self.get_instance_id(), url_str)
        if not is_dup:
            self.redis.sadd("spider-dup_" + self.get_job_id() + "_" + self.get_instance_id(), url_str)
        return is_dup

    def set_mashine_status(self, status):
        self.redis.hset("mashines_" + self._mashine_ip, self.get_pid(), status)

    def get_pid(self):
        return self._pid


class DebugJob(BaseJob):
    """
    用于本地调试的job
    """
    def __init__(self, job_id, instance_id, redis_pool=None):
        self.queue = Queue()
        self._instance_id = instance_id
        self._job_id = job_id
        self._dup_dict = {}

    def get_job_status(self):
        return True

    def get_item(self):
        try:
            return self.queue.get(block=False, timeout=1)
        except:
            return None

    def push_item(self, req, is_retry=False):
        req._url = correct(req.get_url())
        if (not self.duplicate(req.get_url())) or is_retry:
            self.queue.put(req.dumpJson())
        else:
            print("dup:" + req.getUrl())

    def duplicate(self, url_str):
        url_str = hashlib.sha1(url_str).hexdigest()
        is_dup = self._dup_dict.get(url_str, False)
        if not is_dup:
            self._dup_dict[url_str] = True
        return is_dup
