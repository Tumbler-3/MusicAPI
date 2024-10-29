from rest_framework import serializers
from apps.Genre.models import Genre


# Creating Genre Serializer
class GenreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre # I used Genre model as base for Album Serializer
        fields = '__all__'
