from rest_framework import serializers
from apps.Song.models import Song


# Creating Song Serializer
class SongModelSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')
    genre_names = serializers.ReadOnlyField(source='genre.name')
    album_name = serializers.ReadOnlyField(source='album.name')

    class Meta:
        model = Song  # I used Song model as base for Album Serializer
        fields = '__all__'
