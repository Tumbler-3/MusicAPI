from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.Music.models import Genre, Album, Song
from apps.Music.serializers import GenreSerializer, AlbumSerializer, SongSerializer


class GenreViewAPI(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination


class GenreDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'



class AlbumViewAPI(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = PageNumberPagination


class AlbumDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = 'id'
    


class SongViewAPI(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = PageNumberPagination


class SongDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'id'