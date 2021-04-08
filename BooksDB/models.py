from django.db import models


class MyDataBase(models.model):
    col = models.CharField(max_length=10)
