# -*- coding: utf-8 -*-
from rest_framework import serializers

from app.models import Notes, Sections


class SectionsSerializer(serializers.ModelSerializer):
    notes_title = serializers.CharField(source='notes.title', read_only=True)
    start_time = serializers.DecimalField(max_digits=10, decimal_places=2, default=0, required=False)
    end_time = serializers.DecimalField(max_digits=10, decimal_places=2, default=0, required=False)
    position = serializers.IntegerField(default=0, required=False)
    image = serializers.CharField(default='', required=False)
    remark = serializers.CharField(default='', required=False)

    class Meta:
        model = Sections
        fields = ('uuid', 'user', 'notes', 'remark', 'origin', 'highlight', 'trash',
                  'is_video', 'image', 'updated_at', 'position', 'notes_title',
                  'start_time', 'end_time', 'link',)


class SimpleSectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sections
        fields = ('uuid', 'remark', 'origin', 'highlight', 'trash',
                  'is_video', 'image', 'updated_at', 'position',
                  'start_time', 'end_time', 'link',)


class NotesSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    def get_sections(self, instance):
        sections = instance.sections.all().filter(is_active=True).order_by('-updated_at')
        return SimpleSectionsSerializer(sections, many=True).data

    class Meta:
        model = Notes
        fields = ('uuid', 'user', 'title', 'origin', 'updated_at', 'sections',)


class NotesHightlightSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    def get_sections(self, instance):
        sections = instance.sections.all().filter(is_active=True, highlight=True).order_by('-updated_at')
        return SimpleSectionsSerializer(sections, many=True).data

    class Meta:
        model = Notes
        fields = ('uuid', 'user', 'title', 'origin', 'updated_at', 'sections',)


class NotesTrashSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    def get_sections(self, instance):
        sections = instance.sections.all().filter(is_active=True, trash=True).order_by('-updated_at')
        return SimpleSectionsSerializer(sections, many=True).data

    class Meta:
        model = Notes
        fields = ('uuid', 'user', 'title', 'origin', 'updated_at', 'sections',)
