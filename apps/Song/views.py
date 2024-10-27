from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.Song.models import Song
from apps.Song.serializers import SongModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from apps.Song.service import SongFilter


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
