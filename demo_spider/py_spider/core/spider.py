# -*- coding: utf-8 -*-
# @Date:   2017-02-27 11:48:09
# @Last Modified time: 2017-02-27 11:49:19
import traceback
from threading import Thread

import requests
from page import Page

from core.kit.req import Req


class Spider(Thread):

    def __init__(self, thread_q, pipline, current_job, script_module, proxies=None):
        super(Spider, self).__init__()
        self.thread_q = thread_q
        self.work_status = False
        self.pipline = pipline
        self.process = script_module.process
        self.current_job = current_job
        self._proxies = proxies
        self._site = {"encoding": "utf-8"}
        try:
            inner_site = script_module.site.get("encoding", None)
            if inner_site:
                self._site["encoding"] = inner_site
        except:
            pass

    def get_work_status(self):
        return self.work_status

    def run(self):
        while True:
            request_item = Req.from_request_item(self.thread_q.get())
            self.work_status = True
            try:
                r = self.download(request_item)
                if r.status_code == 200:
                    p = Page(request_item, r, r.text, self.current_job)
                    self.process(p)
                    for result in p.get_results():
                        self.pipline.save(result)

            except Exception, e:
                traceback.print_exc()  # .format_exc()
                try:
                    print(request_item.dumpJson())
                except:
                    pass
                try:
                    if request_item._retry < 3:
                        request_item._retry = request_item._retry + 1
                        self.current_job.pushItem(request_item, isRetry=True)
                except Exception, ex:
                    traceback.print_exc()  # .format_exc()

            self.thread_q.task_done()
            self.work_status = False

    def download(self, request):
        args = {
            "headers": {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"},
            "timeout": 60
        }
        if self._proxies:
            args["proxies"] = self._proxies
        if request._method.lower() == "get":
            r = requests.get(request.getUrl(), **args)
            r.encoding = self._site["encoding"]
            print(request.getUrl())
        return r
