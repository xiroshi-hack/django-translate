from operator import mod
from django.db import models
from django.urls import reverse

class TranslatePage(models.Model):
    name = models.CharField(max_length=100)
    # slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
    # ?
    bio = models.CharField(max_length=200, default='bio mavjud emas')

    def __str__(self):
        return self.name
