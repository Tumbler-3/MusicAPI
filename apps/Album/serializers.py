from rest_framework import serializers
from apps.Album.models import Album


# Creating Album Serializer
class AlbumModelSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name') 
    genre_names = serializers.ReadOnlyField(source='genre.name')

    class Meta:
        model = Album # I used Album model as base for Album Serializer
        fields = '__all__'
