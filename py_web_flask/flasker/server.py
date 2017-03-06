# encoding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import os
from flask import Flask
from Controller import route_config, session_config # 路由、会话
from Common.logger import logger # 错误日志


def get_server_path():
    return os.path.split(os.path.realpath(__file__))[0] # 获取当前路径


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(get_server_path(), 'data', 'upload')
app.config['DOWNLOAD_FOLDER'] = os.path.join(get_server_path(), 'data', 'download')

# 注册session
session_config.init(app)


# if __name__ != "__main__":
# 注册登录验证拦截器


"""
#
# 注册router
#
"""
route_config.init(app)
logger.init(app.logger)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=2000)
