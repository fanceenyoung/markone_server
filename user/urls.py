# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from utils.func import SelfRouter, SimpleRouter
from user.views import UsersView, UserViewSet, forget_password


self_router = SelfRouter()
router = SimpleRouter()
self_router.register(r'', UserViewSet, base_name='user')

urlpatterns = [
    url(r'^logout/?$', UserViewSet.as_view({'put': 'logout'}), name='logout'),
    url(r'^check-password/?$', UserViewSet.as_view({'get': 'check_password'})),
    url(r'^update-relation/?$', UserViewSet.as_view({'put': 'update_relation'})),
    url(r'^forget-password/?$', forget_password, name='forget-password'),
    url(r'^', include(self_router.urls)),
    url(r'^', include(router.urls)),
]
