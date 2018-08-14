# -*- coding: utf-8 -*-

import os
import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import make_aware
from django.db.models import Count, Case, When

from app.models import User, Notes, Sections


class LocalUrlView(APIView):
    # permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        abs_path = os.getcwd()

        resp_dict = {
            'url': abs_path,
            'success': True,
        }
        return Response(resp_dict, status=status.HTTP_200_OK)


def calculate_users_count():
    users_query = User.objects.all()
    total_info = {}
    day_info = users_query.extra({'day': "date(created_at)"}).values('day').annotate(count=Count('pk')).order_by('day')
    total_info['total'] = users_query.count()
    total_info['day_info'] = day_info
    return total_info


def calculate_notes_count():
    query = Notes.objects.all()
    total_info = {}
    day_info = query.extra({'day': "date(created_at)"}).values('day').annotate(count=Count('pk')).order_by('day')
    total_info['total'] = query.count()
    total_info['day_info'] = day_info
    return total_info


def calculate_sections_count():
    query = Sections.objects.all()
    total_info = {}
    day_info = query.extra({'day': "date(created_at)"}).values('day').annotate(count=Count('pk')).order_by('day')
    total_info['total'] = query.count()
    total_info['day_info'] = day_info
    return total_info


class DashboardView(APIView):
    # permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        end_data = calculate_users_count()
        notes_data = calculate_notes_count()
        sections_data = calculate_sections_count()

        resp_dict = {
            'users': end_data,
            'notes': notes_data,
            'sections': sections_data,
            'success': True,
        }
        return Response(resp_dict, status=status.HTTP_200_OK)
