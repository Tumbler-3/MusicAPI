from django.db import models
from apps.User.models import Author


class Genre(models.Model):
    name = models.CharField(verbose_name='genre name', max_length=200)
    description = models.TextField(verbose_name='genre description')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Genre',
        verbose_name_plural = 'Genres'


class Album(models.Model):
    name = models.CharField(verbose_name='album name', max_length=200)
    length = models.DurationField(verbose_name='album length')
    genre = models.ManyToManyField(
        Genre, verbose_name='album genre', max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    cover = models.ImageField(verbose_name='album cover')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Album',
        verbose_name_plural = 'Albums'


class Song(models.Model):
    name = models.CharField(verbose_name='song name', max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    length = models.DurationField(verbose_name='song length')
    genre = models.ManyToManyField(Genre, verbose_name='song genre')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Song',
        verbose_name_plural = 'Songs'

    def __str__(self):
        return f'{self.name}'
