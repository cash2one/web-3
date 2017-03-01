# -*- coding: utf-8 -*-
# @Date:   2017-02-27 08:54:30
# @Last Modified time: 2017-02-27 09:00:31
import sys
from multiprocessing import cpu_count, Pool

import redis

from core.engine import Engine as engine

reload(sys)
sys.setdefaultencoding('utf-8')


def create_redis_pool():
    '''
    创建redis连接池
    :return:
    '''
    redis_pool = redis.ConnectionPool(
        host='vm.test.com',
        port=6379,
        db=0,
        password=""
    )
    return redis_pool


def create_proxy():
    """
    '''
    代理服务器
    '''
    proxy_host = ""
    proxy_port = ""
    '''
    代理隧道验证信息
    '''
    proxy_user = ""
    proxy_pass = ""
    """
    proxy_host = "127.0.0.1"
    proxy_port = "8000"
    proxy_user = ""
    proxy_pass = ""
    proxy_meta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxy_host,
        "port": proxy_port,
        "user": proxy_user,
        "pass": proxy_pass,
    }

    proxies = {
        "http": proxy_meta,
        "https": proxy_meta,
    }
    return proxies


def create_child(thread_count, job_id, instance_id, script_name, use_http_proxy=False, debug=True):
    """
    创建子进程
    """
    http_proxy = create_proxy() if use_http_proxy else None
    if debug:
        from core.jobs import DebugJob as job
        from core.kit.piplines import DebugPipline as pipline
        redis_pool = None
    else:
        from core.jobs import Job as job
        from core.kit.piplines import MongodbPipline as pipline
        redis_pool = create_redis_pool()
    current_job = job(job_id, instance_id, redis_pool=redis_pool)
    current_pipline = pipline(current_job)
    engine.run(
        current_job,
        current_pipline,
        script_name,
        thread_count=thread_count,
        proxies=http_proxy
    )


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', help='script name')
    parser.add_argument("-p", "--process", help="[option,only effective in worker mode] process count ,default is cpu count", type=int, default=cpu_count())
    parser.add_argument("-t", "--thread", help="[option,only effective in worker mode] thread count in every process,default is 1", type=int, default=1)
    parser.add_argument('-worker', help='[option] run with online,please easy', action='store_true')

    args = parser.parse_args()
    debug = True
    if args.worker:
        debug = False

    process_count = args.process
    thread_count = args.thread
    if debug:
        process_count = 1
        thread_count = 1

    print("main process start")

    job_id = args.s
    use_http_proxy = False

    pool = Pool(processes=process_count)
    for i in range(process_count):
        result = pool.apply_async(
            create_child,
            [
                thread_count,
                job_id,
                '1',
                job_id,
                use_http_proxy,
                debug
            ]
        )
    pool.close()
    pool.join()

    print("main process dead")