from django_filters import rest_framework as rf
from apps.Song.models import Song


class CharInFilter(rf.BaseInFilter, rf.CharFilter):
    pass


class SongFilter(rf.FilterSet):
    genre = CharInFilter(field_name='genre__name', lookup_expr='in')
    album = CharInFilter(field_name='album__name', lookup_expr='in')

    class Meta:
        model = Song
        fields = ('author', 'genre', 'album')
