# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from utils.func import SelfRouter, SimpleRouter
from users.views import (UserViewSet, forget_password, user_login, check_user, LogoutView,
                         UploadAvatarView, UploadImageView, certify_email, certify_password, CertifyEmailView)
from users.vertify_backend import VerifyViewSet


self_router = SelfRouter()
router = SimpleRouter()
router.register('auth_verify', VerifyViewSet, base_name='auth_verify')
self_router.register('', UserViewSet, base_name='users')

urlpatterns = [
    url(r'^login/?$', user_login, name='login'),
    url(r'^check_user/?$', check_user, name='check_user'),
    url(r'^forget_password/?$', forget_password, name='forget_password'),
    url(r'^certify_email/$', CertifyEmailView.as_view(), name='certify_email'),
    url(r'^certify_password/?$', certify_password, name='certify_password'),
    url(r'^upload_avatar/?$', UploadAvatarView.as_view(), name='upload_avatar'),
    url(r'^upload_image/?$', UploadImageView.as_view(), name='upload_image'),

    url(r'^logout/?$', LogoutView.as_view(), name='logout'),
    url(r'^reset_password/?$', UserViewSet.as_view({'put': 'reset_password'})),
    url(r'^help_center/?$', UserViewSet.as_view({'get': 'help_center'})),
    url(r'^', include(self_router.urls)),
    url(r'^', include(router.urls)),
]
