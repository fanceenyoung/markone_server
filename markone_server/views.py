# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from djangomako.shortcuts import render_to_response


class DomainIndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        resp = {'success': True, 'msg': 'OK'}
        return Response(resp, status=200)


class IndexView(View):

    @method_decorator(ensure_csrf_cookie)
    def get(self, request):
        return render_to_response('index.html', {})


@ensure_csrf_cookie
def index(request):
    resp = {'success': True, 'msg': 'OK'}
    return render_to_response('index.html', resp)
