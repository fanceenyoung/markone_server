# -*- coding: utf-8 -*-

import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class LocalUrlView(APIView):
    # permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        abs_path = os.getcwd()

        resp_dict = {
            'url': abs_path,
            'success': True,
        }
        return Response(resp_dict, status=status.HTTP_200_OK)
