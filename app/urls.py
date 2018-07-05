# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from utils.func import SelfRouter, SimpleRouter
from app.views import SectionsViewSet, NotesViewSet

router = SimpleRouter()
router.register('sections', SectionsViewSet, base_name='sections')
router.register('notes', NotesViewSet, base_name='notes')

urlpatterns = [
    url(r'^', include(router.urls)),
]
