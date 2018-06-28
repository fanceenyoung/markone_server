# coding: utf-8
import re
import string

from django.core.exceptions import ValidationError as DValidationError
from rest_framework.exceptions import APIException
from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler


class ErrorFactory(type):
    def __new__(cls, name, bases, attrs):
        base = bases[0]
        if 'default_code' not in attrs:
            code = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', name)
            code = '_'.join(map(string.lower, code))
            attrs['default_code'] = code
        clazz = super(ErrorFactory, cls).__new__(cls, name, bases, attrs)
        if hasattr(base, '_children'):
            base._children.append(clazz)
        return clazz


class BasicException(APIException):
    __metaclass__ = ErrorFactory

    status_code = 400

    _children = []


class InvalidUUID(BasicException):
    pass


class InvalidValue(BasicException):
    pass


class InvalidFormat(BasicException):
    pass


class InvalidPhoneNumber(BasicException):
    pass


def custom_exception_handler(exc, context):
    if isinstance(exc, DValidationError) and exc.message == "'%(value)s' is not a valid UUID.":
        exc = InvalidUUID()

    response = exception_handler(exc, context)

    if isinstance(exc, ValidationError):
        try:
            codes = exc.get_codes()
            field, (msg,) = next(codes.iteritems())

            if field == 'non_field_errors':
                response.data['code'] = msg
            else:
                response.data['code'] = '%s_%s' % (field, msg)
        except:
            pass
    elif isinstance(exc, BasicException):
        response.data.update(exc.get_full_details())

    return response
