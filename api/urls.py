# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from api.views import (LocalUrlView,)
from user.views import UsersView

urlpatterns = [
    url(r'^local_url/$', LocalUrlView.as_view(), name='local_url'),
    url(r'^users/?$', UsersView.as_view(), name='users'),
    url(r'^users/', include('user.urls')),
]
