from rest_framework import serializers
from apps.Genre.models import Genre


class GenreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
