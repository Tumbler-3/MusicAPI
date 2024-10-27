from rest_framework import serializers
from apps.Song.models import Song


class SongModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'
