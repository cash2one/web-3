# -*- coding: utf-8 -*-
# @Date:   2017-02-27 11:08:48
# @Last Modified time: 2017-02-27 11:12:07
from requests.packages.urllib3.util import parse_url, Url


def get_mashine_ip():
    """
    获取本机ip
    :return:
    """
    import socket
    my_name = socket.getfqdn(socket.gethostname())   # 获取本机电脑名
    my_addr = socket.gethostbyname(my_name)          # 获取本机ip
    return my_addr


def get_process_id():
    """
    获取当前线程id
    :return:
    """
    import os
    return str(os.getpid())


def correct(url, refer_url=None):
    """
    校正url ：
            /abc.htm => http://xxx/abc.htm
            # => None
            javascript:xxx => None
    scheme='http', host='google.com', port=80, path='/mail/', query='?后面', auth='@后面', fragment='#后面'
    :param url:
    :param refer_url:
    :return:
    """
    p_host = None
    p_scheme = None
    p_port = None
    if refer_url:
        try:
            r_scheme, r_auth, r_host, r_port, r_path, r_query, r_fragment = parse_url(refer_url)
            if p_scheme and p_scheme.lower() in ['http', 'https']:
                p_scheme = p_scheme
            p_host = r_host
            p_port = r_port
        except:
            pass
    try:
        scheme, auth, host, port, path, query, fragment = parse_url(url)
        if not path and not host:
            return None
        if not host:
            if not p_host:
                return None
            else:
                host = p_host
                port = p_port
        if not scheme:
            scheme = p_scheme or 'http'

        return Url(scheme=scheme, auth=auth, host=host, port=port, path=path, query=query, fragment=fragment).url

    except Exception as e:
        return None


if __name__ == "__main__":
    url = "http://bj.58.com/job/?utm_source=market&spm=b-31580022738699-me-f-824.bdpz_biaoti&key="
    print correct(url)
