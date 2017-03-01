# -*- coding: utf-8 -*-
# @Date:   2017-02-27 09:09:04
# @Last Modified time: 2017-02-27 09:10:18
import importlib
import sys
import time
import traceback
from Queue import Queue
from core.kit.req import Req
from spider import Spider

reload(sys)
sys.setdefaultencoding('utf8')


class Engine:

    @staticmethod
    def run(current_job, pipline, script_name, thread_count=1, proxies=None):

        try:
            if not current_job.get_job_status():
                print("job is not start")
                return
            script =importlib.import_module('scripts.'+script_name)

            print(current_job.get_pid()+" process start")
            thread_q = Queue(maxsize=thread_count*3)
            for starturl in script.starturl:
                current_job.push_item(req=Req(starturl))

            """
            创建工作线程
            """

            spiders = []
            for i in range(thread_count):
                sp = Spider(thread_q, pipline, current_job, script, proxies)
                sp.daemon = True
                sp.start()
                spiders.append(sp)
            """
            1，判断分布式job是否停止
            2，从队列(redis)取request，分发给线程(Queue中继)
            3，通知集群，本进程的工作状态
            """
            while current_job.get_job_status():
                if thread_q.full():
                    time.sleep(3)
                else:
                    url_item = current_job.get_item()
                    if not url_item:
                        if current_job.get_job_status():
                            has_thread_running = False
                            for status in spiders:
                                if status.getWorkStatus():
                                    has_thread_running = True
                                    break
                            if not has_thread_running:
                                current_job.set_mashine_status("waitother")
                        time.sleep(3)
                    else:
                        current_job.set_mashine_status("running")
                        thread_q.put(url_item, False)
            current_job.set_mashine_status("stop")
        except Exception, e:
            traceback.print_exc()
        print(current_job.get_pid()+" process end")


    @staticmethod
    def debug_run(current_job, pipline, script_name, thread_count=1, proxies=None):

        try:
            script =importlib.import_module('scripts.'+script_name)

            thread_q = current_job.queue
            for starturl in script.starturl:
                current_job.pushItem(req=Req(starturl))

            """
            创建工作线程
            """
            spiders=[]
            for i in range(thread_count):
                sp = Spider(thread_q, pipline, current_job, script, proxies=proxies)
                sp.daemon = True
                sp.start()
                spiders.append(sp)
            for s in spiders:
                s.join()

        except Exception,e:
            traceback.print_exc()
