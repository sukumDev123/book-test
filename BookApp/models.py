from django.db import models

# Create your models here.
class BookModel(models.Model):
    name_book = models.CharField(max_length=255, blank=True)
    name_author = models.CharField(max_length=255, blank=True)
    detail = models.TextField()
