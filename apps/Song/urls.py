from django.urls import path
from apps.Song.views import SongViewAPI, SongDetailViewAPI


urlpatterns = [
    path('song/', SongViewAPI.as_view()),
    path('song/<int:id>/', SongDetailViewAPI.as_view()),
]