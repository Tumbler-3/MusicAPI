from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.Album.models import Album
from apps.Album.serializers import AlbumModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from apps.Album.service import AlbumFilter
from django.shortcuts import render


class AlbumViewAPI(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AlbumFilter


class AlbumDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer
    lookup_field = 'id'