# -*- coding: utf-8 -*-
import logging
import random
import string

from django.db import transaction
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework import mixins
from django.views.decorators.csrf import csrf_exempt

from shaw.schema import check_body_keys, check_params_keys
from users.serializers import UserSerializer
from app.models import User
from utils import const
from rest_framework import views
from users.celery_tasks import sync_reset_password_task
from users.email_mixins import send_email_change_password


LOG = logging.getLogger(__name__)


def generate_random_password():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))


@api_view(['POST'])
@csrf_exempt
def user_login(request):
    user = authenticate(request, **request.data)
    if user:
        login(request, user)
        result = UserSerializer(instance=user).data
        return Response(result, status=status.HTTP_200_OK)
    else:
        result = {'success': False, 'msg': 'Email or password error'}
        return Response(result, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def check_user(request):
    params = request.query_params
    check_params_keys(params, ['email', 'phone'], exclusion=True)
    result = False
    for field in ('phone', 'email'):
        if params.get(field):
            result |= User.objects.filter(**{field: params[field]}).exists()
    return Response({'result': result})


@api_view(['PUT'])
@transaction.atomic
@csrf_exempt
def forget_password(request):
    data = request.data
    email = data.get('email')
    if not email or not User.objects.filter(email=email).exists():
        error_msg = {
            'success': False,
            'msg': 'Invalid email address!',
        }
        return Response(error_msg, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(email=email).first()
    if user:
        password = generate_random_password()
        user.set_password(password)
        user.save()
        post_data = {
            'password': password,
            'email': email,
        }
        # send_email_change_password(email=email, password=password)
        sync_reset_password_task.delay(**post_data)
    msg_str = 'Reset password to email:[{}] succeeded!'.format(email)
    result = {
        'success': True,
        'msg': msg_str,
    }
    return Response(result, status=status.HTTP_200_OK)


class LogoutView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_profile(self, request):
        user = request.user
        # user = User.objects.first()
        result = UserSerializer(instance=user).data
        user.last_login = timezone.now()
        user.save()
        return Response(result, status=status.HTTP_200_OK)

    def set_profile(self, request):
        data = request.data
        u_serializer = UserSerializer(request.user, data=data, partial=True)
        u_serializer.is_valid(raise_exception=True)
        u_serializer.save()
        return Response(u_serializer.data, status=status.HTTP_200_OK)

    @detail_route(methods=['get', 'put'], permission_classes=[IsAuthenticated])
    def profile(self, request):

        if request.method == 'GET':
            return self.get_profile(request)
        else:
            return self.set_profile(request)

    @detail_route(methods=['put'], url_path='reset_password', permission_classes=[IsAuthenticated])
    def reset_password(self, request):
        data = request.data
        user = request.user
        check_body_keys(data, ['old_password', 'new_password'])
        user.check_password(data['old_password'], raise_exception=True)
        user.set_password(data['new_password'])
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def help_center(self, request):
        result = {
            'questions': const.QUESTIONS,
            'feedback_image': const.FEEDBACK_IMAGE,
            'contact': const.FEEDBACK_CONTACT,
            'members': const.ABOUT_US_MEBS,
            'about_us': const.ABOUT_US_DESC,
        }
        return Response(result, status=status.HTTP_200_OK)