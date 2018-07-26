# -*- coding: utf-8 -*-
from celery import shared_task
from celery.signals import task_success, task_failure

from .email_mixins import send_email_change_password


@shared_task
def sync_reset_password_task(**kwargs):
    password = kwargs.get('password')
    email = kwargs.get('email')
    send_email_change_password(email=email, password=password)
    print '>>> sync_reset_password_task run success!'


@task_success.connect(sender=sync_reset_password_task)
def reset_password_task_success_handler(result=None, **kwargs):
    print '>>> reset_password_task_success_handler: run OK'


@task_failure.connect(sender=sync_reset_password_task)
def reset_password_task_failure_handler(**kwargs):
    print '>>> reset_password_task_failure_handler: run, fail'


'''
celery -A markone_server worker -l info -P eventlet
celery -A markone_server beat -l info
celery -A markone_server flower
celery -A markone_server flower --basic_auth=markonenote:markonenote
'''