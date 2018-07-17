# -*- coding: utf-8 -*-
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated

from app.models import Notes, Sections, User
from app.serializers import NotesSerializer, SectionsSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.filter(is_active=True).order_by('-updated_at')
    serializer_class = NotesSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('is_active', )

    search_fields = ('title',)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        # user = User.objects.last()
        return self.queryset.filter(user=user)

    def perform_destroy(self, instance):
        instance.is_active = False
        Sections.objects.filter(notes=instance).update(is_active=False)
        instance.save()


class SectionsViewSet(viewsets.ModelViewSet):
    queryset = Sections.objects.filter(is_active=True).order_by('-updated_at')
    serializer_class = SectionsSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('remark',)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        # user = User.objects.last()
        query = self.queryset.filter(user=user)
        return query

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    @list_route(methods=['get'])
    def highlight(self, request):
        query = self.queryset.filter(highlight=True).order_by('-updated_at')
        self.queryset = query
        return super(SectionsViewSet, self).list(request)

    @list_route(methods=['get'])
    def trash(self, request):
        query = self.queryset.filter(trash=True).order_by('-updated_at')
        self.queryset = query
        return super(SectionsViewSet, self).list(request)
