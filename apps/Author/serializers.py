from rest_framework import serializers
from apps.Author.models import Author


# Creating Author Serializer
class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author  # I used Author model as base for Album Serializer
        fields = '__all__'
