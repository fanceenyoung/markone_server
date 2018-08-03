# -*- coding: utf-8 -*-
from celery import shared_task
from celery.signals import task_success, task_failure
from celery.schedules import crontab
import datetime
from dateutil import relativedelta
from django.db.models import F

from markone_server.celery import celery_app
from app.models import Sections, EmailCertification
from users.email_mixins import send_email_change_password


# 异步任务
@celery_app.task
def sync_reset_password_task(**kwargs):
    email = kwargs.get('email')
    code = kwargs.get('code')
    send_email_change_password(email=email, code=code)
    print 'sync_reset_password_task run success!'
    return {'email': email, 'code': code}


@task_success.connect(sender=sync_reset_password_task)
def reset_password_task_success_handler(result=None, **kwargs):
    print 'reset_password_task_success_handler: run OK'
    email = result.get('email')
    code = result.get('code')
    EmailCertification.objects.filter(code=code, email=email).update(count=F('count')+1, send=True)


@task_failure.connect(sender=sync_reset_password_task)
def reset_password_task_failure_handler(**kwargs):
    print '>>> reset_password_task_failure_handler: run, fail'


# 定时任务
@celery_app.task
def periodic_fresh_trash(arg):
    print '%s' % arg
    time_end = datetime.datetime.now() - relativedelta.relativedelta(months=1)
    Sections.objects.filter(trash=True, updated_at__gte=time_end).update(is_active=False)


@celery_app.task
def hello_test(arg):
    print ">>> run hello_test"


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # sender.add_periodic_task(10.0, hello_test.s('what the fuck'), name='add every 10')
    # sender.add_periodic_task(10.0, periodic_fresh_trash.s('fresh trash'), name='add every 10')
    # Executes every day morning at 3 a.m.
    sender.add_periodic_task(
        crontab(hour=3, minute=0,),
        periodic_fresh_trash.s('run everyday trash check'),
    )

'''
celery -A markone_server worker --autoreload -l info -P eventlet
celery -A markone_server beat --autoreload -l info
celery -A markone_server flower
celery -A markone_server flower --basic_auth=markonenote:markonenote
'''
