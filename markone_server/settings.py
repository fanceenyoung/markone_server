# -*- coding: utf-8 -*-

import os

def get_local_env(name, default=None):
    import envs
    return os.getenv(name) or getattr(envs, name, default)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^!-+anzlrgsjc=u!@*eo1hjdtq^=*2je+wsrw7%wh@gtu95!cg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_local_env('DJANGO_DEBUG') == 'True'
TEST = DEBUG and get_local_env('TEST') == 'True'


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mako',
    'djangomako',
    'rest_framework',
    'rest_framework.authtoken',
    'django_redis',
    'markone_server',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.middlewares.DisableCSRF',
]

AUTHENTICATION_BACKENDS = [
    'user.backends.MarkOneAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'markone_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'markone_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DB_SQLITE = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'db.sqlite3',
}

DB_MYSQL = {
    "ENGINE": "django.db.backends.mysql",
    "NAME": get_local_env('DB_NAME', 'markone_server'),
    "USER": get_local_env('DB_USER', 'root'),
    "PASSWORD": get_local_env('DB_PASSWORD', ''),
    "HOST": get_local_env('DB_HOST_MYSQL', '127.0.0.1'),
    "PORT": get_local_env('DB_PORT_MYSQL', 3306)
}

DATABASES = {
    'default': DB_SQLITE if DEBUG else DB_MYSQL
}
API_VERSION = 'v1'

AUTH_USER_MODEL = 'app.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PAGINATION_CLASS': 'utils.func.PageNumberPagination',
    'PAGE_SIZE': int(get_local_env('PAGE_SIZE', 10)),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'EXCEPTION_HANDLER': 'utils.exceptions.custom_exception_handler',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',
}



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# REDIS_SETTINGS
REDIS_HOST = 'redis://localhost:6379/'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_HOST + "0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 邮箱设置
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
# EMAIL_HOST_USER = 'Markonenote@163.com'
# EMAIL_HOST_PASSWORD = 'mayiji55'
EMAIL_HOST_USER = 'zhangtianyiww@163.com'
EMAIL_HOST_PASSWORD = '163mail'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# 验证码有效时间
CODE_EXPIRY_TIME = 12 * 60 * 60
CODE_SEND_INT = 60

# CELERY SETTINGS
CELERY_BROKER_URL = REDIS_HOST + "8"
CELERY_RESULT_BACKEND = REDIS_HOST + "8"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'

BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 31104000}

# 阿里云OSS存储
OSS_KEY = 'LTAIUXXAywNcD8v3'
OSS_SECRET = 'RlrJI1W6wn679wz94DS5NXHZfi6lm7'
END_POINT = 'oss-cn-beijing.aliyuncs.com'
BUCKET_NAME = 'audionetwork'
OSS_DIR = 'markone'
