# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView


class DomainIndexView(APIView):
    def get(self, request, *args, **kwargs):
        resp = {'success': True, 'msg': 'OK'}
        return Response(resp, status=200)
