from django.db import models

class IntegerPair(models.Model):
    hour = models.IntegerField()
    load = models.IntegerField()