from django.conf.urls import url, include
from django.contrib import admin
from login import urls as login_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(login_urls)),
]
