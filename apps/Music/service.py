from django_filters import rest_framework as rf
from apps.Music.models import Genre, Album, Song


class CharInFilter(rf.BaseInFilter, rf.CharFilter):
    pass


class AlbumFilter(rf.FilterSet):
    author = CharInFilter(field_name='author__name', lookup_expr='in')
    genre = CharInFilter(field_name='genre__name', lookup_expr='in')
    
    class Meta:
        model = Album
        fields = ('author', 'genre')


class SongFilter(rf.FilterSet):
    author = CharInFilter(field_name='author__name', lookup_expr='in')
    genre = CharInFilter(field_name='genre__name', lookup_expr='in')
    album = CharInFilter(field_name='album__name', lookup_expr='in')
    
    class Meta:
        model = Song
        fields = ('author', 'genre', 'album')