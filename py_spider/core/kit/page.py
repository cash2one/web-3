# -*- coding: utf-8 -*-
# @Date:   2017-02-27 11:47:36
# @Last Modified time: 2017-02-27 11:47:44
from core.kit.utils import correct
from req import Req


class Page:
    """
    Page对象，封装了每次request、response的相关信息
    """

    def __init__(self, request, response, text, current_job):
        self._text = text
        self._results = []
        # self._htmlselector = None
        # self._textselector = None
        # self._jsonselector = None
        self._request = request
        self._response = response
        self._job = current_job

    def get_req(self):
        """
        获取 req对象
        :return:
        """
        return self._request

    def is_default_level(self):
        return self.get_req().is_level("")

    def is_level(self, level):
        return self.get_req().is_level(level)

    def get_ext(self, key):
        return self.get_req().get_ext(key)

    def put_ext(self, key, value):
        self.get_req().put_ext(key, value)

    def get_url(self):
        return self.get_req().get_url()

    def get_text(self):
        return self._text

    def get_results(self):
        return self._results

    def put(self, arg):
        if isinstance(arg, dict):
            self._results.append(arg)
        else:
            raise Exception("arg must is dict,example: page.put({....})")

    def add_url(self, url, level="", ext=None, force=False):
        ext = ext if ext else {}
        """
        待爬取队列添加url
        :param url: 要爬取的url
        :param level: script的level
        :param ext: 用户定义的数据
        :param force: False（默认），如果url已经爬取过，就不向队列添加。True，强制向队列添加url
        :return:
        """
        if level is None:
            raise Exception("page.add_url(...)  level parametar can not be empty or ''")
        r = Req(url=url, level=level, ext=ext)
        valid_url = correct(r.get_url(), self._request.get_url())
        if valid_url:
            r._url = valid_url
            self._job.push_item(r, is_retry=force)
        else:
            print("invalid url:"+url)
