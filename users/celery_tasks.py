# -*- coding: utf-8 -*-
from celery import task

from .email_mixins import send_email_change_password


@task()
def sync_reset_password_task(**kwargs):
    password = kwargs.get('password')
    email = kwargs.get('email')
    send_email_change_password(email=email, password=password)
    print 'sync_reset_password_task run success!'
