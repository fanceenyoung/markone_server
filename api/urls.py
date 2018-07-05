# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from api.views import (LocalUrlView,)

urlpatterns = [
    url(r'^local_url/$', LocalUrlView.as_view(), name='local_url'),
    url(r'^users/', include('user.urls')),
    url(r'^', include('app.urls')),
]
