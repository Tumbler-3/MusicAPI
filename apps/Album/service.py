from django_filters import rest_framework as rf
from apps.Album.models import Album


# CharInFilter for string filtration
class CharInFilter(rf.BaseInFilter, rf.CharFilter):
    pass


# String filtration for Album Serializer
class AlbumFilter(rf.FilterSet):
    genre = CharInFilter(field_name='genre__name', lookup_expr='in')
    
    class Meta:
        model = Album
        fields = ('author', 'genre')
