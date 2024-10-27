# Generated by Django 5.1.2 on 2024-10-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='genre name')),
                ('description', models.TextField(verbose_name='genre description')),
            ],
            options={
                'verbose_name': ('Genre',),
                'verbose_name_plural': 'Genres',
            },
        ),
    ]