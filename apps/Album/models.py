from django.db import models
from apps.Genre.models import Genre
from apps.Author.models import Author


# Creating album Model for Database
class Album(models.Model):
    name = models.CharField(verbose_name='album name', max_length=200)
    
    # author and genre fields is connected to Genre field via Foreign key connection
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, verbose_name='album genre', blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='album author', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Album',
        verbose_name_plural = 'Albums'
