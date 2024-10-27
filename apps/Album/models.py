from django.db import models
from apps.Genre.models import Genre
from apps.Author.models import Author

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
