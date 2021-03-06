# -*- coding: utf-8 -*-
# @Date:   2017-02-27 11:48:09
# @Last Modified time: 2017-03-13 16:16:57
import traceback
import requests
from threading import Thread
from kit.page import Page
from kit.req import Req


class Spider(Thread):
    """
    一个爬虫线程
    每个线程导入一次爬虫脚本，执行时传入一个page对象给脚本的process函数
    """

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
            """
            get()阻塞线程，直到Queue队列有数据
            """
            req = Req.from_request_item(self.thread_q.get())
            self.work_status = True
            try:
                r = self.download(req)
                if r.status_code == 200:
                    """
                    把每次请求的req、response相关信息封装成page对象，再传给脚本的process方法
                    """
                    p = Page(req, r, r.text, self.current_job)
                    self.process(p)
                    for result in p.get_results():
                        self.pipline.save(result)

            except Exception, e:
                traceback.print_exc()  # .format_exc()
                try:
                    print(req.dump_json())
                except:
                    pass
                try:
                    if req._retry < 3:
                        req._retry = req._retry + 1
                        self.current_job.push_item(req, is_retry=True)
                except Exception, e:
                    traceback.print_exc()  # .format_exc()

            self.thread_q.task_done()
            self.work_status = False

    def download(self, req):
        """
        项目爬虫程序（处理get请求）
        :param request:
        :return:
        """
        args = {
            "headers": {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"},
            "timeout": 60
        }
        if self._proxies:
            args["proxies"] = self._proxies
        if req._method.lower() == "get":
            r = requests.get(req.get_url(), **args)
            r.encoding = self._site["encoding"]
            print(req.get_url())
        return r
