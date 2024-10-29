from django.db import models
from apps.Genre.models import Genre
from apps.Author.models import Author
from apps.Album.models import Album


# Creating Song Model for Database
class Song(models.Model):
    name = models.CharField(verbose_name='song name', max_length=200)

    # album field is connected to Genre field via Foreign key connection
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, verbose_name='song album', blank=True, null=True)

    # genre field is connected to Genre field via Many to many connection
    genre = models.ManyToManyField(
        Genre, verbose_name='song genre', blank=True)

    # author field is connected to Genre field via Foreign key connection
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, verbose_name='song author', blank=True, null=True)
    file = models.FileField(verbose_name="song file", upload_to='media/')

    class Meta:
        verbose_name = 'Song',
        verbose_name_plural = 'Songs'

    def __str__(self):
        return f'{self.name}'
