# -*- coding: utf-8 -*-
import logging
import smtplib
import random

from django.conf import settings
from django.core.mail import send_mail

from utils.exceptions import InvalidValue
from utils import const

LOG = logging.getLogger(__name__)


def base_email_send(email, subject, content):
    LOG.info('Send email. | %s %s %s', email, subject, content)
    try:
        return send_mail(subject, content, settings.EMAIL_HOST_USER, [email])
    except smtplib.SMTPRecipientsRefused:
        raise InvalidValue(detail='Mailbox not found or access denied')


def send_email_code(email, code=None):
    code = code if code else str(random.randint(100000, 999999))
    subject = const.EMAIL_CODE_SUBJECT
    expire_str = ', this code will expires in {} hours'.format(settings.CODE_EXPIRY_TIME/3600)
    content = const.EMAIL_CODE_CONTENT + code + expire_str
    base_email_send(email=email, subject=subject, content=content)


def send_email_change_password(email, password):
    subject = const.EMAIL_PASSWORD_SUBJECT
    expire_str = ', this code will expires in {} hours'.format(settings.CODE_EXPIRY_TIME/3600)
    content = const.EMAIL_PASSWORD_CONTENT + password + expire_str
    base_email_send(email=email, subject=subject, content=content)


