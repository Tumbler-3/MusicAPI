from rest_framework import serializers
from apps.Music.models import Song, Album, Genre


class GenreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AlbumModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'


class SongModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'
