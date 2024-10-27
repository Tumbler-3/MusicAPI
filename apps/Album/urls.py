from django.urls import path
from apps.Album.views import AlbumViewAPI, AlbumDetailViewAPI


urlpatterns = [
    path('album/', AlbumViewAPI.as_view()),
    path('album/<int:id>/', AlbumDetailViewAPI.as_view()),
]