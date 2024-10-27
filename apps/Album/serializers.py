from rest_framework import serializers
from apps.Album.models import Album


class AlbumModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'
