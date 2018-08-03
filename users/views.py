# -*- coding: utf-8 -*-
import logging
import random
import string
import os
import hashlib
from time import time
import oss2
from django.http import Http404
import uuid

from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser
from django.conf import settings
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
from rest_framework.views import APIView
from django.core.files.images import get_image_dimensions
from rest_framework.renderers import TemplateHTMLRenderer

from shaw.schema import check_body_keys, check_params_keys
from users.serializers import UserSerializer
from app.models import User, EmailCertification
from utils import const
from rest_framework import views
from users.tasks import sync_reset_password_task


LOG = logging.getLogger(__name__)


def generate_random_password():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))


def upload_pic(file_name, file_obj):
    auth = oss2.Auth(settings.OSS_KEY, settings.OSS_SECRET)
    bucket = oss2.Bucket(auth, settings.END_POINT, settings.BUCKET_NAME, enable_crc=False)

    remote_name = settings.OSS_DIR + '/' + file_name
    result = bucket.put_object(remote_name, file_obj)
    if result.status == 200:
        return 'https://{}.{}/{}/{}'.format(settings.BUCKET_NAME, settings.END_POINT, settings.OSS_DIR, file_name)
    return ''


class UploadAvatarView(APIView):
    parser_classes = (MultiPartParser, FileUploadParser, FormParser,)

    def post(self, request):
        file_obj = request.FILES.get('file')
        file_name, file_ext = os.path.splitext(file_obj.name)
        if file_ext.upper() not in ['.PNG', '.JPG', '.JEPG', '.GIF']:
            msg = 'Invalid image file type, should be png jpg jepg gif!'
            result = {'success': False, 'msg': msg}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        width, height = get_image_dimensions(file_obj)
        print 'width, ', height, width
        if width > const.AVATAR_WIDTH or height > const.AVATAR_LENGTH:
            error_msg = 'Invalid dimensions: it should be lower than 1080*1650!'
            resp_result = {"message": error_msg, "success": False}
            return Response(resp_result, status=400)

        img_size = file_obj.size if file_obj.size else 0
        if img_size > const.AVATAR_MAX_SIZE:
            error_msg = 'Invalid size: the size should be lower than 600KB！'
            resp_result = {"msg": error_msg, "success": False}
            return Response(resp_result, status=400)

        hashed_file_name = hashlib.md5(file_obj.name.encode("UTF-8") + str(time())).hexdigest()
        full_name = '{0}{1}'.format(hashed_file_name, file_ext)
        avatar_url = upload_pic(file_name=full_name, file_obj=file_obj)
        result = {'success': True, 'url': avatar_url}
        return Response(result, status=status.HTTP_200_OK)


class UploadImageView(APIView):
    parser_classes = (MultiPartParser, FileUploadParser, FormParser,)

    def post(self, request):
        file_obj = request.FILES.get('file')
        file_name, file_ext = os.path.splitext(file_obj.name)
        hashed_file_name = hashlib.md5(file_obj.name.encode("UTF-8") + str(time())).hexdigest()
        full_name = '{0}{1}'.format(hashed_file_name, file_ext)
        avatar_url = upload_pic(file_name=full_name, file_obj=file_obj)
        result = {'success': True, 'url': avatar_url}
        return Response(result, status=status.HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt
def user_login(request):
    user = authenticate(request, **request.data)
    if user:
        login(request, user)
        result = UserSerializer(instance=user).data
        return Response(result, status=status.HTTP_200_OK)
    else:
        result = {'success': False, 'msg': 'Email or password error!'}
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


@csrf_exempt
@api_view(['GET'])
def certify_email(request):
    params = request.query_params
    code = params.get('code')
    if not code or not EmailCertification.objects.filter(code=code).exists():
        raise Http404

    # check_params_keys(params, ['email', 'phone'], exclusion=True)
    # result = False
    # for field in ('phone', 'email'):
    #     if params.get(field):
    #         result |= User.objects.filter(**{field: params[field]}).exists()
    cer_obj = EmailCertification.objects.get(code=code)
    result = {'email': cer_obj.email}
    return Response(result, status=200)


class CertifyEmailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'certify_email.html'

    def get(self, request, *args, **kwargs):
        params = request.query_params
        code = params.get('code')
        if not code or not EmailCertification.objects.filter(code=code).exists():
            result = {
                'success': False,
                'msg': 'Invalid code!',
            }
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        else:
            cer_obj = EmailCertification.objects.filter(code=code).first()
            return Response({'email': cer_obj.email}, status=200)


@csrf_exempt
@api_view(['POST'])
def certify_password(request):
    data = request.data
    code = data.get('code')
    first_password = data.get('first_password')
    second_password = data.get('second_password')
    if not code or first_password.upper() != second_password.upper():
        msg_str = 'Invalid code or password does not match!'
        result = {
            'success': False,
            'msg': msg_str,
        }
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

    certify_obj = EmailCertification.objects.get(code=code)
    user = User.objects.filter(email=certify_obj.email).first()
    user.set_password(second_password)
    user.save()

    login(request, user)

    result = {
        'success': True,
        'msg': 'Reset password success!'
    }
    return Response(result, status=status.HTTP_200_OK)


@api_view(['POST'])
@transaction.atomic
@csrf_exempt
def forget_password(request):
    data = request.data
    email = data.get('email')
    if not email or not User.objects.filter(email=email).exists():
        result = {
            'success': False,
            'msg': 'Invalid email address!',
        }
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

    if not EmailCertification.objects.filter(email=email).exists():
        uuid_str = uuid.uuid4().hex
        cer_obj = EmailCertification.objects.create(email=email, code=uuid_str)
        msg_str = 'Reset password to email:[{}] succeeded!'.format(email)
        result = {
            'success': True,
            'msg': msg_str,
        }

        post_data = {
            'email': cer_obj.email,
            'code': str(uuid_str)
        }
        sync_reset_password_task.delay(**post_data)
        return Response(result, status=status.HTTP_200_OK)
    else:
        latest_obj = EmailCertification.objects.filter(email=email).latest('created_at')
        date_now = timezone.now()
        delta = date_now - latest_obj.created_at
        if delta.seconds < EmailCertification.EXPIRE_TIME:
            result = {
                'success': False,
                'msg': 'Forget password forbidden in short time!',
            }

            return Response(result, status=status.HTTP_200_OK)
        else:
            uuid_str = uuid.uuid4().hex
            latest_obj.code = uuid_str
            latest_obj.save()
            msg_str = 'Reset password to email:[{}] succeeded!'.format(email)
            result = {
                'success': True,
                'msg': msg_str,
            }

            post_data = {
                'email': latest_obj.email,
                'code': str(uuid_str)
            }
            sync_reset_password_task.delay(**post_data)
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
        user = request.user
        password = request.data.get('password', )
        user.set_password(password)
        user.save()
        logout(request)
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
