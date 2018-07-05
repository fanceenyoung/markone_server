# -*- coding: utf-8 -*-
from rest_framework import serializers

from app.models import Notes, Sections


class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = ('uuid', 'remark', 'origin', 'highlight', 'trash',
                  'is_video', 'image', 'created_at', 'notes')


class NotesSerializer(serializers.ModelSerializer):
    sections = SectionsSerializer(many=True, read_only=True)

    class Meta:
        model = Notes
        fields = ('uuid', 'title', 'origin', 'created_at', 'sections',)
