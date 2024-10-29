from django.contrib import admin
from apps.Author.models import Author

# registering Author model to admin panel
admin.site.register(Author)
