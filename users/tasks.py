# -*- coding: utf-8 -*-
from celery import shared_task
from celery.signals import task_success, task_failure
from celery.schedules import crontab
import datetime
from dateutil import relativedelta

from users.email_mixins import send_email_change_password
from markone_server.celery import celery_app
from app.models import Sections


# 异步任务
@shared_task
def sync_reset_password_task(**kwargs):
    password = kwargs.get('password')
    email = kwargs.get('email')
    send_email_change_password(email=email, password=password)
    return 'sync_reset_password_task run success!'


@task_success.connect(sender=sync_reset_password_task)
def reset_password_task_success_handler(result=None, **kwargs):
    print '>>> reset_password_task_success_handler: run OK'


@task_failure.connect(sender=sync_reset_password_task)
def reset_password_task_failure_handler(**kwargs):
    print '>>> reset_password_task_failure_handler: run, fail'


# 定时任务
@celery_app.task
def periodic_fresh_trash(arg):
    print '%s' % arg
    time_end = datetime.datetime.now() - relativedelta.relativedelta(months=1)
    Sections.objects.filter(trash=True, updated_at__gte=time_end).update(is_active=False)


@celery_app.on_after_finalize.connect
def setup_users_periodic_tasks(sender, **kwargs):
    # Executes every day morning at 3 a.m.
    sender.add_periodic_task(
        crontab(hour=3, minute=0,),
        periodic_fresh_trash.s('run everyday trash check'),
    )

'''
celery -A markone_server worker -l info -P eventlet
celery -A markone_server beat -l info
celery -A markone_server flower
celery -A markone_server flower --basic_auth=markonenote:markonenote
'''
