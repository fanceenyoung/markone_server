# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from django.contrib import admin

from markone_server.views import (DomainIndexView, IndexView, index)

urlpatterns = [
    url(r'^$',  DomainIndexView.as_view(), name='index'),
    # url(r'^$',  index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls', namespace='api')),
]
