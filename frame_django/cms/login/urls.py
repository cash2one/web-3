from django.conf.urls import url, include
from login import views


urlpatterns = [
    url(r'^login/', include([
        url(r'^(?P<form_name>[a-z]+_[a-z]+|)$', views.LoginView.as_view(), name="login"),
        url(r'^get_email_code$', views.get_email_code, name='get_email_code'),
    ])),
    url(r'^menu/', include([
        # url(r'',),
    ]))
]
