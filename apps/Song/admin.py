from django.contrib import admin
from apps.Song.models import Song

# registering Song model to admin panel
admin.site.register(Song)
