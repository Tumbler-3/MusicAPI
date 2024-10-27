from django.urls import path
from apps.Genre.views import GenreViewAPI, GenreDetailViewAPI


urlpatterns = [
    path('genre/', GenreViewAPI.as_view()),
    path('genre/<int:id>/', GenreDetailViewAPI.as_view()),
]