from django.db import models
from apps.Genre.models import Genre
from apps.Author.models import Author
from apps.Album.models import Album

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
