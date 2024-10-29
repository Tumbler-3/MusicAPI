from django.db import models


# Creating Genre Model for Database
class Genre(models.Model):
    name = models.CharField(verbose_name='genre name', max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Genre',
        verbose_name_plural = 'Genres'
