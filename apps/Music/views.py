from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.Music.models import Genre, Album, Song
from apps.Music.serializers import GenreModelSerializer, AlbumModelSerializer, SongModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from apps.Music.service import AlbumFilter, SongFilter
from django.shortcuts import render

def main(request):
    return render(request, 'main.html')


class GenreViewAPI(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer
    pagination_class = PageNumberPagination


class GenreDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer
    lookup_field = 'id'


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


class SongViewAPI(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SongFilter


class SongDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer
    lookup_field = 'id'
