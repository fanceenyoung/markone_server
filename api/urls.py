# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from api.views import (LocalUrlView, DashboardView)

urlpatterns = [
    url(r'^local_url/$', LocalUrlView.as_view(), name='local_url'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^users/', include('users.urls')),
    url(r'^', include('app.urls')),
]
