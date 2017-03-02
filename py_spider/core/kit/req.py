# -*- coding: utf-8 -*-
# @Date:   2017-02-27 13:20:49
# @Last Modified time: 2017-02-27 13:20:55
import json


class Req:
    """
    Req，把一个url封装转换为每次request的相关信息（每次请求实例化一次）
    给字典对象_ext，添加以键取值、更新键值对的方法————put_ext、get_ext
    类（实例）的对象可以直接获取、修改、判断，封装方法只是方便调用
    """

    def __init__(self, url="", method="get", data=None, ext=None, retry=0, level=""):
        self._url = url
        self._method = method
        self._data = data if data else {}
        self._ext = ext if ext else {}
        self._retry = retry
        self._level = str(level)

    def is_start(self):
        return self.is_level("")

    def is_level(self, level):
        return self._level == str(level)

    def set_level(self, level):
        self._level = str(level)

    def get_ext(self, key):
        return self._ext.get(key, "")

    def put_ext(self, key, value):
        self._ext[str(key)] = value

    @staticmethod
    def from_request_item(request_item):
        """
        staticmethod与实例化的对象无关
        集成外部函数
        美化代码结构
        不需要类实例化
        :param request_item:
        :return:
        """
        request_json = json.loads(request_item)
        return Req(**request_json)

    def dump_json(self):
        return json.dumps(self.get_dict())

    def get_url(self):
        return self._url

    def get_dict(self):
        return {
            "url": self._url,
            "method": self._method,
            "data": self._data,
            "ext": self._ext,
            "retry": self._retry,
            "level": self._level
        }
