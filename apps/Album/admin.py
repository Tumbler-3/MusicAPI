from django.contrib import admin
from apps.Album.models import Album

# registering Album model to admin panel
admin.site.register(Album)

