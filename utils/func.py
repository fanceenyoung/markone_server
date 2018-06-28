# -*- coding: utf-8 -*-
import phonenumbers
from rest_framework import pagination
from rest_framework import routers

from utils.exceptions import InvalidPhoneNumber


def phone_parse(number, region=None, raise_exception=False):
    try:
        ph = phonenumbers.parse(number, region=region)
        if phonenumbers.is_valid_number(ph):
            return ph
    except:
        pass
    if raise_exception:
        raise InvalidPhoneNumber()


class SimpleRouter(routers.SimpleRouter):
    def __init__(self):
        super(SimpleRouter, self).__init__()
        self.trailing_slash = '[/]?'


class SelfRouter(SimpleRouter):
    routes = [
        routers.Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'post': 'create',
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy',
            },
            name='{basename}',
            initkwargs={'suffix': 'Instance'},
        ),
        routers.DynamicDetailRoute(
            url=r'^{prefix}/{methodname}{trailing_slash}$',
            name='{basename}-{methodname}',
            initkwargs={}
        )
    ]


class PageNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100
