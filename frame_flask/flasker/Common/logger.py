# encoding=utf-8
import traceback # 追踪异常

__author__ = ''


class logger(object):
    _lg = None

    @staticmethod
    def init(log):
        logger._lg = log

    @staticmethod
    def error(e=None):
        errorstrack = traceback.format_exc()
        if e:
            errorstrack = errorstrack + '\n' + e.message
        logger._lg.error(errorstrack)
