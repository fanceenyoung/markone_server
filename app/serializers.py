# -*- coding: utf-8 -*-
from rest_framework import serializers

from app.models import Notes, Sections


class SectionsSerializer(serializers.ModelSerializer):
    notes_id = serializers.CharField(source='notes.uuid')
    notes_title = serializers.CharField(source='notes.title')
    start_time = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)
    end_time = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        model = Sections
        fields = ('uuid', 'remark', 'origin', 'highlight', 'trash',
                  'is_video', 'image', 'updated_at', 'position',
                  'notes_id', 'notes_title', 'start_time', 'end_time',
                  'link',)


class SimpleSectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sections
        fields = ('uuid', 'remark', 'origin', 'highlight', 'trash',
                  'is_video', 'image', 'updated_at', 'position',)


class NotesSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    def get_sections(self, instance):
        sections = instance.sections.all().filter(is_active=True).order_by('-updated_at')
        return SimpleSectionsSerializer(sections, many=True).data

    class Meta:
        model = Notes
        fields = ('uuid', 'title', 'origin', 'updated_at', 'sections',)


class NotesHightlightSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    def get_sections(self, instance):
        sections = instance.sections.all().filter(is_active=True, highlight=True).order_by('-updated_at')
        return SimpleSectionsSerializer(sections, many=True).data

    class Meta:
        model = Notes
        fields = ('uuid', 'title', 'origin', 'updated_at', 'sections',)


class NotesTrashSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    def get_sections(self, instance):
        sections = instance.sections.all().filter(is_active=True, trash=True).order_by('-updated_at')
        return SimpleSectionsSerializer(sections, many=True).data

    class Meta:
        model = Notes
        fields = ('uuid', 'title', 'origin', 'updated_at', 'sections',)
