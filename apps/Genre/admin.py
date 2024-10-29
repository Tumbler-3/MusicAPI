from django.contrib import admin
from apps.Genre.models import Genre

# registering Genre model to admin panel
admin.site.register(Genre)

