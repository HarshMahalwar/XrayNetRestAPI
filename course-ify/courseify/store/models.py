from django.db import models


class courseInfo(models.Model):
    name = models.CharField(max_length=200)
