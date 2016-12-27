from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

from login import urls as login_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/login')),
    url(r'^', include(login_urls)),
]
