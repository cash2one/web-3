# -*- coding: utf-8 -*-
# @Date:   2016-11-28 14:19:26
# @Last Modified time: 2016-11-29 20:37:07
#
# 传递额外的参数到视图函数
# url(r'^foo/$', views.foobar_view, {'template_name': 'template1.html'}),
from views import views, test_views
from django.conf.urls import url, include

urlpatterns = [
    # 声明共同的路径前缀，然后include，不能直接把父级、子级写在一起
    url(r'^', include([
        # 使用命名组，传递关键字参数————忽略非命名组————(?P<name>\w{9})
        # 没有命名组，传递位置参数————(name)
        # 以的两种情况，Django同时会以关键字参数的方式传递一些额外参到视图函数
        url(r'^([a-z]+_[a-z]+|)$', views.login, name="login")
    ])),
    url(r'download_list/', include([
        url(r'^$', views.DownloadList.as_view()),
        url(r'^report_excel$', views.report_excel),
        url(r'^add_download', views.AddDownload.as_view()),
    ])),
]
# 邮箱验证码登录测试
urlpatterns += [
    # test必须有/
    url(r'^test/', include([
        url(r'^form_test', test_views.form_test),
        url(r'^login_test', test_views.LoginView.as_view()),
        url(r'^getcode', test_views.login_email_validate)
    ]))
]
