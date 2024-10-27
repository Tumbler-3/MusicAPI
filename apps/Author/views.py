from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.Author.models import Author
from apps.Author.serializers import AuthorModelSerializer


class AuthorViewAPI(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    pagination_class = PageNumberPagination


class AuthorDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    lookup_field = 'id'
