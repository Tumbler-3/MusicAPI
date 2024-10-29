from django.db import models


# Creating Author Model for Database
class Author(models.Model):
    name = models.CharField(verbose_name='author name', max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Author',
        verbose_name_plural = 'Authors'
