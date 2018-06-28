# -*- coding: utf-8 -*-
import logging

from django.db import transaction
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view


from shaw.exception import SHException
from shaw.schema import check_body_keys, validate_value, check_params_keys
from user.serializers import UserSerializer, validate_and_save
from utils.func import phone_parse


LOG = logging.getLogger(__name__)


@api_view(['PUT'])
@transaction.atomic
def forget_password(request):
    data = request.data
    check_body_keys(data, ['password'])
    password = data['password']
    phone = data.get('phone')
    # if phone and VerifyPhone.check(request.session, phone):
    #     auth.backend.change_password(phone, password)
    # email = data.get('email')
    # if email and VerifyEmail.check(request.session, email):
    #     auth.backend.change_password(email, password)
    return Response(status=status.HTTP_204_NO_CONTENT)


class UsersView(APIView):

    @transaction.atomic
    def post(self, request):
        data = request.data
        LOG.info('Create user request. | {}'.format(data))

        check_body_keys(data, ['password'])
        email = data.get('email')
        if not email:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        s = UserSerializer(data=data)
        user = validate_and_save(s)
        user.save()

        user = authenticate(request, **data)
        login(request, user)
        return Response(s.data, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def logout(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_profile(self, request):
        user = request.user
        result = UserSerializer(instance=user)
        user.last_login = timezone.now()
        user.save()
        return Response(result, status=status.HTTP_200_OK)

    def set_profile(self, request):
        data = request.data
        u_serializer = UserSerializer(request.user, data=data, partial=True)
        u_serializer.is_valid(raise_exception=True)
        u_serializer.save()
        return Response(u_serializer.data, status=status.HTTP_200_OK)

    @detail_route(methods=['get', 'put'])
    def profile(self, request):
        if request.method == 'GET':
            return self.get_profile(request)
        else:
            return self.set_profile(request)

    @detail_route(methods=['put'], url_path='reset-password')
    def set_password(self, request):
        data = request.data
        user = request.user
        check_body_keys(data, ['old_password', 'new_password'])
        user.check_password(data['old_password'], raise_exception=True)
        user.set_password(data['new_password'])
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @detail_route(methods=['put'], url_path='change-phone')
    @transaction.atomic
    def set_phone(self, request):
        user = request.user
        data = request.data
        check_body_keys(data, ['phone'])
        # VerifyPhone.check(request.session, data['phone'])
        # if phone_parse(user.phone):
        #     VerifyPhone.check(request.session, user.phone)
        s = UserSerializer(user, data={'phone': data['phone']}, partial=True)
        validate_and_save(s)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @detail_route(methods=['put'], url_path='change-email')
    @transaction.atomic
    def set_email(self, request):
        user = request.user
        data = request.data
        check_body_keys(data, ['email'])
        # VerifyEmail.check(request.session, data['email'])
        # if user.email:
        #     VerifyEmail.check(request.session, user.email)
        s = UserSerializer(user, data={'email': data['email']}, partial=True)
        validate_and_save(s)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update_relation(self, request):
        user = request.user
        data = request.data
        check_body_keys(data, ['type', 'uuid'])
        type = data['type']
        # validate_value(type, const.REL_USER_ACTIONS)
        # if type == const.REL_USER_FOLLOW:
        #     relation.follow_user(user, data['uuid'])
        # if type == const.REL_USER_UN_FOLLOW:
        #     relation.unfollow_user(user, data['uuid'])
        result = {'message': '关注成功'}
        return Response(result, status=status.HTTP_200_OK)
