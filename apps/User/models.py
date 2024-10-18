from django.db import models
from django.contrib.auth.models import AbstractUser

class Author(AbstractUser):
    name = models.CharField(blank=True,null=False, max_length = 50)
    username = models.CharField(blank=True,null=False, max_length = 50, unique=True)
    password = models.CharField(blank=True,null=True, max_length = 30)
    first_name = models.CharField(blank=False,null=False, max_length = 100)
    last_name = models.CharField(blank=True,null=True, max_length = 100)
    description = models.TextField(blank=True, null=True)
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name","email","password"]
