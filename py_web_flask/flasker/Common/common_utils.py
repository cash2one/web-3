# coding=utf-8

__author__ = ''
import urllib2
import json
from oss.oss_api import *
import time
from datetime import datetime, timedelta
from qiniu import Auth, put_file


class CommonUtils(object):
    """
    get请求返回string对象
    """

    @staticmethod
    def http_get(url):
        request = urllib2.Request(url)
        request.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(request)
        return response.read()

    """
    post请求返回string对象
    """

    @staticmethod
    def http_post(url, post_data):
        request = urllib2.Request(url, post_data)
        request.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(request)
        return response.read()

    '''
    put请求返回string对象
    '''

    @staticmethod
    def http_put(url, put_data):
        request = urllib2.Request(url, put_data)
        request.add_header('Content-Type', 'application/json')
        request.get_method = lambda x: 'PUT'
        response = urllib2.urlopen(request)
        return response.read()

    '''
    delete请求返回string对象
    '''

    @staticmethod
    def http_delete(url):
        request = urllib2.Request(url)
        request.add_header('Content-Type', 'application/json')
        request.get_method = lambda x: 'DELETE'
        response = urllib2.urlopen(request)
        return response.read()

    '''
    get请求返回json对象
    '''

    @staticmethod
    def get(url):
        return json.loads(CommonUtils.http_get(url))

    '''
    post请求返回json对象
    '''

    @staticmethod
    def post(url, post_data):
        return json.loads(CommonUtils.http_post(url, post_data))

    '''
    put请求返回json对象
    '''

    @staticmethod
    def put(url, post_data):
        return json.loads(CommonUtils.http_put(url, post_data))

    '''
    delete请求返回json对象
    '''

    @staticmethod
    def delete(url):
        return json.loads(CommonUtils.http_delete(url))

    @staticmethod
    def view_cache():
        cache = os.listdir('templates')

    @staticmethod
    def upload_img(file_path, file_name):
        oss = OssAPI("oss-cn-beijing.aliyuncs.com",
                     "D8POxD4e4EOaGap7", "cAnUGRVSmDAHjHKtpLelLcssKIDaNR")
        res = oss.put_object_from_file("building-images", file_name, file_path)
        if res.status == 200:
            return 'building-images.oss-cn-beijing.aliyuncs.com/{0}'.format(file_name)

    @staticmethod
    def upload_img_qiniu(file_path, file_name):
        q = Auth("ODF9cqw7TnYotPWHzo1RyTZ4amFnABF_Fw-2HtqT",
                 "M0blVKOhJGhtqWysOegJqd7I6FKZy236yzWYQGz0")
        token = q.upload_token("ubanoffice")
        ret, info = put_file(token, file_name, file_path, check_crc=True)
        print(ret)

    @staticmethod
    def upload_void_qiniu(file_path, file_name):
        q = Auth("ODF9cqw7TnYotPWHzo1RyTZ4amFnABF_Fw-2HtqT",
                 "M0blVKOhJGhtqWysOegJqd7I6FKZy236yzWYQGz0")
        token = q.upload_token("privatevideo")
        ret, info = put_file(token, file_name, file_path, check_crc=True)
        print(ret)

    @staticmethod
    def delete_img(file_name):
        oss = OssAPI("oss-cn-beijing.aliyuncs.com",
                     "D8POxD4e4EOaGap7", "cAnUGRVSmDAHjHKtpLelLcssKIDaNR")
        res = oss.delete_object("building-images", file_name)
        if res.status == 204:
            return 'ok'

    @staticmethod
    def getToday(days=0):
        d1 = datetime.now()
        d1 = datetime(d1.year, d1.month, d1.day, 0, 0, 0)
        if days:
            d1 = d1 + timedelta(days=days)
        epoch = datetime(1970, 1, 1, hour=8)
        diff = d1 - epoch
        d = diff.days * 24 * 3600 + diff.seconds
        return d

    @staticmethod
    def unixtime_to_strHMS(value):
        dt = datetime(1970, 1, 1, hour=8) + timedelta(seconds=value)
        dt = dt.strftime('%H:%M:%S')
        # format = '%Y-%m-%d'
        # value为传入的值为时间戳(整形)，如：1332888820
        # value = time.localtime(value)
        # 经过localtime转换后变成
        ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
        # 最后再经过strftime函数转换为正常日期格式。
        # dt = time.strftime(format, value)
        return dt

    @staticmethod
    def unixtime_to_strYMDHMS(value):
        dt = datetime(1970, 1, 1, hour=8) + timedelta(seconds=value)
        dt = dt.strftime('%Y-%m-%d %H:%M:%S')
        # format = '%Y-%m-%d'
        # value为传入的值为时间戳(整形)，如：1332888820
        # value = time.localtime(value)
        # 经过localtime转换后变成
        ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
        # 最后再经过strftime函数转换为正常日期格式。
        # dt = time.strftime(format, value)
        return dt

    @staticmethod
    def unixtime_to_str(value):
        dt = datetime(1970, 1, 1, hour=8) + timedelta(seconds=value)
        dt = dt.strftime('%Y-%m-%d')
        # format = '%Y-%m-%d'
        # value为传入的值为时间戳(整形)，如：1332888820
        # value = time.localtime(value)
        # 经过localtime转换后变成
        ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
        # 最后再经过strftime函数转换为正常日期格式。
        # dt = time.strftime(format, value)
        return dt

    @staticmethod
    def str_full_to_unixtime(dt):
        d = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')

        epoch = datetime(1970, 1, 1, hour=8)
        diff = d - epoch
        d = diff.days * 24 * 3600 + diff.seconds
        # dt为字符串
        # 中间过程，一般都需要将字符串转化为时间数组
        # time.strptime(dt, '%Y-%m-%d')
        ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
        # 将"2012-03-28 06:53:40"转化为时间戳
        # s = time.mktime(time.strptime(dt, '%Y-%m-%d'))
        return int(d)

    @staticmethod
    def str_to_unixtime(dt):
        d = datetime.strptime(dt, '%Y-%m-%d')

        epoch = datetime(1970, 1, 1, hour=8)
        diff = d - epoch
        d = diff.days * 24 * 3600 + diff.seconds
        # dt为字符串
        # 中间过程，一般都需要将字符串转化为时间数组
        # time.strptime(dt, '%Y-%m-%d')
        ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
        # 将"2012-03-28 06:53:40"转化为时间戳
        # s = time.mktime(time.strptime(dt, '%Y-%m-%d'))
        return int(d)

    @staticmethod
    def cnstr_to_unixtime(dt):
        d = None
        try:
            d = datetime.strptime(dt, '%Y年%m月%d日')
        except:
            try:
                d = datetime.strptime(dt, '%Y年%m月')
            except:
                d = datetime.strptime(dt, '%Y年')

        epoch = datetime(1970, 1, 1, hour=8)
        diff = d - epoch
        d = diff.days * 24 * 3600 + diff.seconds
        # dt为字符串
        # 中间过程，一般都需要将字符串转化为时间数组
        # time.strptime(dt, '%Y-%m-%d')
        ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
        # 将"2012-03-28 06:53:40"转化为时间戳
        # s = time.mktime(time.strptime(dt, '%Y-%m-%d'))
        return int(d)

    @staticmethod
    def datetime_to_unixtime(dt):

        epoch = datetime(1970, 1, 1, hour=8)
        diff = dt - epoch
        diff = diff.days * 24 * 3600 + diff.seconds
        # dt为字符串
        # 中间过程，一般都需要将字符串转化为时间数组
        # time.strptime(dt, '%Y-%m-%d')
        ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
        # 将"2012-03-28 06:53:40"转化为时间戳
        # s = time.mktime(time.strptime(dt, '%Y-%m-%d'))
        return int(diff)

    @staticmethod
    def get_unixtime():
        return int(time.time())
