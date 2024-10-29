from django.db import models
from apps.Genre.models import Genre
from apps.Author.models import Author


# Creating album Model for Database
class Album(models.Model):
    name = models.CharField(verbose_name='album name', max_length=200)
    genre = models.ManyToManyField(  # genre field is connected to Genre field via Many to many connection
        Genre, verbose_name='album genre', max_length=100, blank=True, null=True)
    author = models.ForeignKey(  # author field is connected to Genre field via Foreign key connection
        Author, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Album',
        verbose_name_plural = 'Albums'
