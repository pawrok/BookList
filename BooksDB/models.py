from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    publication_date = models.CharField(max_length=64, blank=True, null=True)
    ISBN = models.BigIntegerField(blank=True, null=True)
    page_count = models.IntegerField(blank=True, null=True)
    cover_src = models.CharField(max_length=256, blank=True, null=True)
    language = models.CharField(max_length=64, blank=True, null=True)
