from django_filters import rest_framework as rf
from apps.Song.models import Song


# CharInFilter for string filtration
class CharInFilter(rf.BaseInFilter, rf.CharFilter):
    pass


# String filtration for Album Serializer
class SongFilter(rf.FilterSet):
    genre = CharInFilter(field_name='genre__name', lookup_expr='in')
    album = CharInFilter(field_name='album__name', lookup_expr='in')
    name = CharInFilter(field_name='name', lookup_expr='in')

    class Meta:
        model = Song
        fields = ('author', 'genre', 'album', 'name')
