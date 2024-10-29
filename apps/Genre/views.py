from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.Genre.models import Genre
from apps.Genre.serializers import GenreModelSerializer
from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


# View for Genre Serializer
class GenreViewAPI(ListCreateAPIView):
    queryset = Genre.objects.all() # Data taken from Genre model
    serializer_class = GenreModelSerializer # Using Genre serializer for showing and creating
    pagination_class = PageNumberPagination # pagination


# Detain view for Genre Serializer
class GenreDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all() # Data taken from Genre model
    serializer_class = GenreModelSerializer # Using Genre serializer for showing, updating, deleting
    lookup_field = 'id' # showing 1 object via id