from rest_framework import serializers
from apps.Author.models import Author


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
