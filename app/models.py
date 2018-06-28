# -*- coding: utf-8 -*-
import uuid
import jsonfield
import logging

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, Group

from utils import const

LOG = logging.getLogger(__name__)


class BaseUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, password, email, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        LOG.debug("Test password {}".format(password))
        user.set_password(password)
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
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=512, db_index=True, blank=True, default='')
    phone = models.CharField(max_length=32, db_index=True, blank=True, default='')
    type = models.CharField(max_length=16, choices=const.USER_TYPES, default=const.US_VISITOR)
    location = jsonfield.JSONField(blank=True)
    country = models.CharField(max_length=32, blank=True, default='China')
    avatar = models.CharField(max_length=256, blank=True, default='')
    groups = models.ManyToManyField(Group)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)

    objects = BaseUserManager()

