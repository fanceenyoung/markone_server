# -*- coding: utf-8 -*-
import logging
import random
import time

from django.conf import settings
from rest_framework import viewsets
from rest_framework.decorators import list_route

from shaw import errors
from shaw.exception import SHException
from shaw.schema import check_body_keys
from shaw.web import empty_response

from users.email_mixins import send_email_code
from utils import exceptions

LOG = logging.getLogger(__name__)


class VerifyBase(object):
    USERNAME_FIELD = 'auth'
    CODE_EXPIRY_TIME = settings.CODE_EXPIRY_TIME
    CODE_SEND_INT = settings.CODE_SEND_INT

    @staticmethod
    def _send(username, code):
        pass

    @staticmethod
    def _gen_code():
        pass

    @classmethod
    def send(cls, session, username):
        now = time.time()
        key = 'auth.verify.' + username
        item = session.get(key)

        if item and (now - item[1]) < cls.CODE_SEND_INT:
            raise SHException(code=errors.ERR_TOO_MANY_REQUESTS,
                              message='Request for code too frequency!')

        if item and (now - item[1]) < cls.CODE_EXPIRY_TIME:
            code = item[0]
        else:
            code = cls._gen_code()
        session[key] = (code, now)
        cls._send(username, code)
        return empty_response()

    @classmethod
    def _make_verified(cls, session, username, expires=None):
        expires = expires or time.time() + cls.CODE_EXPIRY_TIME
        session['auth.verified.' + username] = expires
        session.save()

    @classmethod
    def _clear(cls, session, username):
        session.pop('auth.verified.' + username, None)
        session.save()

    @classmethod
    def check(cls, session, username, raise_exception=True):
        expires = session.get('auth.verified.' + username, 0)
        timeout = time.time() > expires
        if raise_exception and timeout:
            raise exceptions.WrongAuth(cls.USERNAME_FIELD)
        return not timeout

    @classmethod
    def verify(cls, session, username, code):
        items = session.get('auth.verify.' + username)
        if not items:
            raise exceptions.UnsentCode()

        now = time.time()
        _code, timestamp = items

        if now > timestamp + cls.CODE_EXPIRY_TIME:
            msg = 'Verify code after %d min!' % (cls.CODE_EXPIRY_TIME / 60)
            raise SHException(code=errors.ERR_TIME_LIMIT_EXCEEDED,
                              message=msg)

        if _code != code:
            raise exceptions.WrongCode()

        cls._make_verified(session, username)


class VerifyEmail(VerifyBase):
    USERNAME_FIELD = 'email'

    @staticmethod
    def _gen_code():
        return str(random.randint(100000, 999999))

    @staticmethod
    def _send(email, code):
        send_email_code(email, code)


class VerifyPass(VerifyBase):
    USERNAME_FIELD = 'test'

    @staticmethod
    def _gen_code():
        return '0000'

    @staticmethod
    def _send(email, code):
        print('send verify code ha ha ha!')


class VerifyViewSet(viewsets.ViewSet):

    @list_route(methods=['put'])
    def send(self, request):
        VerifyPass.send(request.session, request.data.get('phone') or request.data.get('email'))
        return empty_response()

    @list_route(methods=['put'])
    def verify(self, request):
        data = request.data
        check_body_keys(data, ['code'])
        if request.data.get('email'):
            VerifyEmail.verify(request.session, data.get('email'), data['code'])
        return empty_response()
