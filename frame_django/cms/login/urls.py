from django.conf.urls import url, include
from login import views


urlpatterns = [
    url(r'^login/', include([
        url(r'^([a-z]+_[a-z]+|)$', views.LoginView.as_view(), name="login")
    ])),
]
