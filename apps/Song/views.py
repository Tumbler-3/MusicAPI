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
    queryset = Song.objects.all() # Data taken from Song model
    serializer_class = SongModelSerializer # Using Song serializer for showing and creating
    pagination_class = PageNumberPagination # pagination
    filter_backends = (DjangoFilterBackend,) # filtration backend
    filterset_class = SongFilter # filtration for view

    def post(self, request, *args, **kwargs): # modified post method for music files
        file = request.data.dict()['file']
        file_exts = ('.mp3', '.m4a', '.wav', '.wma', '.aac') #allowed music file extensions

        if not Path(str(file)).suffix in file_exts: # checks if posted file in allowed list
            raise ValidationError(
                f'Audio accepted only in: {file_exts}')

        return self.create(request, *args, **kwargs) #creating new Song object


# Detain view for Song Serializer
class SongDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all() # Data taken from Song model
    serializer_class = SongModelSerializer # Using Song serializer for showing, updating, deleting
    lookup_field = 'id' # showing 1 object via id
