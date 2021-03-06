# -*- coding: utf-8 -*-
import uuid
import jsonfield
import logging
import random

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from app import base_models
from utils import const

LOG = logging.getLogger(__name__)


def generate_random_avatar():
    ava_list = const.USER_AVATARS
    return random.choice(ava_list)


class BaseUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, password, email, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        LOG.debug("Test password {}".format(password))
        if password is None:
            password = 'password'
        user.set_password(password)
        if 'avatar' not in extra_fields:
            user.avatar = generate_random_avatar()
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, phone='', email=''):
        return self.get(phone=phone, email=email)

    def create_user(self, password=None, email=None, **extra_fields):
        return self._create_user(password, email, **extra_fields)

    def create_superuser(self, email, password):
        return self.create_user(password, email, is_admin=True)


@python_2_unicode_compatible
class User(AbstractBaseUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, default='')
    nickname = models.CharField(max_length=128, default='')
    email = models.CharField(max_length=512, db_index=True, unique=True)
    phone = models.CharField(max_length=32, db_index=True, blank=True, default='')
    type = models.CharField(max_length=16, choices=const.USER_TYPES, default=const.US_VISITOR)
    location = jsonfield.JSONField(blank=True)
    country = models.CharField(max_length=32, blank=True, default='China')
    avatar = models.CharField(max_length=256, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    token = models.TextField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = BaseUserManager()

    def __str__(self):
        return '{} {}'.format(self.uuid, self.name)


@python_2_unicode_compatible
class Notes(base_models.Object):
    user = models.ForeignKey(User, related_name='notes')
    title = models.CharField(max_length=128, default='')
    origin = models.CharField(max_length=256, default='')

    data = jsonfield.JSONField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Notes:{}'.format(self.uuid)


@python_2_unicode_compatible
class Sections(base_models.Object):
    user = models.ForeignKey(User)
    notes = models.ForeignKey(Notes, related_name='sections')
    position = models.PositiveIntegerField(default=0)
    remark = models.TextField(blank=True)
    origin = models.CharField(max_length=256, default='', blank=True)
    highlight = models.BooleanField(default=False)
    trash = models.BooleanField(default=False)

    is_video = models.BooleanField(default=False)
    image = models.CharField(max_length=256, default='', blank=True)

    start_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    end_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    link = models.CharField(max_length=1024, default='', blank=True)

    data = jsonfield.JSONField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Sections:{}'.format(self.uuid)


@python_2_unicode_compatible
class EmailCertification(base_models.Time):
    EXPIRE_TIME = 3600 * 12
    code = models.CharField(max_length=512)
    email = models.CharField(max_length=512)
    status = models.BooleanField(default=True)
    send = models.BooleanField(default=False)
    count = models.IntegerField(default=0)

    def __str__(self):
        return 'EmailCertification:{}{}'.format(self.code, self.email)


@receiver(post_save, sender=User)
def meta_add_user_default_section(sender, **kwargs):
    if kwargs.get('created'):
        user = kwargs.get('instance')
        if not Notes.objects.filter(user=user, title=const.DEFAULT_NOTES_TITLE).exists():
            note = Notes.objects.create(user=user, title=const.DEFAULT_NOTES_TITLE, origin=const.DEFAULT_SITE)
            for each in const.DEFAULT_SECTION_LIST:
                if 'https://' not in each:
                    se_dict = {'user': user, 'notes': note, 'remark': each, 'origin': const.DEFAULT_SITE}
                else:
                    se_dict = {'user': user, 'notes': note, 'remark': '', 'origin': const.DEFAULT_SITE, 'is_video': True, 'image': each}
                Sections.objects.create(**se_dict)
