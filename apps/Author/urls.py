from django.urls import path
from apps.Author.views import AuthorViewAPI, AuthorDetailViewAPI


urlpatterns = [
    path('author/', AuthorViewAPI.as_view()),
    path('author/<int:id>/', AuthorDetailViewAPI.as_view()),
]