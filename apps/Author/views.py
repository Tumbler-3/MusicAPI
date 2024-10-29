from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.Author.models import Author
from apps.Author.serializers import AuthorModelSerializer

# View for Author Serializer
class AuthorViewAPI(ListCreateAPIView):
    queryset = Author.objects.all() # Data taken from Author model
    serializer_class = AuthorModelSerializer # Using Author serializer for showing and creating
    pagination_class = PageNumberPagination # pagination

# Detain view for Author Serializer
class AuthorDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all() # Data taken from Author model
    serializer_class = AuthorModelSerializer # Using Author serializer for showing, updating, deleting
    lookup_field = 'id' # showing 1 object via id
