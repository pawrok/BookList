from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64, default='')
    author = models.CharField(max_length=64, default='')
    publication_date = models.DateField(default=None)
    ISBN = models.IntegerField()
    page_count = models.IntegerField()
    cover_src = models.CharField(max_length=256, default='')
    language = models.CharField(max_length=64, default='')
