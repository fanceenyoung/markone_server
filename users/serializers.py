# -*- coding: utf-8 -*-
import re

from django.db import transaction
from rest_framework import serializers

from app.models import User


def validate_and_save(serializer, **kws):
    serializer.is_valid(raise_exception=True)
    return serializer.save(**kws)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('country', 'updated_at', )
        extra_kwargs = {
            'password': {'required': False, 'write_only': True},
            'avatar': {'required': False},
        }

    def validate(self, data):
        if not self.partial and not data.get('email'):
            msg = 'Missing email in post data !'
            raise serializers.ValidationError(msg)
        return data

    def validate_email(self, email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if email and not re.match(regex, email):
            msg = 'Invalid email format!'
            raise serializers.ValidationError(msg)
        return email

    @transaction.atomic
    def create(self, validated_data):
        country = validated_data.get('location', {}).get('country')
        if country:
            validated_data['country'] = country
        email = validated_data.get('email')
        if not User.objects.filter(email=email).exists():
            return User.objects.create_user(**validated_data)
        return User.objects.filter(email=email).first()

    @transaction.atomic
    def update(self, user, validated_data):
        country = validated_data.get('location', {}).get('country')
        if country:
            user.country = country

        password = validated_data.pop('password', None)
        if password:
            user.set_password(password)

        return super(UserSerializer, self).update(user, validated_data)
