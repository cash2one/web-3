from django.conf.urls import url, include
from login.views import login_views


urlpatterns = [
    url(r'^', include([
        url(r'^([a-z]+_[a-z]+|)$', login_views.LoginView.as_view(), name="login")
    ])),
]
