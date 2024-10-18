from django.db import models
from apps.User.models import Author


class Genre(models.Model):
    name = models.CharField(verbose_name='genre_name', max_length=200)
    desription = models.TextField(verbose_name='genre_description')


class Album(models.Model):
    name = models.CharField(verbose_name='album_name', max_length=200)
    length = models.TimeField(verbose_name='album_length')
    genre = models.CharField(verbose_name='album_genre', max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='album_genre')


class Song(models.Model):
    name = models.CharField(verbose_name='song_name', max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    length = models.TimeField(verbose_name='song_length')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
