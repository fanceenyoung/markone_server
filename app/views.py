# -*- coding: utf-8 -*-
import datetime
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from app.models import Notes, Sections
from app.serializers import (NotesSerializer, SectionsSerializer,
                             NotesHightlightSerializer, NotesTrashSerializer)


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.filter(is_active=True).order_by('-updated_at')
    serializer_class = NotesSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('is_active', )

    search_fields = ('title', 'sections__remark')
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

    def perform_destroy(self, instance):
        instance.is_active = False
        Sections.objects.filter(notes=instance).update(is_active=False)
        instance.save()

    @list_route(methods=['get'])
    def check_notes(self, request):
        params = request.query_params
        origin = params.get('origin')
        if not origin or origin is None:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        note_obj = Notes.objects.filter(origin=origin, user=request.user).first()
        result = NotesSerializer(instance=note_obj).data if note_obj else {}
        return Response(result, status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def highlight(self, request):
        query = self.queryset.filter(sections__highlight=True).distinct().order_by('-updated_at')
        self.serializer_class = NotesHightlightSerializer
        self.queryset = query
        return super(NotesViewSet, self).list(request)

    @list_route(methods=['get'])
    def trash(self, request):
        query = self.queryset.filter(sections__trash=True).distinct().order_by('-updated_at')
        self.serializer_class = NotesTrashSerializer
        self.queryset = query
        return super(NotesViewSet, self).list(request)


class SectionsViewSet(viewsets.ModelViewSet):
    queryset = Sections.objects.filter(is_active=True).order_by('-highlight', '-updated_at')
    serializer_class = SectionsSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('remark', 'link', 'origin', )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        query = self.queryset.filter(user=user)
        return query

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        note_obj = instance.notes
        note_obj.update_at = datetime.datetime.now()
        note_obj.save()
        return super(SectionsViewSet, self).update(request)
