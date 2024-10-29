from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.Album.models import Album
from apps.Album.serializers import AlbumModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from apps.Album.service import AlbumFilter


# View for Album Serializer
class AlbumViewAPI(ListCreateAPIView):
    queryset = Album.objects.all() # Data taken from Album model
    serializer_class = AlbumModelSerializer # Using Album serializer for showing and creating
    pagination_class = PageNumberPagination # pagination
    filter_backends = (DjangoFilterBackend,) #filtration backend
    filterset_class = AlbumFilter # filtration for view


# Detain view for Album Serializer
class AlbumDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all() # Data taken from Album model
    serializer_class = AlbumModelSerializer # Using Album serializer for showing, updating, deleting
    lookup_field = 'id' # showing 1 object via id