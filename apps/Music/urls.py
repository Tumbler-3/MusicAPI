from django.urls import path
from apps.Music.views import GenreViewAPI, GenreDetailViewAPI, AlbumViewAPI, AlbumDetailViewAPI, SongViewAPI, SongDetailViewAPI


urlpatterns = [
    path('genre/', GenreViewAPI.as_view()),
    path('genre/<int:id>/', GenreDetailViewAPI.as_view()),
    path('album/', AlbumViewAPI.as_view()),
    path('album/<int:id>/', AlbumDetailViewAPI.as_view()),
    path('song/', SongViewAPI.as_view()),
    path('song/<int:id>/', SongDetailViewAPI.as_view()),
]