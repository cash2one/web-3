# coding:utf-8
from Controller.download.views import *

def init(app):
    app.add_url_rule('/', view_func=DownloadCenterAction.as_view('download_center'),
                     methods=['GET', 'POST'])