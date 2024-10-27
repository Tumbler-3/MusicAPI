from django.db import models

class Author(models.Model):
    name = models.CharField(verbose_name='futhor name', max_length=200)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Author',
        verbose_name_plural = 'Authors'
