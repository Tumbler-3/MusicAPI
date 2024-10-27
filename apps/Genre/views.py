from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.Genre.models import Genre
from apps.Genre.serializers import GenreModelSerializer
from django.shortcuts import render

def main(request):
    return render(request, 'main.html')


class GenreViewAPI(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer
    pagination_class = PageNumberPagination


class GenreDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer
    lookup_field = 'id'