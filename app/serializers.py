# -*- coding: utf-8 -*-
from rest_framework import serializers

from app.models import Notes, Sections


class SectionsSerializer(serializers.ModelSerializer):
    notes_id = serializers.CharField(source='notes.uuid')
    notes_title = serializers.CharField(source='notes.title', required=False)

    class Meta:
        model = Sections
        fields = ('uuid', 'remark', 'origin', 'highlight', 'trash',
                  'is_video', 'image', 'updated_at', 'notes_id', 'notes_title',)


class NotesSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    def get_sections(self, instance):
        sections = instance.sections.all().filter(is_active=True).order_by('-updated_at')
        return SectionsSerializer(sections, many=True).data

    class Meta:
        model = Notes
        fields = ('uuid', 'title', 'origin', 'updated_at', 'sections',)
