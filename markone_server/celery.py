# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'markone_server.settings')

celery_app = Celery(
    'markone_server',
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_BROKER_URL,
    # include=['user.tasks']
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modulaes from all registered Django app configs.
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@celery_app.task
def hello_test(arg):
    print(arg)


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, hello_test.s('run hello_test'), name='add every 10')

    # Executes every Monday morning at 7:30 a.m.

    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     hello_test.s('run every Monday '),
    # )
