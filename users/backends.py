# -*- coding: utf-8 -*-
from django.db.models import Q
from app.models import User


def _get_user(username):
    try:
        return User.objects.get(Q(phone=username) | Q(email=username))
    except User.DoesNotExist:
        return None


class MarkOneAuthBackend(object):

    def authenticate(self, request, password, **kws):
        username = kws.get('phone') or kws.get('email')
        user = _get_user(username)
        if user and user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
