from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.Song.models import Song
from apps.Song.serializers import SongModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from apps.Song.service import SongFilter
from pathlib import Path
from rest_framework.exceptions import ValidationError


# View for Song Serializer
class SongViewAPI(ListCreateAPIView):
    queryset = Song.objects.all()  # Data taken from Song model
    # Using Song serializer for showing and creating
    serializer_class = SongModelSerializer
    pagination_class = PageNumberPagination  # pagination
    filter_backends = (DjangoFilterBackend,)  # filtration backend
    filterset_class = SongFilter  # filtration for view

    def post(self, request, *args, **kwargs):  # modified post method for music files
        file = request.data.dict()['file']
        # allowed music file extensions
        file_exts = ('.mp3', '.m4a', '.wav', '.wma', '.aac')

        if not Path(str(file)).suffix in file_exts:  # checks if posted file in allowed list
            raise ValidationError(
                f'Audio accepted only in: {file_exts}')

        # creating new Song object
        return self.create(request, *args, **kwargs)


# Detain view for Song Serializer
class SongDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()  # Data taken from Song model
    # Using Song serializer for showing, updating, deleting
    serializer_class = SongModelSerializer
    lookup_field = 'id'  # showing 1 object via id
